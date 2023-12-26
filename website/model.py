from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy  # Import Flask-SQLAlchemy

# Initialize Flask-SqlAlchemy
db = SQLAlchemy

Base = declarative_base()


class Outbreak(Base):
    __tablename__ = 'outbreak_data'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    disease = Column(String)
    date = Column(DateTime)
    iso2 = Column(String)
    iso3 = Column(String)
    year = Column(Integer)
    icd10n = Column(String)
    icd103n = Column(String)
    icd104n = Column(String)
    icd10c = Column(String)
    icd103c = Column(String)
    icd104c = Column(String)
    icd11c1 = Column(String)
    icd11c2 = Column(String)
    icd11c3 = Column(String)
    icd11l1 = Column(String)
    icd11l2 = Column(String)
    icd11l3 = Column(String)
    disease_name = Column(String)
    DONS = Column(String)
    definition = Column(String)


def init_db():
    db.create_all()


def get_outbreaks_by_country_and_year(country, year):
    # Use Flask-SqlAlchemy's scoped_session to manage sessions in Flask context
    session = db.session

    # Write a query to get all disease outbreaks for a specific country in the last 10 years
    query = session.query(Outbreak).filter(Outbreak.country == country, Outbreak.date >= f'{year - 10}-01-01').all()
    return query
