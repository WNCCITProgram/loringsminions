"""
    Joe's flask program
    Date: 09/18/2025
    Purpose: Use flask.
"""

from flask import Flask

# Assign flask object. Bypass different name
app = Flask(__name__)

# Return message to server
@app.route("/")
def hi_world():
    return "<p> Hello there!"

# Run programs
if __name__ == "__main__":
        app.run(debug=True)

# You can locate this message at http://localhost:5000/