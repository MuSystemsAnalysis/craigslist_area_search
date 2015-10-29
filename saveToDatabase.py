import sqlite3
import sys

def saveCityNamesToDatabase(cityList):
	database_file = 'test.db'

	#connect
	conn = sqlite3.connect(database_file)
	cursor = conn.cursor()


	#create table
	cursor.execute('DROP TABLE IF EXISTS cities')
	cursor.execute('''CREATE TABLE cities
	    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
	    NAME TEXT NOT NULL);''')
	print("Table created...\n")


	#insert
	for city in cityList:
	    format_str = """INSERT INTO cities (ID, NAME) VALUES (NULL, "{cityName}");"""
	    sql_command = format_str.format(cityName=city)
	    cursor.execute(sql_command)

	#view
	c = conn.execute("SELECT * FROM cities")
	for row in c:
	    print ("ID = ", row[0])
	    print ("NAME = ", row[1])


	#save and close the database
	conn.commit()
	conn.close()
