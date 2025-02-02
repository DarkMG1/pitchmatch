from flask import Flask
from routes import api

app = Flask(__name__)

# Register API routes
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)