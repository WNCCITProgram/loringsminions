"""
    NAME:   hello_flask_4.py
    AUTHOR: Shawn Noon
    CREATED:    09/29/2025
    PURPOSE:    First Python Flask web application 
"""
# pip install flask
# From the flask library, import the Flask class and render_template
from flask import Flask, render_template
# Create a Flask object
app = Flask(__name__)

@app.route("/")
def hello_world():
    # Render an HTML template and return
    return render_template("hello.html")

if __name__ == "__main__":
    app.run()


