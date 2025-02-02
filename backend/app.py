from flask import Flask, render_template, redirect
from routes import api

app = Flask(__name__, template_folder="../frontend", static_folder="../frontend")

# Register API routes
app.register_blueprint(api)

@app.route("/")
def landing():
    return redirect("/frontend/landing.html")

@app.route("/login")
def login():
    return redirect("/frontend/login.html")

@app.route("/signup")
def signup():
    return redirect("frontend/signup.html")

@app.route("/profile/vc")
def profile():
    return redirect("frontend/vc-profile.html")

@app.route("/profile/startup")
def startup_profile():
    return redirect("frontend/startup-profile.html")

if __name__ == "__main__":
    app.run(debug=True)