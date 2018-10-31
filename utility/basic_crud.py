from pymongo import MongoClient
from bson.json_util import dumps
from flask import jsonify
# Here dumps used to convert the pymongo cursor to json.

class basic_crud_operations:

    def __init__(self,collection,database):
        self.collection = collection
        self.database = database
        self.client = MongoClient('mongodb://localhost:27017/'+ str(self.database))



    # Insert new record
    # json_data = {}
    def create(self,json_data):
        if((self.client[self.database][self.collection].insert_one(json_data)).count() >0 ):
            return {"message":"New records created successfully."},200

    # Read all data.
    def read(self,json_data):
        return self.client[self.database][self.collection].find(json_data)


    def update(self,my_query,new_values):
        self.client[self.database][self.collection].update_one(my_query,new_values)
        return {"message":"Records updated successfully."}

    def delete(self,json_data):
        self.client[self.database][self.collection].delete_one(json_data)
        return {"message":"Record deleted successfully. "}

    def delete_all(self):
        no_of_documents_deleted = self.client[self.database][self.collection].delete_many({})
        return {"message":str(no_of_documents_deleted)+" documents deleted!"}
