# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS SOLAR_SYSTEM")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS SOLAR_SYSTEM.System_Element (
    id INTEGER(50) NOT NULL,
    Planet VARCHAR(50) NOT NULL, 
    Color VARCHAR(100),
    Mass INTEGER,
    Diameter INTEGER,
    Density INTEGER,
    Surface_Gravity INTEGER,
    Escape_Velocity INTEGER,
    PRIMARY KEY (id)
  );""")


#Delete data from the table System_Element
mycursor.execute("DELETE FROM SOLAR_SYSTEM.System_Element")
mydb.commit()

#Read data from a csv file
system_date = pd.read_csv('./planets.csv', index_col=False, delimiter = ',')
system_date = system_date.fillna('Null')
print(system_date.head(20))

#Fill the table
for i,row in system_date.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO SOLAR_SYSTEM.System_Element VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM SOLAR_SYSTEM.System_Element")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)