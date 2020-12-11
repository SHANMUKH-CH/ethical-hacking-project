from flask import Flask #package #class
app = Flask(__name__)
#assigining instance of Flask class main to app 
@app.route('/')
#('/') is associated with the home function that returns a 
# particular string displayed on the web page
#@app.route('/index_page/login Or reg') 
def index(): #index page
    return '<h1> Hello kitty!</h1>' #html

@app.route('/login')
def login(): #login page
    return '<h1><strong>Bruh!<!strong>do you want to login?</h1>' #login

@app.route('/kitty/<name>')#enter the name in the url
def kitty(name):
    return "<h1>This is page for {} bruh!</h1>".format(name.upper())

@app.route('/register')
def register(): #register page
    return '<h1>Bruh! do you want to register?</h1>' #register

if __name__ == '__main__':
    app.run(debug=True)#run method in Flask class #debug for real time changes,
    #dangerous becareful while production set it off