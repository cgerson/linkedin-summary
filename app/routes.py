from flask_restful import Resource, reqparse
from app import api
from app import app
from flask import request

from flask import render_template

import random

"""
class Test(Resource):

    def get(self):
        return render_template('index.html', title='Generate a LinkedIn Summary', username="Claire")

api.add_resource(Test, "/index")
"""

def create_summary(result_dict):
    wildcards = ['relentlessly', 'tenaciously', 'persistently']

    first_part = "I am a {0}".format(random.choice(wildcards))

    summary = first_part + " {d[adj1]}, {d[adj2]}, and {d[adj3]} {d[noun1]} who lives to {d[verb1]} {d[plnoun1]}, {d[verb2]} {d[plnoun2]}, {d[verb3]} {d[plnoun3]} and {d[verb4]}.".format(d = result_dict)

    #summary = "testing {d[noun1]} {d[verb1]} !!!".format(d = result_dict)

    return summary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
      result = request.form
      summary = create_summary(result)
      return render_template("result.html",s = summary)

