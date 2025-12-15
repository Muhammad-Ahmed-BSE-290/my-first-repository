from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html", title="Home")

# About Us Page
@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

# Membership Page
@app.route("/membership")
def membership():
    return render_template("membership.html", title="Membership")

if __name__ == "__main__":
    app.run(debug=True)
