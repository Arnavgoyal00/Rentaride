from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/rentaride'
db = SQLAlchemy(app)


class user(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=False, nullable=False)
    Email = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(12), unique=True, nullable=False)
    Password = db.Column(db.String(30), unique=False, nullable=False)
    HostelN = db.Column(db.String(80), unique=False, nullable=False)
    HostelR = db.Column(db.String(80), unique=False, nullable=False)
    Type = db.Column(db.String(80), unique=False, nullable=False)


@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
def user():
    if (request.method == 'POST'):
        '''Add entery to database'''
        name = request.form.get('name')
        Email = request.form.get('Email')
        Phone = request.form.get('Phone')
        Password = request.form.get('Password')
        HostelN = request.form.get('HostelN')
        HostelR = request.form.get('HostelR')
        Type = request.form.get('Type')


        entry = user( name=name, Phone=Phone, Email=Email, Password=Password, HostelN=HostelN, HostelR=HostelR, Type=Type)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user')
def user1():
    return render_template('user.html')


app.run(debug=True)
