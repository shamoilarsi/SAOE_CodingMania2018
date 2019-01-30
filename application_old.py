from flask import Flask, render_template, request, jsonify
import sqlite3
import random
import enum
from array import *
import datetime
import time

# class city(enum.Enum):
#     pune = 0
#     mumbai = 1
#     nasik = 2
#     jaipur = 3
#     delhi = 4
#     lucknow = 5
#
#
# # pune,mumbai,nasik,jaipur,delhi,lucknow
# a = [[99, 1, 2, 3, 5, 5],
#      [1, 99, 1, 3, 5, 6],
#      [2, 1, 99, 4, 5, 6],
#      [3, 3, 4, 99, 1, 2],
#      [5, 5, 5, 1, 99, 2],
#      [5, 6, 6, 2, 2, 99]]

db = sqlite3.connect("database.db")
cb = db.cursor()
try:

    db.execute(
        '''CREATE TABLE IF NOT EXISTS BloodBank
        (id INTEGER PRIMARY KEY,
        campname TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        phone TEXT NOT NULL,
        location TEXT NOT NULL,
        city TEXT NOT NULL,
        sques TEXT NOT NULL,
        sans TEXT NOT NULL,
        Apos INTEGER ,
        Ang INTEGER ,
        Bpos INTEGER ,
        Bng INTEGER ,
        ABpos INTEGER ,
        ABng INTEGER  ,
        Opos INTEGER  ,
        Ong INTEGER  ); ''')

    db.execute(
        '''CREATE TABLE IF NOT EXISTS Hospital
        (id INTEGER PRIMARY KEY,
        hospitalname TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        phone TEXT NOT NULL,
        location TEXT NOT NULL,
        city TEXT NOT NULL,
        sques TEXT NOT NULL,
        sans TEXT NOT NULL,
        Apos INTEGER ,
        Ang INTEGER ,
        Bpos INTEGER ,
        Bng INTEGER ,
        ABpos INTEGER ,
        ABng INTEGER  ,
        Opos INTEGER  ,
        Ong INTEGER  ); ''')

    db.execute(
        '''CREATE TABLE IF NOT EXISTS Personal
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        phone TEXT NOT NULL,
        location TEXT NOT NULL,
        city TEXT NOT NULL,
        sques TEXT NOT NULL,
        sans TEXT NOT NULL,
        bloodgroup INTEGER ); ''')
    db.commit()

except Exception as e:
    print("Database Already Exists : ", e)

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


@app.route("/", methods=['post', 'get'])
def index():
    db = sqlite3.connect("database.db")
    cb = db.cursor()

    cb.execute(
        """INSERT INTO Personal (name, username, email, password, phone, location, city, sques, sans, bloodgroup) VALUES("AAyush", "dsg", "sf", "sf", "sf", "sf", "sf", "sf", "sf", "zfjnk")""")
    db.commit()
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
    db = sqlite3.connect("database.db")
    cb = db.cursor()

    num = 1

    uname = request.form['uname']
    password = request.form['password']
    # print(uname, password)
    cb.execute('''SELECT * FROM BloodBank WHERE campname = "''' + uname + '''"''')
    string = cb.fetchall()
    num = 1
    print("0")
    if (string == "[]"):
        print("1")
        cb.execute('''SELECT * FROM Hospital WHERE hospitalname = "''' + uname + '''"''')
        string = cb.fetchall()
        num = 2

        if (string == "[]"):
            print("2")
            cb.execute('''SELECT * FROM Personal WHERE username = "''' + uname + '''"''')
            string = cb.fetchall()
            num = 3
            if (string == "[]"):
                num = 4

    print(string)
    print(num)

    if (num != 4):
        if (num == 1):
            cb.execute('''SELECT password FROM BloodBank WHERE campname = "''' + uname + '''"''')
            string = cb.fetchall()
            if password == (string):
                return jsonify(status=True, value=num)
        elif (num == 2):
            cb.execute('''SELECT password FROM Hospital WHERE hospitalname = "''' + uname + '''"''')
            string = cb.fetchall()
            if password == (string):
                return jsonify(status=True, value=num)
        elif (num == 3):
            cb.execute('''SELECT password FROM Personal WHERE username = "''' + uname + '''"''')
            string = cb.fetchall()
            if password == (string):
                return jsonify(status=True, value=num)
    print(string)
    return jsonify(status=False)


@app.route("/bbsignup", methods=['post', 'get'])
def bbsignup():
    db = sqlite3.connect("database.db")
    cb = db.cursor()

    hn = request.form['bloodBank_campName']
    em = request.form['bloodBank_campEmail']
    ct = request.form['bloodBank_city']
    l = request.form['bloodBank_location']
    ans = request.form['bloodBank_seqAns']
    p = request.form['bloodBank_contact']
    passwd = request.form['bloodBank_password']
    ques = request.form['bloodBank_seqQues']

    cb.execute(
        '''INSERT INTO BloodBank (campname, email, password, phone, location, city, sques, sans) VALUES("''' + hn + '''","''' + em + '''","''' + encode(
            passwd,
            hn) + '''","''' + p + '''","''' + l + '''","''' + ct + '''","''' + ques + '''","''' + ans + '''");''')
    db.commit()

    return jsonify(status=True)


