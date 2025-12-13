import mysql.connector

# DATABASE CONNECTION
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="69Bobo69?",      # <--- Replace with your MySQL password
        database="restaurant_db"
    )