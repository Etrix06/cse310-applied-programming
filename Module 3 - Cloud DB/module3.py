import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO = os.getenv("MONGO")

cluster = MongoClient(f"{MONGO}")
db = cluster["python"]
collection = db["python"]

post = {"_id": 1, "name": "Erik", "age": 41}
post1 = {"_id": 3, "name": "Erik", "Character": "Montague", "Character Race": "Half-Elf"}
post2 = {"_id": 4, "name": "Quentin", "Character": "Darvek", "Character Race": "Dwarf"}

#collection.insert_one(post)
#collection.insert_many([post1, post2])
results = collection.find({"Character": "Darvek"})

for result in results:
    print(result) 
#print("Post created in MongoDB.")
