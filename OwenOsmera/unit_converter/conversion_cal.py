"""
Hello_flask_2.py
Owen Osmera
9/18/25
start with flash
"""

# pip install flask
# from the flask library import the flask class
from flask import Flask, render_template, request


# create an instance of the flask class
app = Flask(__name__)

# Create a constant for the Conversion factor of mm to inches
CONVERSION_FACTOR = 0.0393701

#root folder for flask this will be the url for the aplication
@app.route("/", methods=["GET", "POST"])
def home():
    # if request.post
    if request.method == "POST":
        #Get inout from the user
        num1 = request.form.get("num1")
        # sum
        sum = float(num1) * CONVERSION_FACTOR
        sum = round(sum, 2)


        #This html is returned to our browser
        return render_template("result.html", sum=sum)
    
    #Otherwise we return index.html
    return render_template("index.html")


#Start the flask app
if __name__ == "__main__":
    app.run(debug=True)