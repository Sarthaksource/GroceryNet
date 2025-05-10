import mysql.connector
import os

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
            host=os.environ.get("MYSQLHOST"),
            port=os.environ.get("MYSQLPORT", 3306),
            database=os.environ.get("MYSQLDATABASE"),
            user=os.environ.get("MYSQLUSER"),
            password=os.environ.get("MYSQLPASSWORD")
        )
    return __cnx