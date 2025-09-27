"""
    Joe's flask Template Program
    Date: 09/18/2025
    Purpose: Use flask to send message to local host
    from templates folder in VScode
"""

from flask import Flask, render_template

# Assign flask object. Bypass different name
app = Flask(__name__)

@app.route("/")
def hello_world():
    # Render html template and return
    return render_template("hello.html")

if __name__ == ("__main__"):
    app.run(debug=True)