from flask import Blueprint, render_template, request, flash

# Define that this file is the blueprint of the application that has a bunch of roots inside of it
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='Error!')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='Error!')
        elif password1 != password2:
            flash('Passwords DO NOT match', category='Error!')
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters.', category='Error!')
        else:
            # add user to database
            flash('Your account has been created!', category='Success!')

    return render_template("sign_up.html")
