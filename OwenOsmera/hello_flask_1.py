"""
Hello_flask_1.py
Owen Osmera
9/18/25
start with flash
"""

# pip install flask
# from the flask library import the flask class
from flask import Flask

# create an instance of the flask class
app = Flask(__name__)

#root folder for flask this will be the url for the aplication
@app.route("/")
def hello_world():
    #This html is returned to our prowser
    return "<p>Hello, World!</p>"

#Start the flask app
if __name__ == "__main__":
    app.run()