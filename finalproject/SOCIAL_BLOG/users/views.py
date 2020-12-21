#users/views.py
#reg,login,logout,account update, posts
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask.signals import request_tearing_down
from flask_login import login_user,current_user, logout_user, login_required
from sqlalchemy.util.compat import u
from SOCIAL_BLOG import db
from SOCIAL_BLOG.models import User, BlogPost
from SOCIAL_BLOG.users.forms import RegisterForm, loginForm, UpdateUserForm
from SOCIAL_BLOG.users.picture_handler import add_profile_pic

users =Blueprint('users',__name__)
#logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))

#register
@users.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, 
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("yo thanks for registration!")
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

#login
@users.route('/login', methods=['GET','POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in success!')
            next= request.args.get('next')
            if next == None or next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
        return render_template('login.html',form=form)