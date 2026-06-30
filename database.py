import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    autocommit=True
)
cursor = connection.cursor()
def user_save(email , password):
    cursor.execute("INSERT INTO users (email , password) VALUES(%s ,%s)", (email , password))
def check_email(email):
    cursor.execute("select email from users where email = %s ;",(email,))
    result = cursor.fetchone()
    if result :
        return 1 #email exists in the database
    else:
        return 0 
def check_password(email,password):
    cursor.execute("select password from users where email = %s and password = %s;",(email,password))
    result = cursor.fetchone()
    if result :
        return 1 
    else:
        return 0 


