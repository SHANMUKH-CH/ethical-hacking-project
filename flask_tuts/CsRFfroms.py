#secret key for csrf protection
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

#for csrf protection we need a secret key
app.config['SECRET_KEY'] ='mysecrtkey' #astring
#inhertance from flaskforms
class InfoForm(FlaskForm):
  breed=StringField("what breed are you?")
  submit=SubmitField("submit")
#view function
@app.route('/',methods=['GET','POST'])
def index():
  breed = False
  form = InfoForm()
  if form.validate_on_submit():
    breed = form.breed.data
    form.breed.data =''
  return render_template('home2.html',form=form,breed=breed)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)