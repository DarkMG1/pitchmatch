from pymongo import MongoClient
import os
from dotenv import load_dotenv

def connect_and_read_mongodb():
    """
    Connects to a MongoDB database, reads data from a specified collection,
    and prints the retrieved documents.

    Args:
        connection_string: The connection string for the MongoDB server.
                           (e.g., "mongodb://username:password@host:port/")
        database_name: The name of the database to connect to.
        collection_name: The name of the collection to read from.

    Returns:
        None. Prints the retrieved documents to the console.  Or raises an exception if there is an error.
    """
    try:
        # 1. Establish a connection to MongoDB
        load_dotenv("mongo.env")
        username= os.getenv('MONGO_USERNAME')
        password= os.getenv('MONGO_PASSWORD')

        client = MongoClient(f"mongodb+srv://{username}:{password}@pitchmatch.ehi9k.mongodb.net/?retryWrites=true&w=majority&appName=pitchmatch")

        # 2. Access the specified database
        db = client["pitchmatch"]

        # 3. Access the specified collection
        collection = db["sample_mflix.movies"]

        # 4. Read data from the collection (example: find all documents)
        documents = collection.find()  # You can add query criteria here if needed (e.g., collection.find({"name": "John"}))
        lists = list(documents)
        print(documents)
        print(lists)
        # 5. Process and print the retrieved documents
        for document in documents:
            print(document)  # Print each document (you can customize this)

        print(f"Successfully read data from collection 'sample_mflix.comments' in database 'pitchmatch'.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'client' in locals() and client:  # Ensure client is defined and not None
            client.close()  # Close the connection in the finally block to ensure it always closes



# --- Example Usage ---
if __name__ == "__main__":

    connect_and_read_mongodb()


    # Example 2: Using a connection string with SRV record (for MongoDB Atlas)
    # connection_string = "mongodb+srv://your_username:your_password@your_cluster_name.mongodb.net/?retryWrites=true&w=majority"
    # database_name = "your_database_name"
    # collection_name = "your_collection_name"

    # connect_and_read_mongodb(connection_string, database_name, collection_name)