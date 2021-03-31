import mysql.connector
from dotenv import load_dotenv
import os
#Credentials
load_dotenv('.env')

def connect():
    cnx = mysql.connector.connect(user=os.getenv('USERNAME'), password=os.getenv('PASSWORD'),host =os.getenv('HOST'),database=os.getenv('DATABASE'))
    curr = cnx.cursor()
    cnx.close()

def insert(title, author, year, isbn):
    cnx = mysql.connector.connect(user=os.getenv('USERNAME'), password=os.getenv('PASSWORD'),host =os.getenv('HOST'),database=os.getenv('DATABASE'))
    curr = cnx.cursor()
    curr.execute("INSERT INTO bookstore (title, author, year, isbn) VALUES (%s,%s,%s,%s)",(title, author, year, isbn))
    cnx.commit()
    cnx.close()
def view():
    cnx = mysql.connector.connect(user=os.getenv('USERNAME'), password=os.getenv('PASSWORD'),host =os.getenv('HOST'),database=os.getenv('DATABASE'))
    curr = cnx.cursor()
    curr.execute('SELECT * FROM bookstore ')
    rows= curr.fetchall()
    cnx.close()
    return rows
def search(title="", author="", year="", isbn=""):
    cnx = mysql.connector.connect(user=os.getenv('USERNAME'), password=os.getenv('PASSWORD'),host =os.getenv('HOST'),database=os.getenv('DATABASE'))
    curr = cnx.cursor()
    curr.execute("SELECT * FROM bookstore WHERE title=%s OR author=%s OR year=%s OR isbn=%s",(title, author, year, isbn))
    rows= curr.fetchall()
    cnx.close()
    return rows
def delete(id):
    cnx = mysql.connector.connect(user=os.getenv('USERNAME'), password=os.getenv('PASSWORD'),host =os.getenv('HOST'),database=os.getenv('DATABASE'))
    curr = cnx.cursor()
    curr.execute("DELETE FROM bookstore WHERE id=%s",(id,))
    cnx.commit()
    cnx.close()
def update(id, title, author, year, isbn):
    cnx = mysql.connector.connect(user=os.getenv('USERNAME'), password=os.getenv('PASSWORD'),host =os.getenv('HOST'),database=os.getenv('DATABASE'))
    curr = cnx.cursor()
    curr.execute("UPDATE bookstore SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",(title, author, year, isbn,id))
    cnx.commit()
    cnx.close()

connect()
