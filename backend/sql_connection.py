import os
import mysql.connector

def get_sql_connection():
    print("MYSQLHOST:", os.environ.get("MYSQLHOST"))
    print("MYSQLUSER:", os.environ.get("MYSQLUSER"))
    print("MYSQLPASSWORD:", os.environ.get("MYSQLPASSWORD"))
    print("MYSQLDATABASE:", os.environ.get("MYSQLDATABASE"))
    print("MYSQLPORT:", os.environ.get("MYSQLPORT"))
    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT", 3306))
    )
