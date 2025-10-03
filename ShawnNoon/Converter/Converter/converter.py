from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Conversion of 1 kilogram to pounds
KG_TO_POUNDS = 2.20462

# Go to the home or root page
# http://127.0.0.1:5000/

@app.route("/", methods=["GET", "POST"])
def home():
    # If the request is POST
    if request.method == "POST":
        # Get input from user into variables
        num1 = request.form.get("num1")
        
        # Calculate user input into pounds
        pounds = float(num1) * KG_TO_POUNDS

        return render_template("result.html", pounds=pounds)
    
    # Otherwise we return index.html with GET
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)