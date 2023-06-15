from flask import render_template
from app import app

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
