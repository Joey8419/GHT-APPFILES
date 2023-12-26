from flask import Blueprint, render_template, request
from model import Outbreak # Import the Outbreak class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Define SQLAlchemy engine and session
engine = create_engine('sqlite:///outbreak.db')
Session = sessionmaker(bind=engine)
session = Session()


# Define that this file is the blueprint of the application that has a bunch of roots inside of it
views = Blueprint('views', __name__)


@views.route('/')
# This function will run everytime the '/' root is called in the url
def home():
    # Render the home.html template when the root URL is accessed
    return render_template("home.html")


@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # If the form is submitted (POST request), retrieve values from the form
        country = request.form.get('country')
        year = request.form.get('year')

        # Call the function to get disease outbreaks for the specified country and year
        outbreaks = get_outbreaks_by_country_and_year(country, int(year))

        # Render the results.html template with the obtained outbreaks
        return render_template('results.html', outbreaks=outbreaks)

    # If the method is not POST, render the search.html template
    return render_template('search.html')



