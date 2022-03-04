import sqlite3

# Connection
connection = sqlite3.connect('food_storage.db')

cursor = connection.cursor()

# create food table
#cursor.execute("""CREATE TABLE food_storage (
#    name text,
#    vendor text,
#    purchased text,
#    expires text,
#    serving_per_container text,
#    quantity int

#)""")

# create item in database
#cursor.execute("INSERT INTO food_storage VALUES ('Whole Wheat', 'Distribution Center', '1/15/2017', '4/1/2026', '200', '8' )")
#cursor.execute("INSERT INTO food_storage VALUES ('Potato Gems', 'Walmart', '2/3/2019', '4/1/2026', '200', '8' )")

# Query DB with Select
cursor.execute("SELECT * FROM food_storage")

print(cursor.fetchmany(5))   # or cursor.fetchmany()  or cursor.fetchall()

connection.commit()

connection.close()

