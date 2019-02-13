

import settings

import os
import sys
import pandas as pd
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#file location
PATH = "C:/Users/julia/Documents/coding/codingchallenges/qbiz/Archive/DataHealthProfiles/"


def main():
    #create engine
    engine = create_engine(settings.DATABASE_URL, client_encoding='utf8')

    #and connect
    con = engine.connect()

    meta = MetaData(bind=con, reflect=True)

    #get list of file paths
    files = [[fileN, os.path.join(PATH, fileN)] for fileN in os.listdir(PATH) if fileN.endswith(".csv")]


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

if __name__ == "__main__":
    main()
