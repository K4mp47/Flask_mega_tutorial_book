from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { "username" : "Miguel"}
    posts = [
        {
            'author' : { 'username' : 'Linda' },
            'body'   : 'Beautiful day in Poland!'
        },
        {
            'author' : { 'username' : 'Jack' },
            'body'   : 'Marvel is the best'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data)) 
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)
