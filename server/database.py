import os
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient


mongodb_url = os.getenv("DB_URL")


# Create a new client and connect to the server
CLIENT = MongoClient(mongodb_url, server_api=ServerApi('1'))


DB = CLIENT.get_database('employees_data')

# Collections
employees_collection = DB["employees"]
departments_collection = DB["departments"]


# Send a ping to confirm a successful connection
try:
    CLIENT.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
