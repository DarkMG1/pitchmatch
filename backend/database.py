from pymongo import MongoClient

def connect_and_read_mongodb(connection_string, database_name, collection_name):
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
        client = MongoClient(connection_string)

        # 2. Access the specified database
        db = client[database_name]

        # 3. Access the specified collection
        collection = db[collection_name]

        # 4. Read data from the collection (example: find all documents)
        documents = collection.find()  # You can add query criteria here if needed (e.g., collection.find({"name": "John"}))

        # 5. Process and print the retrieved documents
        for document in documents:
            print(document)  # Print each document (you can customize this)

        print(f"Successfully read data from collection '{collection_name}' in database '{database_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'client' in locals() and client:  # Ensure client is defined and not None
            client.close()  # Close the connection in the finally block to ensure it always closes



# --- Example Usage ---
if __name__ == "__main__":
    # *** IMPORTANT: Replace with your actual MongoDB connection string, database, and collection names ***
    connection_string = "mongodb://your_username:your_password@your_host:your_port/"  # Example, replace with your credentials
    database_name = "your_database_name"
    collection_name = "your_collection_name"

    connect_and_read_mongodb(connection_string, database_name, collection_name)


    # Example 2: Using a connection string with SRV record (for MongoDB Atlas)
    # connection_string = "mongodb+srv://your_username:your_password@your_cluster_name.mongodb.net/?retryWrites=true&w=majority"
    # database_name = "your_database_name"
    # collection_name = "your_collection_name"

    # connect_and_read_mongodb(connection_string, database_name, collection_name)