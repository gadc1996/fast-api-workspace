import os
from pymongo import MongoClient
from pymongo.write_concern import WriteConcern
from typing import Optional, TypedDict
from bson.objectid import ObjectId

class MongoDb:
    class Document(TypedDict):
        id: str

    _uri = "mongodb+srv://%s:%s@%s" % (
        os.getenv("MONGO_USERNAME"),
        os.getenv("MONGO_PASSWORD"),
        os.getenv("MONGO_HOST"),
    )

    @classmethod
    def _db(cls):
        """
        This method establishes a connection to the MongoDB server and returns the specified MongoDB collection.

        It uses the MongoDB connection URI (_uri) class variable, which is constructed using environment variables 
        for the MongoDB username, password, and host. It then connects to the MongoDB server using the MongoClient 
        class from the pymongo library, and accesses the specified MongoDB collection, which is also provided as an 
        environment variable.

        Returns:
            Collection: The specified MongoDB collection.
        """
        return MongoClient(cls._uri)[os.getenv("MONGO_DATABASE")]

    @classmethod
    def ping(cls) -> bool:
        """
        This method checks the connection to the MongoDB server.

        It sends a "ping" command to the MongoDB server. If the server is reachable and responds successfully, 
        the method returns True, indicating that the connection is active. If the server is not reachable or 
        does not respond successfully (for example, due to network issues), an exception is raised, 
        and the method returns False, indicating that the connection is not active.

        Returns:
            bool: True if the MongoDB server is reachable and responds successfully, False otherwise.
        """
        try:
            cls._db().command("ping")
            return True
        except Exception:
            return False

    @classmethod
    def insert(cls, collection: str, data: dict) -> Optional[Document]:
        """
        Insert a new document into a collection in the database.

        This method is a class method, meaning it's bound to the class and not the instance of the class.
        It can be called on the class itself, not just an instance of the class.

        Parameters:
        collection (str): The name of the collection to insert the document into.
        data (dict): The data to be inserted into the collection. This should be a dictionary where the keys are the field names and the values are the field values.

        Returns:
        Optional[str]: The ID of the inserted document as a string, if the insert operation was acknowledged by the database. If the insert operation was not acknowledged, it returns None.
        """
        result = cls._db()[collection].insert_one(data)

        if not result.acknowledged:
            return None
        
        return cls.find(collection=collection, _id=str(result.inserted_id))

    @classmethod
    def find(
        cls,
        collection: str,
        _id: Optional[str] = None,
        query: Optional[dict] = None,
    ) -> Optional[Document]:
        """
        Find a document in a collection in the database.

        This method is a class method, meaning it's bound to the class and not the instance of the class.
        It can be called on the class itself, not just an instance of the class.

        Parameters:
        collection (str): The name of the collection to find the document from.
        _id (Optional[str]): The ID of the document to find. If this is provided, the method will ignore the query parameter.
        query (Optional[dict]): A query to find the document. This should be a dictionary where the keys are the field names and the values are the field values to match.

        Returns:
        Optional[dict]: The found document as a dictionary, if a document matching the ID or query was found. The dictionary keys are the field names and the values are the field values. If no document was found, it returns None.
        """
        if _id is not None:
            query = {"_id": ObjectId(_id)}

        result = cls._db()[collection].find_one(query)

        if not result:
            return None
        
        result["id"] = str(result.pop("_id"))

        return result

    @classmethod
    def update(cls, collection: str, new_values: dict, query: Optional[dict] = None, _id: Optional[str] = None) -> Optional[Document]:
        """
        Update a document in a collection in the database.
        
        This method is a class method, meaning it's bound to the class and not the instance of the class.
        It can be called on the class itself, not just an instance of the class.
        
        Parameters:
        collection (str): The name of the collection to update the document in.
        new_values (dict): The new values to update the document with. This should be a dictionary where the keys are the field names and the values are the new field values.
        query (Optional[dict]): A query to find the document to update. This should be a dictionary where the keys are the field names and the values are the field values to match.
        _id (Optional[str]): The ID of the document to update. If this is provided, the method will ignore the query parameter.
        
        Returns:
        Optional[dict]: The updated document as a dictionary, if the update operation was acknowledged by the database. The dictionary keys are the field names and the values are the field values. If the update operation was not acknowledged, it returns None.
        """
        if _id is not None:
            query = {"_id": ObjectId(_id)}
            
        result = cls._db()[collection].update_one(query, {"$set": new_values})
        
        if result.modified_count == 0:
            return None
        
        return cls.find(collection=collection, _id=_id)

    @classmethod
    def delete(cls, collection: str, _id: Optional[str] = None, query: Optional[dict] = None) -> bool:
        """
        Delete a document from a collection in the database.

        This method is a class method, meaning it's bound to the class and not the instance of the class.
        It can be called on the class itself, not just an instance of the class.

        Parameters:
        collection (str): The name of the collection to delete the document from.
        _id (Optional[str]): The ID of the document to delete. If this is provided, the method will ignore the query parameter.
        query (Optional[dict]): A query to find the document to delete. This should be a dictionary where the keys are the field names and the values are the field values to match.

        Returns:
        bool: True if the document was successfully deleted, False otherwise.
        """
        if _id is not None:
            query = {"_id": ObjectId(_id)}

        document = cls._db()[collection].delete_one(query)
        return document.deleted_count > 0
    
    @classmethod
    def delete_all(cls, collection: str) -> bool:
        """
        Delete all documents from a collection in the database.

        This method is a class method, meaning it's bound to the class and not the instance of the class.
        It can be called on the class itself, not just an instance of the class.
        
        Parameters:
        collection (str): The name of the collection to delete all documents from.
        
        Returns:
        bool: True if all documents were successfully deleted, False otherwise.
        """
        c = cls._db()[collection]
        c.delete_many({})
        return c.count_documents({}) == 0
