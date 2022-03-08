import sqlite3

# Connection
connection = sqlite3.connect('food_storage.db')

cursor = connection.cursor()


##### This is how I created the food_storage Table ######

# create food table
#cursor.execute("""CREATE TABLE food_storage (
#    name text,
#    vendor text,
#    purchased text,
#    expires text,
#    serving_per_container text,
#    quantity int
#)""")




#gameloop
quit = False
while quit == False:

    #Initial Questions
    print("\nFood Storage tracker.\n")
    print("What do you wish to do?")
    print(" 1: DISPLAY items in food storage.")
    print(" 2: ADD item to food storage.")
    print(" 3: UPDATE item in food storage.")
    print(" 4: DELETE item in food storage.")
    print(" 5: QUIT")
    choice = input("Please enter number and ENTER: ")
    print()

    # The QUIT choice
    if choice == "5":
        print("You Chose to QUIT")
        quit = True
        break

    # Display the contents of database
    elif choice == "1":
        viewDB = cursor.execute("SELECT * FROM food_storage")
        print("Currently in the database.")
        for x in viewDB:
            print(x)

    # Adds a document to the Database
    elif choice == "2":
        name = input("Please enter name of item to add: ")
        vendor = input("Please enter name of vendor where item was purchased: ")
        purchased = input("Please enter date of purchase, mm/dd/yyyy:  ")
        expires = input("Please enter expiration date, mm/dd/yyyy:  ")
        serving_per_container = input("Please enter servings per container: ")
        quantity = input("Please enter quantity of items purchased: ")
        cursor.execute(f"INSERT INTO food_storage VALUES ('{name}', '{vendor}', '{purchased}', '{expires}', '{serving_per_container}', '{quantity}' )")
        connection.commit()
        print("Updating Database...")

     # Updates contents of Database
    elif choice == "3":
        print("How do you want to find your info, by ")
        print("1: Name of Item.")
        print("2: Name of Vendor.")
        result = input("Type either 1 or 2 then ENTER: ")
        print()
        findBy = ""
        if result == "1":
            findBy = "name"
            name = input("Enter Item Name then hit Enter: ")
        elif result == "2":
            findBy = "vendor"
            name = input("Enter Name of vendor then hit Enter: ")
        updateDB = cursor.execute(f"SELECT * FROM food_storage WHERE {findBy}='{name}' ")
        for x in updateDB:
            print(x)
        print()
        print("\nWhat do you want to update?")
        print("\t1: Item Name")
        print("\t2: Vendor Name")
        print("\t3: Date of Purchase")
        print("\t4: Date of Expiration")
        print("\t5: Number of Servings per container")
        print("\t6: Quantity of Item")
        print()
        updateInput = input("Type 1/2/3/4/5/6 then hit ENTER: ")
        if updateInput == "1":
            updateData = "name"
            updateBy = "name"
        elif updateInput == "2":
            updateData = "vendor"
            updateBy = "vendor"
        elif updateInput == "3":
            updateData = "purchased date"
            updateBy = "purchased"
        elif updateInput == "4":
            updateData = "expiry date"
            updateBy = "expires"
        elif updateInput == "5":
            updateData = "servings per container"
            updateBy = "servings_per_container"
        elif updateInput == "6":
            updateData = "quantity"
            updateBy = "quantity"
        update = input(f"Please enter your new {updateData} then hit ENTER: ")
        cursor.execute(f"UPDATE food_storage SET {updateBy}='{update}' WHERE {findBy}='{name}'")
        connection.commit()
        print("Updating DB")


    # Deletes a document in Database
    elif choice == "4":
        viewDB = cursor.execute("SELECT * FROM food_storage")
        print("Currently in the database.")
        for x in viewDB:
            print(x)
        print("Which do you want to delete?")
        deleteInput = input("Type name of Item that you wish to delete then ENTER: ")
        print()
        print("Are you sure you want to delete:")
        
        print()
        answer = input("Please type y or n then hit ENTER: ")
        if answer == "y" or answer == "Y":
            cursor.execute(f"DELETE from food_storage WHERE name = '{deleteInput}'")
            print("Deleted\n")
            print("Updating DB")
        else:
            print("Not Deleted\n")  
        
        connection.commit()
        



    print("Do you wish to continue?")
    exitChoice = input("Type y to continue or type n or q to quit then ENTER: ")
    if exitChoice == "y" or exitChoice == "Y":
        quit = False
    elif exitChoice == "q" or exitChoice == "Q" or exitChoice == "n" or exitChoice == "N":
        quit = True
        break
 