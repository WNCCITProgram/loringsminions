"""
Owen Osmera
"""

# import nessesary flask requiremnts
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# flask app
app = Flask(__name__)
# config database object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the object
db = SQLAlchemy(app)
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)