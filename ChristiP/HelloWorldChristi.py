from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_World():
    return "<p>Hello, Flask! </p>"

if __name__ == "__main__":
    app.run()