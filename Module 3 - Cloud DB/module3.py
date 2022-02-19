from random import randint
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
    print()
    if choice == "5":
        print("You Chose to QUIT")
        quit = True
        break
    elif choice == "1":
        viewDB = collection.find({})
        print("Currently in MongoDB.")
        for x in viewDB:
            print(x)
        print()
    elif choice == "2":
        id = randint(1,3000)
        name = input("Please enter Player Name then hit ENTER: ")
        character = input("Please enter Character Name then hit ENTER: ")
        race = input("Please enter Character Race then hit ENTER: ")
        post = {"_id": id, "name": name, "Character": character, "Character Race": race}
        collection.insert_one(post)
        print("Updating MongoDB...")
    elif choice == "3":
        print("How do you want to find your info, by ")
        print("1: Player Name")
        print("2: Character Name")
        result = input("Type either 1 or 2 then ENTER: ")
        print()
        findBy = ""
        if result == "1":
            findBy = "name"
            name = input("Enter Player Name then hit Enter: ")
        elif result == "2":
            findBy = "Character"
            name = input("Enter Character Name then hit Enter: ")
        findInDB = collection.find({findBy: name})
        for result in findInDB:
            print(result)
        print()
        updateId = input("To confirm your choice please enter the id number then hit ENTER: ")
        numId = int(updateId)
        print("\nWhat do you want to update?")
        print("\t1: Player Name")
        print("\t2: Character Name")
        print("\t3: Character Race")
        updateInput = input("Type 1/2/3 then hit ENTER: ")
        if updateInput == "1":
            updateData = "name"
        elif updateInput == "2":
            updateData = "Character"
        elif updateInput == "3":
            updateData = "Character Race"
        update = input(f"Please enter your {updateData} then hit ENTER: ")
        results = collection.update_one({"_id": numId}, {"$set":{updateData: update}})
        print("Updating DB")
        findInDB = collection.find({findBy: name})
        for result2 in findInDB:
            print(result2)
    elif choice == "4":
        viewDB = collection.find({})
        print("Currently in MongoDB.")
        for x in viewDB:
            print(x)
        print("Which do you want to delete?")
        deleteId = input("Enter the Id number of the one you want to delete then hit ENTER: ")
        print()
        print("Are you sure you want to delete:")
        delId = int(deleteId)
        resultsDel = collection.find_one({"_id": delId})
        print(resultsDel)
        print()
        #for result in resultsDel:
        #    print(result)
        answer = input("Please type y or n then hit ENTER: ")
        if answer == "y" or answer == "Y":
            resultsDel = collection.delete_one({"_id": delId})
            print("Deleted\n")
        else:
            print("Not Deleted\n")




      


    #post = {"_id": 1, "name": "Erik", "age": 41}
    #post1 = {"_id": 3, "name": "Erik", "Character": "Montague", "Character Race": "Half-Elf"}
    #post2 = {"_id": 4, "name": "Quentin", "Character": "Darvek", "Character Race": "Dwarf"}

    

    #collection.insert_one(post)
    #collection.insert_many([post1, post2])
    #results = collection.find({"Character": "Darvek"})
    #results = collection.find_one({"_id":0})

    #results = collection.delete_one({"_id":1})
    #results = collection.find({})
    #results = collection.update_one({"_id":0}, {"$set":{"hobby": "Dungeons and Dragons"}})


    #for result in results:
    #    print(result["name"]) 


    

    print("Do you wish to continue?")
    exitChoice = input("Type y to continue or type n or q to quit then ENTER: ")
    if exitChoice == "y" or exitChoice == "Y":
        quit = False
    elif exitChoice == "q" or exitChoice == "Q" or exitChoice == "n" or exitChoice == "N":
        quit = True
        break