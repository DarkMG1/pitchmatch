from flask import Flask
from routes import api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register API routes
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)