@app.route("/hpsignup", methods=['post', 'get'])
def hpsignup():
    db = sqlite3.connect("database.db")
    cb = db.cursor()

    n = str(request.form['hospital_name'])
    loc = str(request.form['hospital_location'])
    c = str(request.form['hospital_city'])
    con = str(request.form['hospital_contact'])
    em = str(request.form['hospital_Email'])
    passwd = str(request.form['hospital_password'])
    license = str(request.form['hospital_licence'])
    ques = str(request.form['hospital_seqQues'])
    ans = str(request.form['hospital_seqAns'])

    cb.execute(
        '''INSERT INTO Hospital (hospitalname, email, password, phone, location, city, sques, sans) VALUES("''' + n + '''","''' + em + '''","''' + encode(
            n,
            passwd) + '''","''' + con + '''","''' + loc + '''","''' + c + '''","''' + ques + '''","''' + ans + '''");''')
    db.commit()

    return jsonify(status=True)


@app.route("/ursignup", methods=['post', 'get'])
def ursignup():
    n = str(request.form['person_name'])
    un = str(request.form['person_username'])
    em = str(request.form['person_Email'])
    p = str(request.form['person_phone'])
    loc = str(request.form['person_location'])
    c = str(request.form['person_city'])
    passwd = str(request.form['person_Password'])
    sques = str(request.form['person_SeqQues'])
    ans = str(request.form['person_SeqAns'])
    bgroup = str(request.form['person_bloodgroup'])

    db = sqlite3.connect("database.db")
    cb = db.cursor()

    cb.execute(
        '''INSERT INTO Personal (name, username, email, password, phone, location, city, sques, sans, bloodgroup) VALUES("''' + n + '''","''' + un + '''","''' + em + '''","''' + encode(
            n,
            passwd) + '''","''' + p + '''","''' + loc + '''","''' + c + '''","''' + sques + '''","''' + ans + '''","''' + bgroup + '''");''')
    db.commit()

    return jsonify(status=True)


@app.route("/search", methods=['post', 'get'])
def searchp():
    print('here')
    db = sqlite3.connect("database.db")
    cb = db.cursor()
    search = request.form['search']
    print(search)
    check = db.execute('''Select * from BloodBank where city="''' + search + '''"''')
    n = search
    if len(check.fetchall()) == 0:
        if search == 'pune':
            print("k")
            x = a[0].index(min(a[0]))
            print(x)
            n = city(x).name
            print(n)
        elif search == 'mumbai':
            print("k")
            x = a[1].index(min(a[1]))
            print(x)
            n = city(x).name
            print(n)
        elif search == 'nasik':
            print("k")
            x = a[2].index(min(a[2]))
            print(x)
            n = city(x).name
            print(n)
        elif search == 'jaipur':
            print("k")
            x = a[3].index(min(a[3]))
            print(x)
            n = city(x).name
            print(n)
        elif search == 'delhi':
            print("k")
            x = a[4].index(min(a[4]))
            print(x)
            n = city(x).name
            print(n)
        elif search == 'lucknow':
            print("k")
            x = a[5].index(min(a[5]))
            print(x)
            n = city(x).name
            print(n)
        else:
            n = 'mumbai'

    print(n)
    lis = db.execute(
        '''Select * from BloodBank  where username="''' + search + '''"or city="''' + search + '''" or location="''' + search + '''" or city="''' + n + '''"''')
    d = lis.fetchall()

    lis1 = db.execute(
        '''Select * from Hospital  where username="''' + search + '''"or city="''' + search + '''" or location="''' + search + '''" or city="''' + n + '''"''')
    d1 = lis1.fetchall()
    print(d1)
    lis2 = db.execute(
        '''Select * from Personal  where username="''' + search + '''"or city="''' + search + '''" or location="''' + search + '''" or city="''' + n + '''"''')
    d2 = lis2.fetchall()
    d = d + d1 + d2

    search = search.replace('+', 'pos')
    search = search.replace('-', 'ng')
    print(search)
    cb = db.cursor()
    l = cb.execute('''Select * from BloodBank where Apos>0 ''')
    l1 = l.fetchall()
    print(l1)
    return render_template("search.html", data=d)


@app.route("/searchQuery", methods=['post', 'get'])
def searchQuery():
    db = sqlite3.connect("database.db")
    cb = db.cursor()
    search = request.form['search']
    lis = db.execute(
        '''Select * from BloodBank  where username="''' + search + '''"or city="''' + search + '''" or location="''' + search + '''"''')
    items = lis.fetchall()

    return jsonify(status=True, data=items)


app.run(port='8080', debug=True)
