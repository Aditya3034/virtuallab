from flask import Flask,request,render_template
app = Flask(__name__)

def login():
    if request.method == 'POST':
        user=request.form['userName']
        password=request.form['userPassword']
        if user=='Aditya' and password =='000000':
            return render_template('Test.html', name=user)
        else:
            return 'login failed %s' %user
    else:
        user=request.args.get['userName'] 
        password=request.args.get['userPassword'] 
        if user=='Aditya' and password =='1234':
            return 'welcome %s' %user
        else:
            return 'login failed %s' %user
    


import sqlite3

connection =sqlite3.connect("user_data.db")
cursor = connection.cursor()

#Queries

command = """CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""

cursor.execute(command)

cursor.execute("INSERT INTO users VALUES ('Rishab','123456789')")
cursor.execute("INSERT INTO users VALUES ('Aditya3034@gmail.com','00000000')")
cursor.execute("INSERT INTO users VALUES ('Vedant','11111111')")

connection.commit()

if __name__=="__main__":
     app.run(debug=True)