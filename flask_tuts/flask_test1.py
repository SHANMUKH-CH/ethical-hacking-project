from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Goto kitty/name and see the result!</h1>'
@app.route('/kitty/<name>')
def kitty(name):
    kitty_name = ' '
    if name[-1] =='y' or 'Y':
        kitty_name = name[:-1] + 'iful'
    else:
        kitty_name = name + 'y'
    return '<h1> your kitty name: ' + kitty_name + '</h1>'
if __name__ == '__main__':
    app.run()