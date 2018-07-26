import MySQLdb
import hashlib
db = MySQLdb.connect('HOST_URL', 'DATABASE_USERNAME', 'DATABASE_PASSWORD', 'DATABASE_NAME')

cursor = db.cursor()

def signup():
    fname = input("Enter Your First Name: ")
    lname = input("Enter Your Last Name: ")
    age = int(input("Enter Your Age: "))
    gender = input("Enter Your Gender(M/F): ")
    income = int(input("Enter Your Income: "))
    password = input("Enter Your Password: ")
    hash_object = hashlib.sha1(password.encode())
    hex_dig = hash_object.hexdigest()
    username = input("Enter Your Username: ")

    # Create table as per requirement

    try:
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE ")
        sql1 = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,
             SEX CHAR(1),
             INCOME FLOAT,
             PASSWORD CHAR(225),
             USERNAME CHAR(225))"""
        cursor.execute(sql1)
        sql = 'insert into EMPLOYEE values(%s, %s, %s, %s, %s, %s, %s)'
        val = (fname, lname, age, gender, income, str(hex_dig), username)
        cursor.execute(sql, val)
    except:
        sql = 'insert into EMPLOYEE values(%s, %s, %s, %s, %s, %s, %s)'
        val = (fname, lname, age, gender, income, str(hex_dig),username)
        cursor.execute(sql, val)

def login():
    sql3 = "SELECT * FROM EMPLOYEE"
    cursor.execute(sql3)
    result = cursor.fetchall()
    username = input("Enter Your Username: ")
    password= input("Enter Your Password: ")
    hash_object = hashlib.sha1(password.encode())
    passw = hash_object.hexdigest()
    if any(username in i for i in result) and any(passw in i for i in result):
        print("Successfully Logged In")
    else:
        print("Wrong Input!")

user_input = input("Login or Signup?: ").lower()
if user_input == "login":
    login()
else:
    signup()

db.commit()
# disconnect from server
db.close()

