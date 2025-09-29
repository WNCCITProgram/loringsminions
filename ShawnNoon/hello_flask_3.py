"""
    NAME:   hello_flask_3.py
    AUTHOR: Shawn Noon
    CREATED:    09/29/2025
    PURPOSE:    My first Python Flask Web Application
                We added debugging, this automatically reloads the web server
                whenever we modify and save the code.
                Run the program from the command line, Idle,
                or from VS Code without debugging
                Added variables
"""
# pip install flask
# From the flask library, import the Flask class and request
from flask import Flask, request
# Create a Flask object
app = Flask(__name__)

# Routing the decorator function hello_name
# http://127.0.0.1:5000/hello/YourName
@app.route('/hello/<Shawn>')
def hello_name(name):
    return f"<h1>Hello {name}!<h1/>"

# Route decorator tells Flask which URL
# will trigger our function
# Go to the home or root page
# http://127.0.0.1:5000/
@app.orute("/")
def hello_world():
    # This html is returned to our browser
    user_agent = request.heeaders.get("User-Agent")
    return f"""<h2>Hello, World!</h2>
    <p>Your browser is {user_agent}</p>
    """


# http://127.0.0.1.5000/bye
@app.route("/bye")
def say_bye():
    # This html is returned to our browser
    return "<p>Bye</p>"


# Start the flask application
# debug=True will reload the application
# as changes are made and saved
if __name__ == "__main__":
    app.run(debug=True)
