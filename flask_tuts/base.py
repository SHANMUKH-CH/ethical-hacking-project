from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/kittty/<name>')
def kitty_name(name):
    return render_template('kittty.html', name=name)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 