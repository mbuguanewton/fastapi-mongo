from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb://localhost:27017/", port=27017, connect=False)
DB = client.get_database("fastapi")


# class Mongo:
#     """
#     mongo db methods
#     """

#     def __init__(self, collection):
#         self.db = DB.get_collection(collection)

#     def create(self, data):
#         try:
#             new = self.db.insert_one({**data})
#             doc_id = new.inserted_id

#             todo = self.db.find_one({"_id": ObjectId(doc_id)})
#             return todo
#         except Exception as error:
#             return {"error": f"Somthing went wrong: {error}"}
