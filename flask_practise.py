from flask import Flask #package #class
app = Flask(__name__)
#assigining instance of Flask class main to app 
@app.route('/')
#('/') is associated with the home function that returns a particular string displayed on the web page
#@app.route('/index_page/login Or reg') 
def index(): #index page
    return '<h1> Hello kitty!</h1>' #html
if __name__ == '__main__':
    app.run(debug=True)#run method in Flask class #debug for real time changes