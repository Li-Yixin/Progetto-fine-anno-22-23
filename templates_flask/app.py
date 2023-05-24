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
def home_page():
    return render_template('hello.html')

@app.route('/S')
def nomi():
    mycursor.execute("SELECT * FROM System_Element")
    myresult = mycursor.fetchall()
    return render_template('System_Element.html', units=myresult)


@app.route('/D')
def descrizine():
    
    return render_template('Descrizione.html')