import re, os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir,'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
####
class users(db.Model):
  #manual table choice!
  __tablename__ = 'users'
  
  #columms
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.Text)
  def __init__(self,id,name):
    self.id = id
    self.name = name
  def __repr__(self):
    return f'users {self.id} {self.name}'

@app.route('/', methods=['GET','POST'])
def index():
  #a static webpage with buttons to login page as well as register
  return render_template('index.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/register')
def reg():
  return render_template('register.html')

@app.route('/homepage')
#xss_stored
def hp():
  return render_template('homepage.html')

@app.route('/profilepage')
#csrf_attack
def pp():
  return render_template('profilepage.html')

@app.route('/searchpage')
#sql_injection
def sp():
  return render_template('searchpage.html')

@app.route('/thank_you')
def thank_you():
  email = request.args.get('email')
  regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
  if (re.search(regex, email)):
    return render_template('homepage.html', email=email[:8])
  else:
    return render_template('emailvalidcheck.html')

@app.errorhandler(404)
def pnf(errorhandler):
  return "<h1>Page not found 404 error</h1>",404

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)