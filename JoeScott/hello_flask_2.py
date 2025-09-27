"""
    Joe's Flask Program #2
    Date: 09/25/2025
    Purpose: Run flask with debugging.
"""
# get flask library
from flask import Flask

# Assign flask object. Bypass different name
app = Flask(__name__)

# Return message to server
# Route decorator tells flask which URL triggers our function
# Main directory
@app.route("/")
def hi_world():
    return "<p>Hello there!"

# Sub-Directory
@app.route("/bye")
def bye():
    # This HTML is returned to our browser
    return "<p>Bye!<p>"

# Run program with debug
if __name__ == "__main__":
    app.run(debug=True)

# You can locate this message at http://localhost:5000/