import os

from froms import AddForm, DelForm, AddOwnerForm
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
    name = db.Column(db.text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self,name): 
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"

class Owner(db.Models):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Intger, db.ForeignKey("pupppies.id"))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.namr}"

        else:
            return f'Puppy name: {self.name} and no owner assigned yet!'




### view function ###
@app.route('/')
def index():
    return render_template('home')

@app.route('/add_owner', methods=['GET','POST'])
def add_owner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data

        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('add_owner.html', form=form)

@app.route('/add', methods=['GET','POST'])
def add_pup():
     form = AddForm()

     if form.validate_on_submit():

         name = form.name.data

         new_pup = Puppy(name)
         db.session.add(new_pup)
         db.session.commit()

         return redirect(url_for('list_pup'))
    
    return render_template('ass,html',form= form)

@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@app.route('/delete', methods=['GET','POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delet(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)







