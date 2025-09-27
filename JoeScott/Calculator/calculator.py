"""
    Flask Calculator Program
    Author: Joe Scott
    Date: 09/25/2025
    Purpose: Add 2 numbers together with flask
"""
# Import flask libraries
from flask import Flask, render_template, request

# Create flask object
app = Flask(__name__)

# To acces the home root page, go to:
# http://localhost:5000/

@app.route("/", methods=["GET", "POST"])
def home():
    # If the request is POST
    if request.method == "POST":
        # Get user input into variables
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")

        # Calculate
        sum = float(num1) + float(num2)

        # Return the results back to the web page
        return render_template("result.html", sum=sum)
    
    # Otherwise we return index.html with GET
    return render_template("index.html")

# Run program
if __name__ == "__main__":
    app.run(debug=True)
