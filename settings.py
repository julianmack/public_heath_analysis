
DATABASE_NAME = "health_profiles_qbiz"
DATABASE_USER = "julian.mack"
DATABASE_HOST = "localhost"
DATABASE_PASS = "passwordverysafe" #This isn't my normal password fyi
DATABASE_PORT = 5432

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'
DATABASE_URL = DATABASE_URL.format(DATABASE_USER, DATABASE_PASS, DATABASE_HOST,
                    DATABASE_PORT, DATABASE_NAME)
