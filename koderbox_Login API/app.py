from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(_name_)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'authentication'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    email = request.form['email']
    password = request.form['password']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (first_name, last_name, gender, email, password) VALUES (%s, %s, %s, %s, %s)",
                (first_name, last_name, gender, email, password))
    mysql.connection.commit()
    cur.close()
    
    return "Registration successful!"

if _name_ == '_main_':
    app.run(debug=True)