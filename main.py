from website import create_app

app = create_app()

# Only if this file is ran, will the following line be executed:
if __name__ == '__main__':
    # Will run flask application and start up the web server; everytime a change is made to python code it will
    # automatically rerun the web server
    app.run(debug=True) # Remove this code when you're done coding
