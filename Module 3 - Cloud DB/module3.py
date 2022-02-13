import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO = os.getenv("MONGO")

cluster = MongoClient(f"{MONGO}")
db = cluster["python"]
collection = db["python"]

post = {"_id": 0, "name": "Erik", "age": 41}

collection.insert_one(post)

print("Post created in MongoDB.")
