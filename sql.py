##creating table 
import sqlite3

#creating database 
with sqlite3.connect("blog.db") as connection:
	
	# get a cursor object
	c = connection.cursor()
	
	# Create the table
	c.execute("CREATE TABLE posts(title TEXT, post TEXT)")

	#insert dummy data
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")') 
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")') 
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")') 
	c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")') 