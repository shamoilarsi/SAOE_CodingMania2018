from flask import Flask, render_template, request, jsonify
import sqlite3
import random


try:
    db = sqlite3.connect("database.db")
    cb = db.cursor()

    db.execute(
        '''CREATE TABLE IF NOT EXISTS BloodBank(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        phone TEXT NOT NULL,
        location TEXT NOT NULL,
        city TEXT NOT NULL,
        securityQuestion TEXT NOT NULL,
        securityAnswer TEXT NOT NULL,
        Apositive INTEGER DEFAULT 0,
        Anegetive INTEGER DEFAULT 0,
        Bpositive INTEGER DEFAULT 0,
        Bnegetive INTEGER DEFAULT 0,
        ABpositive INTEGER DEFAULT 0,
        ABnegetive INTEGER  DEFAULT 0,
        Opositive INTEGER  DEFAULT 0,
        Onegetive INTEGER  DEFAULT 0
        ); ''')

    db.execute(
        '''CREATE TABLE IF NOT EXISTS Hospital(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        phone TEXT NOT NULL,
        location TEXT NOT NULL,
        city TEXT NOT NULL,
        license TEXT NOT NULL,
        securityQuestion TEXT NOT NULL,
        securityAnswer TEXT NOT NULL,
        Apositive INTEGER  DEFAULT 0,
        Anegetive INTEGER DEFAULT 0,
        Bpositive INTEGER DEFAULT 0,
        Bnegetive INTEGER DEFAULT 0,
        ABpositive INTEGER DEFAULT 0,
        ABnegetive INTEGER  DEFAULT 0,
        Opositive INTEGER  DEFAULT 0,
        Onegetive INTEGER  DEFAULT 0
        ); ''')

    db.execute(
        '''CREATE TABLE IF NOT EXISTS Personal(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        phone TEXT NOT NULL,
        location TEXT NOT NULL,
        city TEXT NOT NULL,
        securityQuestion TEXT NOT NULL,
        securityAnswer TEXT NOT NULL,
        bloodGroup INTEGER 
        ); ''')
    db.commit()

except Exception as e:
    print("Exception :", e)

app = Flask(__name__)


def encode(uname, password):
    n = random.randint(1, 1001)
    new = ""

    for i in range(0, len(password)):
        h = ord(password[i])
        new += chr(h + n)

    new = str(n + len(uname)) + "!" + new
    return new


def decode(uname, password):
    l = len(uname)
    q = (password.index('!'))
    s = int(password[2:q])
    s -= l
    password = password[q + 1:len(password) - 3]
    new = ""

    for i in range(0, len(password)):
        new += (chr(ord(password[i]) - s))
    return new


def insert_into_db(table, fields, data):
    query = f'''INSERT INTO 
    {table} ({fields})
    values 
    {data}'''

    db = sqlite3.connect("database.db")
    cb = db.cursor()
    cb.execute(query)
    db.commit()
    print("Inserted into table :", table)


def get_credentials_from_db(table, email):
    query = f"SELECT password FROM {table} WHERE email = '{email}'"
    db = sqlite3.connect("database.db")
    cb = db.cursor()
    cb.execute(query)
    rows = cb.fetchall()
    if len(rows) != 0:
        print("Password :", rows[0][0])
        return rows[0][0]
    else:
        return ""


def check_password(password, db_password):
    if password == db_password:
        return True
    else:
        return False


@app.route("/", methods=['post', 'get'])
def index():
    return render_template("homepage.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/About")
def About():
    return render_template("About.html")


@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/hospitalProfile")
def hospitalProfile():
    return render_template("hProfile.html")


@app.route("/personal")
def personal():
    return render_template("personal.html")


@app.route("/bloodBank")
def bloodbank():
    return render_template("bloodbank.html")


@app.route("/hospital")
def hospital():
    return render_template("hospital.html")


@app.route("/checkLogin", methods=['post', 'get'])
def checkLogin():
    email = str(request.form['email'])
    password = str(request.form['password'])

    if check_password(password, get_credentials_from_db("BloodBank", email)):
        print("BloodBank Login")
        return jsonify(status=True, value=1)
    elif check_password(password, get_credentials_from_db("Hospital", email)):
        print("Hospital Login")
        return jsonify(status=True, value=2)
    elif check_password(password, get_credentials_from_db("Personal", email)):
        print("Personal Login")
        return jsonify(status=True, value=3)
    else:
        return jsonify(status=False)


@app.route("/bbsignup", methods=['post', 'get'])
def bbsignup():
    name = request.form['bloodBank_campName']
    email = request.form['bloodBank_campEmail']
    password = request.form['bloodBank_password']
    phno = request.form['bloodBank_contact']
    location = request.form['bloodBank_location']
    city = request.form['bloodBank_city']
    security_question = request.form['bloodBank_seqQues']
    security_answer = request.form['bloodBank_seqAns']

    insert_into_db("BloodBank",
                   '''name, email, password, phone, location, city, securityQuestion, securityAnswer''',
                   (name, email, password, phno, location, city, security_question, security_answer))

    return jsonify(status=True)


@app.route("/hpsignup", methods=['post', 'get'])
def hpsignup():
    name = str(request.form['hospital_name'])
    email = str(request.form['hospital_Email'])
    password = str(request.form['hospital_password'])
    phno = str(request.form['hospital_contact'])
    location = str(request.form['hospital_location'])
    city = str(request.form['hospital_city'])
    license_number = str(request.form['hospital_licence'])
    security_question = str(request.form['hospital_seqQues'])
    security_answer = str(request.form['hospital_seqAns'])

    insert_into_db("Hospital",
                   '''name, email, password, phone, location, city, license, securityQuestion, securityAnswer''',
                   (name, email, password, phno, location, city, license_number, security_question, security_answer))

    return jsonify(status=True)


@app.route("/ursignup", methods=['post', 'get'])
def ursignup():
    name = str(request.form['person_name'])
    username = str(request.form['person_username'])
    email = str(request.form['person_Email'])
    phno = str(request.form['person_phone'])
    loc = str(request.form['person_location'])
    city = str(request.form['person_city'])
    password = str(request.form['person_Password'])
    security_question = str(request.form['person_SeqQues'])
    security_answer = str(request.form['person_SeqAns'])
    blood_group = str(request.form['person_bloodgroup'])

    insert_into_db("Personal",
                   '''name, username, email, password, phone, location, city, securityQuestion, securityAnswer, bloodGroup''',
                   (name, username, email, phno, loc, city, password, security_question, security_answer, blood_group))

    return jsonify(status=True)


@app.route("/search", methods=['post', 'get'])
def searchp():
    return render_template("search.html", data="")


@app.route("/searchQuery", methods=['post', 'get'])
def searchQuery():
    return jsonify(status=True, data="")


app.run(port='8080', debug=True)