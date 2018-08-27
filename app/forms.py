from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

# not being used, yet
# but maybe one day will decide this way of receiving and validating form fields is better than an onclick jquery event handling

class WordEntryForm(FlaskForm):

    noun1 = StringField('Noun', id = 'noun1', validators=[DataRequired()])
    adj1 = StringField('Adjective', id = 'adj1', validators=[DataRequired()])
    adj2 = StringField('Adjective', id = 'adj2', validators=[DataRequired()])
    adj3 = StringField('Adjective', id = 'adj3', validators=[DataRequired()])
    plnoun1 = StringField('Plural Noun', id= 'plnoun1', validators=[DataRequired()])
    plnoun2 = StringField('Plural Noun', id= 'plnoun2', validators=[DataRequired()])
    plnoun3 = StringField('Plural Noun', id= 'plnoun3', validators=[DataRequired()])
    verb1 = StringField('Verb', id = 'verb1', validators=[DataRequired()])
    verb2 = StringField('Verb', id = 'verb2', validators=[DataRequired()])
    verb3 = StringField('Verb', id = 'verb3', validators=[DataRequired()])
    verb4 = StringField('Verb', id = 'verb4', validators=[DataRequired()])
    submit = SubmitField('Generate Summary')
