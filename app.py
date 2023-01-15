#Imports
import sqlite3
from flask import Flask, render_template, request, session, redirect
import pyrebase

#Setup
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index1():
        return render_template('index.html')

#Routes
@app.route('/loginPage.html')
def index2():
        return render_template('loginPage.html')

@app.route('/register.html')
def index3():
        return render_template('loginPage.html')

@app.route('/logout')
def logout():
        return render_template('index.html') 

config = {
    "apiKey": "AIzaSyAXFkvFb4dGvbedTeK92AMe0-tX7__J19w",
    "authDomain": "vlabs-4d54a.firebaseapp.com",
    "projectId": "vlabs-4d54a",
    "storageBucket": "vlabs-4d54a.appspot.com",
    "messagingSenderId": "773645748479",
    "appId": "1:773645748479:web:b11b5347cec6b6882864ca",
    "measurementId": "G-PJ4V7D84NC",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = "secret_invasion"


@app.route('/register.html', methods=["POST"])
def register():
  if request.method == 'POST':    

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirm password']
        try:
           user = auth.create_user_with_email_and_password(email, password)
        except:
           return 'Error 404'
        #   print(user)

        auth.send_email_verification(user['idToken'])
  return render_template('loginPage.html')

@app.route('/loginPage.html', methods=['GET','POST'])
def index():
        if (request.method == 'POST'):
            email = request.form['email']
            password = request.form['password']    
            try:
              user = auth.sign_in_with_email_and_password(email, password)
              session['user'] = email
            except:
              return 'Login Failed'
        return render_template('extc.html')
if __name__ == "__main__":
    app.run(debug = True) 