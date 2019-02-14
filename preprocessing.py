"""Class holding all the preprocessing and data manipulation functions"""
import  pandas as pd
import numpy as np
import settings
import sqlalchemy as sqla
import time
import os
from sklearn.preprocessing import StandardScaler
from scipy import stats

from indicator_categories import ind_cat as INDICATOR_CATEGORIES


PATH = "C:/Users/julia/Documents/coding/codingchallenges/qbiz/Archive/DataHealthProfiles/"


class Preprocess():
    def __init__(self):
        pass

    def populate_db(self, csv_dir=PATH):
        """This populates the PostgreSQL database that I created using PGAdmin.
        DB settings are in settings.py"""

        #create engine
        engine = sqla.create_engine(settings.DATABASE_URL, client_encoding='utf8')

        #and connect
        con = engine.connect()

        meta = sqla.MetaData(bind=con, reflect=True)

        #get list of file paths
        files = [[fileN, os.path.join(csv_dir, fileN)] for fileN in os.listdir(csv_dir) if fileN.endswith(".csv")]


        print("{} files gathered...".format(len(files)))
        print()

        for [fileN, path] in files:
            try:
                fileN = str(fileN.replace("CSV.csv", "")).lower()

                df = pd.read_csv(path, skiprows = 19)
                df = df.rename(columns = lambda x: x.strip().replace(' ', '_').replace('(', '').replace(')', '').replace('%', '').upper() )
                df = df[['ONS_CODE_OLD', 'ONS_CODE_NEW', 'AREA_NAME',
                         'ONS_CLUSTER', 'PERIOD', 'INDICATOR_VALUE',
                         'LOWER_95_CI', 'UPPER_95_CI']]
                df.to_sql(name = fileN, con = con)
                print("Sucessfully added {}".format(fileN))
            except Exception as e:
                print("Error adding {}".format(fileN))
                print(str(e))

    #As there are 48 tables, it is not practical to use the
    #sqlalchemy classes in sqalchemcy_declarative.py
    #Instead, I create SQL queries and execute directly:

    def create_db_view(self):
        """Creates a DB view to speed up queries.
        I would usually execute this in DBeaver but
        to show my workings..."""

        engine = sqla.create_engine(settings.DATABASE_URL, client_encoding='utf8')
        with engine.connect() as conn:
            meta = sqla.MetaData(bind=conn, reflect=True)
            table_names = list(meta.tables.keys())
            #remove time_series data
            table_names = [x for x in table_names if "trend" not in x]

            query = "CREATE VIEW indicators AS\n"
            query += self.__SQL_select_all_data(table_names)
            result = conn.execute(query)
            print("View Created")

    def get_df_from_db_w_view(self, fast = True):
        """Extracts a df with relevant information from db.
        Note that, for this project, the data can easily fit in memory
        so it will be more convenient to extract everything at once."""

        #set up db connection
        engine = sqla.create_engine(settings.DATABASE_URL, client_encoding='utf8')
        with engine.connect() as conn:
            meta = sqla.MetaData(bind=conn, reflect=True)
            table_names = list(meta.tables.keys())
            #remove time_series data
            table_names = [x for x in table_names if "trend" not in x]
            columns = ["\"AREA_NAME\"", "\"ONS_CODE_NEW\""] + table_names
            query = "SELECT "
            #Add column string
            for col in columns:
                query += "{}, ".format(col)
            query = query[:-2] #remove ", "
            query += " FROM indicators"
            df = pd.read_sql(query, con=conn, columns =columns)
        df = df.set_index("ONS_CODE_NEW", drop=True)
        return df

    def get_df_from_db_no_view(self):
        """Extracts a df with relevant information from db without using view.
        I used this for speed comparison w. view query.
        (see preprocessing_and_analysis.ipynb for results)"""

        #set up db connection
        engine = sqla.create_engine(settings.DATABASE_URL, client_encoding='utf8')
        with engine.connect() as conn:
            meta = sqla.MetaData(bind=conn, reflect=True)
            table_names = list(meta.tables.keys())

            #remove time_series data
            table_names = [x for x in table_names if "trend" not in x]

            query = self.__SQL_select_all_data(table_names)
            res = conn.execute(query)

            columns = ["\"AREA_NAME\"", "\"ONS_CODE_NEW\""] + table_names

            df = pd.read_sql(query, con=conn, columns =columns)
        df = df.set_index("ONS_CODE_NEW", drop=True)
        return df

    def __SQL_select_all_data(self, table_names):
        """Helper function to create SQL query joining all tables on
        ONS_CODE_NEW with renamed col headings given by table name.

        Note: trend data should be ommitted"""


        num_tables = len(table_names)

        #first table will be used frequently in query:
        first = table_names[0]
        query = """SELECT {}.\"AREA_NAME\", {}.\"ONS_CODE_NEW\",\n"""
        query = query.format(first, first)
        for idx, table_name in enumerate(table_names):
            #Alias each indicator value as the name of the indicator
            #(i.e. as the table name)
            col_as_alias = """{}."INDICATOR_VALUE" as {}"""
            col_as_alias = col_as_alias.format(table_name, table_name)

            if idx != (num_tables - 1):
                query += col_as_alias + ",\n"
            else:
                query += col_as_alias + "\n"

        #Now construct the FROM ...
        query += "FROM {}\n".format(first)
        for table_name in table_names[1:]: #iterate through all but first
            join_sql = """inner join {} on {}.\"ONS_CODE_NEW\" = {}.\"ONS_CODE_NEW\"\n"""
            query += join_sql.format(table_name, first, table_name)

        return query


    def divide_into_ABC_DE(self, df):
        """"Accepts a df, indexes on ONS_CODE_NEW and splits into
        two dfs of indicators ABC and DE"""
        try:
            df = df.set_index("ONS_CODE_NEW", drop=True)
        except:
            pass
        try:
            df = df.drop(columns =["AREA_NAME"])
        except KeyError:
            pass

        ABC_cols = []
        DE_cols = []
        ind_cat = INDICATOR_CATEGORIES #dictionary

        for col in df.columns:
            if ind_cat[col] in ["A", "B", "C"]:
                ABC_cols.append(col)
            elif ind_cat[col] in ["D", "E"]:
                DE_cols.append(col)
            else:
                raise "column {} not in expected indicator categories".format(col)
        df1 = df[ABC_cols]
        df2 = df[DE_cols]

        return df1, df2

    def normalize_and_fill_nan(self, df):
        """Mean centre normalize and fill Nan with mean"""
        scaler = StandardScaler() #Mean centres and normalizes per feature

        scaler.fit(df)
        X = scaler.transform(df) #converts into numpy array
        X_names = dict(zip(range(len(df.columns)), df.columns))

        mean = np.nanmean(X, axis=1).reshape((1, -1))

        #Find indicies that you need to replace
        inds_X = np.where(np.isnan(X))

        X[inds_X] = np.take(mean, inds_X[0], axis = 1)
        return X, X_names

    def remove_outliers(self, df):
        """Removes extreme outliers with z score > 4.
        This is not valid in general but is O.K. when running linear
        Regression as outliers will skew the predictions."""
        try:
            df = df.drop(columns =["AREA_NAME"])
        except KeyError:
            pass
        z = np.nan_to_num(np.abs(stats.zscore(df)))

        df_new =  df[(z < 4).all(axis=1)]
        print("{} datapoints reduced to {}".format(df.shape[0], df_new.shape[0]))
        return df_new




if __name__ == "__main__":
    prep = Preprocess()
    df = prep.get_df_from_db_w_view()
    df_ABC, df_DE = prep.divide_into_ABC_DE(df)
    print(df_ABC.shape, df_DE.shape )
