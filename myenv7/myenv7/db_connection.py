from contextlib import contextmanager
import configparser
import pathlib

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from psycopg2 import Error


file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username = config.get("DB", "user")
password = config.get("DB", "password")
db_name = config.get("DB", "db_name")
host = config.get("DB", "host")
port = config.get("DB", "port")

url_to_db = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"

engine = create_engine(url_to_db, echo=True, pool_size=5)
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Base = declarative_base()


# @contextmanager
# def connection():
#     conn = None
#     try:
#         engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/postgres")
#         engine = create_engine(host="localhost", user="postgres", database="postgres",
#                        password="123456")
#         DBSession = sessionmaker(bind=engine)
#         session = DBSession()

#         Base = declarative_base()
#         yield conn
#         conn.commit()
#     except Error as error:
#         print(error)
#         conn.rollback()
#     finally:
#         if conn is not None:
#             conn.close()