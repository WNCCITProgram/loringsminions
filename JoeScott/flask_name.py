"""
    Flask Name Program
    Author: Joe Scott
    Date: 09/25/2025
    Purpose: Display user name on local website
"""

# get flask library
from flask import Flask, request
import requests

# Assign flask object. Bypass different name
app = Flask(__name__)

# Create head line
@app.route("/hello/<name>")
def hello_name(name):
    return f"<hl>Hello, {name}<hl>"

# Display browser
@app.route("/")
def hello_world():
    user_agent = request.headers.get("User-Agent")
    return f"""<h2>Hello, world!<h2>
    <p>Your browser is {user_agent}<p>
    """

# Run program
if __name__ == "__main__":
    app.run(debug=True)

# You can locate this message at http://localhost:5000/
