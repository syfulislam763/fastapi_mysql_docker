from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import os
from dotenv import load_dotenv


load_dotenv()

# DB_URL = "mysql://root:root@172.17.0.1:3306/test_db"

DB_URL = "mysql://{0}:{1}@{2}:{3}/{4}".format(os.getenv("DATABASE_USERNAME"), os.getenv("DATABASE_PASSWORD"), os.getenv("DATABASE_HOST"), os.getenv("DATABASE_PORT"), os.getenv("DATABASE"))
# DB_URL = "sqlite:///.tst.db"
engine = create_engine(DB_URL)


# mysql_engine.connect().execute(text("create database if not exists {0}".format(db)))
# engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3306/{0}".format(db))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()