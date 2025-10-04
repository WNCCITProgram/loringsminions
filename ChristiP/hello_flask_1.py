"""
    Name: hello_flask_1.py
    Author: Christi P
    Created: 10/3/25
    Purpose: my first python flask web application
    2 - added debugging
"""

# pip install flask
# from the flask library, import the flask class
from flask import Flask, request

# create an instance of the flask class
app = Flask(__name__)

# route decorator tells Flask which URL
# will trigger our function
# go to the home or root page
# http://127.0.0.1:5000/
@app.route("/")
def hello_world():
    # this html is returned to our browser
    user_agent = request.headers.get("User-Agent")
    return f"""<p>Hello, World!</p>
    <p>Your browser is {user_agent}</p>
    """

# http://127.0.0.1:5000/bye
@app.route("/bye")
def say_bye():
    # this html is returned to our browser
    return "<p>Bye!!</p>"

# routing the decorator function hello_name
# http://127.0.0.1:5000/hello/YourName
@app.route('/hello/<name>')
def hello_name(name):
    return f"<hl>Hello {name}!<hl/>"

# start the flask application
if __name__ == "__main__":
    app.run(debug=True)