from pymongo import MongoClient
from bson import ObjectId
import time
class Database:
    def __init__(self):
        self.url = "mongodb://localhost:27017"
        self.client = None
        self.cursor = None
        self.connectToDatabase()

    def connectToDatabase(self):
        try:
            self.client = MongoClient(self.url)
            self.cursor = self.client.project.users 
        except Exception as e:
            print("Database Not Connected - ",e)
    def addUser(self,useradd):
        try:
            self.cursor.insert_one(useradd)
            return "Added to database"
        except Exception as e:
            return( "Not Added To The Database",e)
    def getAllUser(self):
        try:
            return self.cursor.find({})
        except Exception as e:
            return("Not Able To Get USERs",e)
    def getUserByID(self,Id):
        try:
            return self.cursor.find_one({"_id": ObjectId(Id)})
        except Exception as e:
            return("Not Able To Get USER ",e)
    def updateById(self,Id,data):
        try:
            a = self.cursor.find_one_and_update({"_id": ObjectId(Id)},  
            {"$set": data},  
            return_document=True )
            return a 
        except Exception as e:
            return("Not Able To Update ",e)
    def deleteUserById(self,Id):
        try:
            a = self.cursor.find_one_and_delete({"_id": ObjectId(Id)})
            return "Entry Deleted"
        except Exception as e:
            return("Not Able To Delete ",e)
# 67c09d7e37ed4ca2f8ab0912



a = Database()
time.sleep(1)
# a.getUserByID("Ki")