import re
import db
from flask import Flask, redirect,render_template, request,session,url_for
from flask_mysqldb import MySQL,MySQLdb
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

app.secret_key='kingkongdingdong'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='shanmukh'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])
    search_query = request.args.get('q')
    comments = db.get_comments(search_query)
    return render_template('home.html',comments=comments,search_query=search_query)
@app.route('/login',methods=["GET","POST"])
def login():
    message = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
        username = request.form['username'] 
        password = request.form['password'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM registration WHERE username = % s AND password = % s', (username, password, )) 
        account = cursor.fetchone() 
        if account: 
            session['loggedin'] = True
            session['id'] = account['id'] 
            session['username'] = account['username'] 
            msg = 'Logged in successfully !'
            return render_template('home.html', msg = msg) 
        else: 
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = message)

@app.route('/register', methods =['GET', 'POST'])
def register(): 
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form : 
        username = request.form['username'] 
        password = request.form['password']
        confirm = request.form['confrim']
        email = request.form['email'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM registration WHERE username = % s', (username, )) 
        account = cursor.fetchone()
        if account: 
            msg = 'Bruhhh Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email): 
            msg = 'Bruhhh Invalid email address !'
        elif password != confirm:
            msg = 'Bruhhh Password mismatch !'
        elif not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email: 
            msg = 'Bruhhh Please fill out the form !'
        else: 
            cursor.execute('INSERT INTO registration VALUES (NULL, % s, % s, % s)', (username, email, password )) 
            mysql.connection.commit() 
            msg = 'You have successfully registered !'
    elif request.method == 'POST': 
        msg = 'Bruhh Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/update', methods=['GET', 'POST'])
@csrf.exempt
def update():
    
    pass

@app.route('/logout')
def logout(): 
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('username', None) 
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)