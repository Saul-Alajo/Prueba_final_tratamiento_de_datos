
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import certifi
load_dotenv()
ca=certifi.where()

class MongoConnect:
    def __init__(self):
        user= os.getenv('MONGO_USER')
        password= os.getenv('MONGO_PASS')
        db_hostname = os.getenv('MONGO_HOST')

        uri = f"mongodb+srv://{user}:{password}@{db_hostname}/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(uri,tlsCAFile=ca)

# Send a ping to confirm a successful connection
    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    MongoConnect().test_connection()

MONGO_URI = 'mongodb+srv://user:password@cluster0.f5vxk.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db