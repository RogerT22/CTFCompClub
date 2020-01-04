from flask import Flask
from flask import render_template, flash, redirect, url_for
#from ... import microblog
#from app.forms import LoginForm
import os

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return "helloworld"
    #return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/planets', methods=['GET', 'POST'])
def planets():
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('suggestion.html');

@app.route('/planets', methods=['GET', 'POST'])
def cookies():
    return "On cookies"

"""
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

"""
if __name__ == "__main__":
    app.run(debug=True)
