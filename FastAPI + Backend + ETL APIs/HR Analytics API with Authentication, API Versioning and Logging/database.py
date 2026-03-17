from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

db_user=os.getenv("db_user")
db_password=os.getenv("db_password")
db_host=os.getenv("db_host")
db_port=os.getenv("db_port")
db_name=os.getenv("db_name")

if not all([db_user,db_password,db_host,db_port,db_name]):
    raise ValueError("Database environment variables are not set properly")

db_url=f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine=create_engine(db_url)
sessionlocal=sessionmaker(bind=engine)

Base=declarative_base()