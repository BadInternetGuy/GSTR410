"""
Code for GSTR 410 website

This is designed as a fairly simple website that will serve as essentially as
an online informational pamphlet. It will include my research in a different
format. It is coded in python using the Flask library. Bootstrap 4 is also
utilized to organize the individual pages. 

Special thanks to:
Dr. Deborah Martin
The internet
"""

from flask import Flask, render_template, redirect


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/esports")
def esports():
    return render_template("esports.html")

@app.route("/streamers")
def streamers():
    return render_template("streamers.html")

@app.route("/champions")
def champions():
    return render_template("champions.html")

@app.route("/cosmetics")
def cosmetics():
    return render_template("cosmetics.html")

#concerns the recent lawsuit filed against Riot Games for
#gender discrimination in the workplace
@app.route("/lawsuit")
def lawsuit():
    return render_template("lawsuit.html")

#concerns the private arbitrations that some were forced into and the
#resulting strike
@app.route("/arbitration")
def arbitration():
    return render_template("arbitration.html")

if __name__ == '__main__':
    app.run(debug=True)
