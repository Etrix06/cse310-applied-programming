import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Database connect
MONGO = os.getenv("MONGO")
cluster = MongoClient(f"{MONGO}")
db = cluster["python"]
collection = db["python"]

#gameloop
quit = False
while quit == False:

    #Initial Questions
    print("\nDungeons and Dragons Player and Character tracker.\n")
    print("What do you wish to do?")
    print(" 1: DISPLAY players and character")
    print(" 2: ADD a player or character")
    print(" 3: UPDATE a player or character")
    print(" 4: DELETE a character")
    print(" 5: QUIT")
    choice = input("Please enter number and ENTER: ")
    print("You chose ", choice)
    if choice == "5":
        print("You Chose to QUIT")
        quit = True
      


    post = {"_id": 1, "name": "Erik", "age": 41}
    post1 = {"_id": 3, "name": "Erik", "Character": "Montague", "Character Race": "Half-Elf"}
    post2 = {"_id": 4, "name": "Quentin", "Character": "Darvek", "Character Race": "Dwarf"}

    #collection.insert_one(post)
    #collection.insert_many([post1, post2])
    #results = collection.find({"Character": "Darvek"})
    #results = collection.find_one({"_id":0})

    #results = collection.delete_one({"_id":1})
    #results = collection.find({})
    results = collection.update_one({"_id":0}, {"$set":{"hobby": "Dungeons and Dragons"}})


    #for result in results:
    #    print(result["name"]) 


    viewDB = collection.find({})
    print("Currently in MongoDB.")
    for x in viewDB:
        print(x)