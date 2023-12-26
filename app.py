# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
#
# # Configure the Flask app with the database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///outbreak.db'
#
# # Suppress a Flask-SQLAlchemy warning
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # Initialize the Flask-SQLAlchemy extension
# db = SQLAlchemy(app)
#
#
# # Create tables
# from model import init_db, db
# init_db()
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
