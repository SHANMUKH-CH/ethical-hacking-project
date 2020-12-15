import re
from typing import NoReturn
from flask import Flask, render_template, request

app = Flask(__name__)

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
def hp():
  return render_template('homepage.html')

@app.route('/profilepage')
def pp():
  return render_template('profilepage.html')

@app.route('/searchpage')
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