from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///todos.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) # connect_args 세팅은 SQLite에서만 필요

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
# sessionmaker 함수를 통해 세션 생성

Base = declarative_base()
#  모델 정의를 위한 부모 클래스 생성  