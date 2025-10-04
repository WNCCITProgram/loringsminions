"""
    Name: calculator.py
    Author: Christi P
    Created: 10/3/25
    Purpose: add 2 numbers together
"""
# pip install flask
# import the flask class, render_template, and request
from flask import Flask, render_template, request# create Flask object
app = Flask(__name__)

# go to the home or root page
# http://127.0.0.1:5000/

@app.route("/", methods=["GET", "POST"])
def home():
    # if the request is POST
    if request.method == "POST":
        # get input from user into variables
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")

        # calculate the sum of the 2 numbers
        sum = float(num1) + float(num2)