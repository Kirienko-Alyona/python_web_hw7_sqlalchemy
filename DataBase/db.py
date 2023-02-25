import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


config = configparser.RawConfigParser()
config.read("./config.ini")
username = config.get("DB", "username")
password = config.get("DB", "password")
db_name = config.get("DB", "db_name")
host = config.get("DB", "host")
port = config.get("DB", "port")

url_to_db = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"
Base = declarative_base()
engine = create_engine(url_to_db, echo=True, pool_size=5)
DBSession = sessionmaker(bind=engine)
session = DBSession()
