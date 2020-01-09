from flask import Flask
from flask import render_template, flash, redirect, url_for
#from ... import microblog
#from app.forms import LoginForm
import os
from flask import request, jsonify, make_response
import sys

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return "helloworld"
    #return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/mercury', methods=['GET', 'POST'])
def mercury():
    return render_template('Mercury.html');

@app.route('/venus', methods=['GET', 'POST'])
def venus():
    return render_template('Venus.html');

@app.route('/earth', methods=['GET', 'POST'])
def earth():
    return render_template('Earth.html');

@app.route('/mars', methods=['GET', 'POST'])
def mars():
    return render_template('Mars.html');

@app.route('/jupiter', methods=['GET', 'POST'])
def jupiter():
    return render_template('Jupiter.html');

@app.route('/saturn', methods=['GET', 'POST'])
def saturn():
    return render_template('Saturn.html');

@app.route('/uranus', methods=['GET', 'POST'])
def uranus():
    return render_template('Uranus.html');

@app.route('/neptune', methods=['GET', 'POST'])
def neptune():
    return render_template('Neptune.html');

@app.route('/robots', methods=['GET', 'POST'])
def robots():
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('robots.html');



@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method == "GET":
        username = request.cookies.get('test')
        if username == "yes":
            return render_template('suggestion.html')
    return render_template('cookies.html');

"""
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/handle_forms', method = ['POST'])
def handle_data():

"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    print('Hello world!', file=sys.stderr)
    if request.method == "POST":
        print("WE IN HERE");
        if request.form['theReal'] == 'Do Something':
            print("WE IN HERE3");
            return render_template('suggestion.html');
    print('Hello world2!', file=sys.stderr)
    return render_template("LoginForm.html");

@app.route('/formQ', methods=['GET','POST'])
def change():
    if request.method == "POST":
        print("WE IN HERE");
        if request.form['theReal'] == 'Do Something':
            print("WE IN HERE3");
            return render_template('suggestion.html');
    return render_template("formQ.html");

@app.route('/MultipleOf516', methods=['GET','POST'])
def check():
    if request.method == "POST":
        print("Hello", file = sys.stderr)
        req = request.get_json()
        print(type(req),dir(req), file = sys.stderr)
        print(req["number"], file = sys.stderr)
        if "number" in req:
            print("DUDUUDU", file = sys.stderr)
        """
        print("This is line 80 ", file = sys.stderr )
        print(req.json['number'], file = sys.stderr)
        print("The type is: " + type(req), file = sys.stderr)
        print(req, file = sys.stderr)
        """
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
