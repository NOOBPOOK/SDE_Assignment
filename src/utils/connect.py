# Code for connecting the database to the application

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values


class Connect:
    def __init__(self):
        self.config = dotenv_values(r".env")
        self.endpoint = self.config.get("MONGO_ENDPOINT")
        self.default_db = self.config.get("MONGO_DEFAULT_DB")
        self.DB = None

        client = MongoClient(self.endpoint, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        print("Connecting to MongoDB...")
        try:
            client.admin.command('ping')
            self.DB = client.get_default_database(self.default_db)

        except Exception as e:
            print("Connection Failed.")
            print(e)

