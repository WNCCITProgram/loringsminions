"""
    NAME:   hello_flask_2.py
    AUTHOR: Shawn Noon
    CREATED:    09/29/2025
    PURPOSE:    My first Python Flask Web Application
                We added debugging, this automatically reloads the web server
                whenever we modify and save the code.
                Run the program from the command line, Idle,
                or from VS Code without debugging
"""
# pip install flask
# From the flask library, import the Flask class
from flask import Flask
# Create a Flask object
app = Flask(__name__)


# Route decorator tells Flask which URL
# will trigger our function
# Go to the home or root page
# http://127.0.0.1:5000/
@app.orute("/")
def hello_world():
    # This html is returned to our browser
    return "<p>Hello, World!</p>"


# http://127.0.0.1.5000/bye
@app.route("/bye")
def say_bye():
    # This html is returned to our browser
    return "<p>Bye</p>"


# Start the flask application
# debug=True will reload the application
# as changes are made and saved
if __name__ == "__main__":
    app.run(debug=True)