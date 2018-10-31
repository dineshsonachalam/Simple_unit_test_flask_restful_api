from pymongo import MongoClient
from bson.json_util import dumps
from flask import jsonify
# Here dumps used to convert the pymongo cursor to json.

class crud_operation:

    def __init__(self):
        self.collection = 'users'
        self.database = 'user_management'
        self.client = MongoClient('mongodb://localhost:27017/'+ str(self.database))



    # Register new users.
    def register_users(self, username, password):
        # Check if users already exits in the database
        if( (self.client[self.database][self.collection].find({"username":username})).count() )>0:
            return {"message":"Username already exists"},400
        else:
            self.client[self.database][self.collection].insert_one(
                {
                    "username":username,
                    "password":password

                })
            return {"message":"Your account has been registered. Please login to continue."},200


    # Login
    def login_users(self,username,password):
        if((self.client[self.database][self.collection].find({"username":username})).count() >0):
            if ((self.client[self.database][self.collection].find({"username": username,"password":password})).count() > 0):
                return {"message":"User has been logged successfully!"},200
            else:
                return {"message":"Password is incorrect"},400
        else:
            return {"message":"Username doesnt exist"},400







    # # read specific tasks
    # def read(self,task_name):
    #     return dumps( self.client[self.database][self.collection].find({"task_name": task_name}))
    #
    # # update specific tasks
    # def update(self,task_name,new_task_name,new_status):
    #     myquery = {"task_name": task_name}
    #     newvalues ={"$set":{"task_name": new_task_name,"status":new_status}}
    #     #print("myquery: ",myquery)
    #     #print("newvalues: ",newvalues)
    #     #self.client[self.database][self.collection].update_one(myquery,newvalues)
    #     self.client[self.database][self.collection].update_one({"task_name": "Rock"},{ "$set": { "task_name": "johnson" }})
    #     return dumps(self.client[self.database][self.collection].find())
    #
    # # delete specific taskname records
    # def delete(self,task_name):
    #     myquery = {"task_name": task_name}
    #     self.client[self.database][self.collection].delete_one(myquery)
    #     return "Records deleted successfully!"
    #
    # # delete all the task documents
    # def delete_all(self):
    #     no_of_documents = self.client[self.database][self.collection].delete_many({})
    #     print("No of documents deleted: ",no_of_documents)
    #     return str(no_of_documents)+" documents deleted."