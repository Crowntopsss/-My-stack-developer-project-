from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = stringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of puppy to remove: ')
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskFrom):
    name = StringField('Name of Owner:)
    pup_id = IntegerField('Id of Puppy: ')
    submit = SubmitField("Add Owner")