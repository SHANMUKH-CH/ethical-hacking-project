from flask import Flask, render_template
from flask.templating import render_template
import jinja2 #package #class
app = Flask(__name__)
#assigining instance of Flask class main to app 
#('/') is associated with the home function that returns a 
# particular string displayed on the web page
#@app.route('/index_page/login Or reg') 
# def index(): #index page
#     return '<h1> Hello kitty!</h1>' #html

# @app.route('/login')
# def login(): #login page
#     return '<h1><strong>Bruh!<!strong>do you want to login?</h1>' #login

# @app.route('/kitty/<name>')#enter the name in the url
# def kitty(name):
#     return "<h1>This is page for {} bruh!</h1>".format(name.upper())

# @app.route('/register')
# def register(): #register page
#     return '<h1>Bruh! do you want to register?</h1>' #register
#jinja2 {{}} - variable
# for loops and if statements - {% %}
@app.route('/')
def index():
    user_login = True #fale - #if or #else
    mynum=[1,2,3,4,5,6,7,8,9,10]
    name_variable='shan'
    letters = list(name_variable)
    kitty_dictionary={'kitty_name':'shan'}
    return render_template('basic.html', 
                           my_variable=name_variable, 
                           letters=letters,
                           kitty_dictionary=kitty_dictionary,
                           mynum=mynum,
                           user_login=user_login)
if __name__ == '__main__':
    app.run(debug=True)#run method in Flask class #debug for real time changes,
    #dangerous becareful while production set it off