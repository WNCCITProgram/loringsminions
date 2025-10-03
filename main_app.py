
from flask import Flask, Blueprint, render_template

# Create a Blueprint with /cs as the URL prefix
cs_bp = Blueprint('cs', __name__, url_prefix='/cs')

@cs_bp.route("/")
def hello():
    return render_template("index.html")

# Create the Flask app
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(cs_bp)

if __name__ == "__main__":
    app.run(debug=True)
