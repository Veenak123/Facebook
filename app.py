from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def signup_data(email, password,confirmpassword):
    connection = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password ='veena@123',
        database ='facebook1'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO facebook_users(email, password,confirmpassword) VALUES (%s, %s,%s)'
    data = (email, password,confirmpassword)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

def login_data(email, password):
    connection = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password ='veena@123',
        database ='facebook1'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO login(email, password) VALUES (%s, %s)'
    data = (email, password)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    
def accdtl_data(first_name, last_name, mobileno, gender):
    connection = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password ='veena@123',
        database ='facebook1'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO accountdetails(first_name, last_name, mobileno, gender) VALUES (%s, %s, %s, %s)'
    data = (first_name, last_name, mobileno, gender)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirmpassword=request.form['confirmpassword']
    

        signup_data(email, password,confirmpassword)

        return render_template('login.html')
        
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        login_data(email, password)

        return render_template('home.html')
    return render_template('login.html')

@app.route('/accdetail', methods=['GET', 'POST'])
def acc_details():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        mobileno = request.form['mobileno']
        gender = request.form['gender']

        accdtl_data(first_name, last_name, mobileno, gender)

        return 'Account Details Added Successfully'
        
    return render_template('account_details.html')

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/friends')
def friends():
    return render_template("friends.html")

if __name__ == '__main__':
    app.run(debug=True)