# Example Python Code to Insert a Document 

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is None:
            raise Exception("Nothing to save, because data parameter is empty")

        # wrapped the insert in try/except like the other methods so a mongo error
        # prints a message and returns False instead of crashing. acknowledged comes
        # back True when the insert actually went through
        try:
            result = self.collection.insert_one(data)  # data must be a dictionary
            return result.acknowledged
        except PyMongoError as e:
            print(f"An error occurred while inserting the document: {e}")
            return False

    # Create method to implement the R in CRUD.
    def read(self, query, projection=None):
        """
        Queries for documents in the animals collection.
        :param query: A dictionary representing the key/value lookup pair.
        :return: A list of matching documents, or an empty list if none found.
        """
        if query is None:
            raise Exception("Query parameter is empty")

        # wrapped the find in try/except so a mongo error just prints a message and
        # returns an empty list instead of crashing the whole dashboard
        try:
            cursor = self.collection.find(query, projection)
            return list(cursor)
        except PyMongoError as e:
            print(f"An error occurred while reading documents: {e}")
            return []
            
    # Create method to implement the U in CRUD.
    def update(self, query, update_data):
        if query is None or update_data is None:
            raise Exception("Query or update parameter is empty")
        
        # same try/except idea here so an update error doesn't take everything down
        try:
            result = self.collection.update_many(query, update_data)
            return result.modified_count
        except PyMongoError as e:
            print(f"An error occurred while updating documents: {e}")
            return 0
            
    # Create method to implement the D in CRUD.
    def delete(self, query):
        if query is None:
            raise Exception("Query parameter is empty")
        
        # and the same here for delete
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"An error occurred while deleting documents: {e}")
            return 0