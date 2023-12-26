from sqlalchemy import Column, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy  # Import Flask-SQLAlchemy
from datetime import datetime

# Initialize Flask-SqlAlchemy
db = SQLAlchemy()

# Base = declarative_base() (didn't need because I'm using Flask-SQLAlchemy


class Outbreak(db.Model):
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

    # Added a column to store date and time of each search
    search_timestamp = Column(DateTime, default=datetime.utcnow)


def init_db():
    db.create_all()


def get_outbreaks_by_country_and_year(country, year):
    # Use Flask-SqlAlchemy's scoped_session to manage sessions in Flask context
    session = db.session

    # Write a query to get all disease outbreaks for a specific country in the last 10 years
    query = session.query(Outbreak).filter(Outbreak.country == country, Outbreak.date >= f'{year - 10}-01-01').all()
    return query


class Search(db.Model):
    # Define the Search model for storing search events
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each search
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to associate with the User model
    country = db.Column(db.String, nullable=False)  # Country selected in the search
    year = db.Column(db.Integer, nullable=False)  # Year selected in the search
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of when the search occurred


class User(db.Model):
    # Define the User model
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    searches = db.relationship('Search', backref='user', lazy=True)  # Relationship to the Search model, lazy loading
