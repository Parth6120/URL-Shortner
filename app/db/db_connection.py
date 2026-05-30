import os
import logging

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Select the database (using an env variable or default to 'url_shortener')
db_name = os.getenv("MONGODB_DB_NAME", "url_shortener")
db = client[db_name]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    logger.info("Pinged your deployment. You successfully connected to MongoDB!")
    print("Connection successfull")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
    raise e