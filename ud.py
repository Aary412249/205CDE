from flask import Flask
from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, SubmitField, RadioField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import validators, ValidationError
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SubmitField

import pymysql
app = Flask(__name__)
app.secret_key = 'any random string'

db = pymysql.connect(host="localhost", user="root", password="", database="until_dawn")
db.connect()

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

@app.route('/shop.html')
def shop():
    return render_template('shop.html', title='Shop')

@app.route('/shop2.html')
def shop2():
    return render_template('shop2', title='Shop 2')

@app.route('/clubbar.html')
def clubbar():
    return render_template('clubbar.html', title='Clubs & Bars')

@app.route('/about.html')
def about:
    return render_template('about.html', title='About')

@app.route('/contact.html')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/cart.html')
def cart():
    return render_template('cart.html', title='cart')

@app.route('/login.html')
def login():
    return render_template('login.html', title='Login')

@app.route('/register.html')
def register():
    return render_template('register.html', title='Register')

if __name__ == '__main__':
	app.debug = True
	app.run(host = "localhost", port=8080)