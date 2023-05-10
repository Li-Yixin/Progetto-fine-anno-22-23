from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="SOLAR_SYSTEM"
)
mycursor = mydb.cursor()

app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/S')
def sito():
    mycursor.execute("SELECT * FROM System_Element")
    myresult = mycursor.fetchall()
    return render_template('System_Element.html', units=myresult)