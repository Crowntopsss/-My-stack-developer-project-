import os

from froms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

### SQL DATABASE SECTION ###

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app,db)

### models ###

class Puppy(db.models):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key = True)
    name =db.Column(db.text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"

### view function ###
@app.route('/')
def index():
    return render_template('home')

@app.route('/add', methods=['GET','POST'])
def add_pup():
     form = AddForm()





