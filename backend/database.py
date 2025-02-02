from pymongo import MongoClient
import os
from dotenv import load_dotenv

def write_vc(vs_in_json):
    try:
        # 1. Establish a connection to MongoDB
        load_dotenv("mongo.env")
        username= os.getenv('MONGO_USERNAME')
        password= os.getenv('MONGO_PASSWORD')

        client = MongoClient(f"mongodb+srv://{username}:{password}@pitchmatch.ehi9k.mongodb.net/?retryWrites=true&w=majority&appName=pitchmatch")
        db = client["pitchmatch"]
        collection = db["vc_info"]

        collection.insert_one(vs_in_json)
        print(f"Successfully inserted data into collection 'pitchmatch.vc_info' in database 'pitchmatch'.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'client' in locals() and client:  # Ensure client is defined and not None
            client.close()

def write_startup(startup_in_json):
    try:
        # 1. Establish a connection to MongoDB
        load_dotenv("mongo.env")
        username= os.getenv('MONGO_USERNAME')
        password= os.getenv('MONGO_PASSWORD')

        client = MongoClient(f"mongodb+srv://{username}:{password}@pitchmatch.ehi9k.mongodb.net/?retryWrites=true&w=majority&appName=pitchmatch")
        db = client["pitchmatch"]
        collection = db["startup_info"]

        collection.insert_one(startup_in_json)
        print(f"Successfully inserted data into collection 'pitchmatch.startup_info' in database 'pitchmatch'.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'client' in locals() and client:  # Ensure client is defined and not None
            client.close()

def read_startup(input_json):
    try:
        # 1. Establish a connection to MongoDB
        load_dotenv("mongo.env")
        username= os.getenv('MONGO_USERNAME')
        password= os.getenv('MONGO_PASSWORD')

        client = MongoClient(f"mongodb+srv://{username}:{password}@pitchmatch.ehi9k.mongodb.net/?retryWrites=true&w=majority&appName=pitchmatch")
        db = client["pitchmatch"]
        collection = db["startup_info"]

        # 2. Read data from MongoDB
        cursor = collection.find(input_json)
        for document in cursor:
            print(document)
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'client' in locals() and client:  # Ensure client is defined and not None
            client.close()


def read_vc(vc_json):
    try:
        # 1. Establish a connection to MongoDB
        load_dotenv("mongo.env")
        username = os.getenv('MONGO_USERNAME')
        password = os.getenv('MONGO_PASSWORD')

        client = MongoClient(f"mongodb+srv://{username}:{password}@pitchmatch.ehi9k.mongodb.net/?retryWrites=true&w=majority&appName=pitchmatch")
        db = client["pitchmatch"]
        collection = db["startup_info"]

        # 2. Read data from MongoDB
        cursor = collection.find(vc_json)
        for document in cursor:
            print(document)
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'client' in locals() and client:  # Ensure client is defined and not None
            client.close()

# --- Example Usage ---
if __name__ == "__main__":

    write_vc({
        "vc_name": "test_vc",
        "vc_email": "test@test.com"})

    write_startup({
        "startup_name": "test_startup",
        "startup_email": "test@startup.com"})

    read_vc({
        "vc_name": "test_vc"})

    read_startup({
        "startup_name": "test_startup"})