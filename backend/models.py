from pymongo import MongoClient
from config import Config

# Connect to MongoDB
client = MongoClient(Config.MONGO_URI)
db = client.get_database()

# Collections
users_collection = db.users
profiles_collection = db.profiles