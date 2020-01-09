from flask import Flask
from flask import render_template, flash, redirect, url_for
#from ... import microblog
#from app.forms import LoginForm
import os
from flask import request, jsonify, make_response, send_file
import sys

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('Mercury.html');
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

@app.route('/thehiddenpage', methods=['GET', 'POST'])
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

@app.route('/hex', methods=['GET', 'POST'])
def hex():
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('base64.html');


@app.route('/nebula', methods=['GET', 'POST'])
def steg():
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('steg.html');

@app.route('/essveegee', methods=['GET', 'POST'])
def svg():
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('svg.html');

@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method == "GET":
        username = request.cookies.get('hmmm')
        if username == "yes":
            return render_template('cookiesFlag.html')
    return render_template('cookies.html');

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("LoginForm.html")
######BUTTON LINK HERE IS OKAY...
@app.route('/formQ', methods=['GET','POST'])
def change():
    """
    if request.method == "POST":
        if request.form['theReal'] == '5':
            print("WE IN HERE3");
            return render_template('formQFlag.html');
            """
    return render_template("formQ.html");

#HAVE TO RENDER TEMPLATE
@app.route('/MultipleOf516', methods=['GET','POST'])
def check():
    #print("Hello", file = sys.stderr)
    res = make_response(jsonify({"message": "nope"}),500)
    if request.method == "POST":
        #print("Hello", file = sys.stderr)
        req = request.get_json()
        #print(type(req),dir(req), file = sys.stderr)
        print(req, file = sys.stderr)
        #print("inside post", file = sys.stderr)
        print("There's a post" + req["message"], file = sys.stderr)
        if "message" in req:
            #print("Val????" + req["message"], file = sys.stderr)
            if req["message"] == "5":
                res = make_response(jsonify({"message": "FLAG{Reality_Can_Be_Whatever_I_Want"}),200)
        """
        print("This is line 80 ", file = sys.stderr )
        print(req.json['number'], file = sys.stderr)
        print("The type is: " + type(req), file = sys.stderr)
        print(req, file = sys.stderr)
        """
    return res

#Robots.txt file
@app.route("/robots.txt")
def robots_txt():
    robots_path = os.path.join(app.static_folder,'robots.txt')
    return send_file(robots_path);

if __name__ == "__main__":
    app.run(debug=True)
