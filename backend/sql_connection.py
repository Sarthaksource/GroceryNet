import mysql.connector

__cnx = None

def get_sql_connection():
	global __cnx

	if __cnx is None:
		__cnx = mysql.connector.connect(
		    host="localhost",
		    database="grocery_store",
	    	user="root",
	    	password="root"
	    )
	return __cnx