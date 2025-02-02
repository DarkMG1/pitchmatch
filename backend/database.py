from pymongo import MongoClient
import os
from dotenv import load_dotenv
from backend import utils


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
        documents = list(cursor)
        return documents
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
        collection = db["vc_info"]

        # 2. Read data from MongoDB
        cursor = collection.find(vc_json)
        documents = list(cursor)
        return documents
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'client' in locals() and client:  # Ensure client is defined and not None
            client.close()

def write_login(login_json):
    try:
        # 1. Establish a connection to MongoDB
        load_dotenv("mongo.env")
        username= os.getenv('MONGO_USERNAME')
        password= os.getenv('MONGO_PASSWORD')

        client = MongoClient(f"mongodb+srv://{username}:{password}@pitchmatch.ehi9k.mongodb.net/?retryWrites=true&w=majority&appName=pitchmatch")
        db = client["pitchmatch"]
        collection = db["login_info"]

        collection.insert_one(login_json)
        print(f"Successfully inserted data into collection 'pitchmatch.login_info' in database 'pitchmatch'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'client' in locals() and client:
            client.close()

def read_login(login_json):
    try:
        # 1. Establish a connection to MongoDB
        load_dotenv("mongo.env")
        username= os.getenv('MONGO_USERNAME')
        password= os.getenv('MONGO_PASSWORD')

        client = MongoClient(f"mongodb+srv://{username}:{password}@pitchmatch.ehi9k.mongodb.net/?retryWrites=true&w=majority&appName=pitchmatch")
        db = client["pitchmatch"]
        collection = db["login_info"]

        cursor = collection.find(login_json)
        documents = list(cursor)
        return documents
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'client' in locals() and client:
            client.close()

# --- Example Usage ---
if __name__ == "__main__":

    write_login({
        "email": "test_login@gmail.com",
        "password": utils.hash_password("test_password")})

    write_vc({
        "vc_name": "test_vc",
        "vc_email": "test@test.com"})

    write_startup({
        "startup_name": "test_startup",
        "startup_email": "test@startup.com"})

    print(read_vc({
        "vc_name": "test_vc"}))

    print(read_startup({
        "startup_name": "test_startup"}))

    print(read_login({
        "email": "test_login"}))
