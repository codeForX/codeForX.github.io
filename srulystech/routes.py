from flask import url_for, render_template
from srulystech import app
from srulystech.models import Post

cards = Post.query.all()

@app.route('/')
def index():
    return render_template('index.html',cards = cards )

@app.route('/login')
def login():
    return 'login'
 
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))