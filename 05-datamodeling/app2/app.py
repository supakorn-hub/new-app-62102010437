from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = "secret-key"

db = SQLAlchemy(app)

class Student(db.Model):
   student_id = db.Column('student_id', db.Integer, primary_key = True)
   first_name = db.Column(db.String(80), nullable=False)
   last_name = db.Column(db.String(80), nullable=False)
   age = db.Column(db.Integer())
   phone = db.Column(db.Integer())
   email = db.Column(db.String(120))



app.env="development"
app.run(debug=True)