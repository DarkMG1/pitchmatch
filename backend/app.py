from flask import Flask, render_template
from routes import api

app = Flask(__name__)

# Register API routes
app.register_blueprint(api)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/profile/vc")
def profile():
    return render_template("vc-profile.html")

@app.route("/profile/startup")
def startup_profile():
    return render_template("startup-profile.html")

if __name__ == "__main__":
    app.run(debug=True)