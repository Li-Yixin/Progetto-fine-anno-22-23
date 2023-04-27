from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/units')
def unitList():
    mycursor.execute("SELECT * FROM plane")
    
    return render_template('hello.html', name='Fabio')