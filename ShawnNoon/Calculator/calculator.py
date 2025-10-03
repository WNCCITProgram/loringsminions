"""
    NAME:       calculator.py
    AUTHOR:     Shawn Noon
    CREATED:    10/02/2025
    PURPOSE:    Add 2 numbers together
"""

# pip install flask
# Import the Flask class, render_template, and request
from flask import Flask, render_template, request
# Create Flask object
app = Flask(__name__)

# Go to the home or root page
# http://127.0.0.1:5000/


@app.route("/", methods=["GET", "POST"])
def home():
    # If the request is POST
    if request.method == "POST":
        # Get input from user into variables
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")

        # Calculate the sum of the two numbers
        sum = float(num1) + float(num2)

        # Return the results using the variable sum
        # in a different web page
        return render_template("result.html", sum=sum)
    
    # Otherwise we return index.html with GET
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)