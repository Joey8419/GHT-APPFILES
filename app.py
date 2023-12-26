from flask import Flask
from model import init_db, db

app = Flask(__name__)

# Configure the Flask app with the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///outbreak.db'

# Suppress a Flask-SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask-SQLAlchemy extension
db.init_app(app)

# Create tables
init_db()

if __name__ == '__main__':
    app.run(debug=True)
