from flask_restful import Resource, reqparse
from app import api
from app import app

from flask import request, jsonify
from flask import render_template

import random

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/_return_summary', methods=['POST', 'GET'])
def return_summary():
# initially built as a get request, updated to post request to take advantage of request.form

    words = ['adj1', 'adj2', 'adj3', 'verb1', 'verb2', 'verb3', 'verb4', 'plnoun1', 'plnoun2', 'plnoun3', 'noun1']

    if request.method == 'POST':
        words_dict = request.form

    else:
        words_dict = {}
        for word in words:
            words_dict[word] = request.args.get(word, '', type=str).lower()

    summary = build_summary(words_dict)

    return jsonify(result=summary)

# helper
def build_summary(result_dict):
    wildcards = ['a relentlessly', 'a tenaciously', 'a persistently', 'an insatiably', 'a bombastically', 'a yair-tastically']

    first_part = "I am {0}".format(random.choice(wildcards))

    second_part = " {d[adj1]}, {d[adj2]}, and {d[adj3]} {d[noun1]} who lives to {d[verb1]} {d[plnoun1]}, {d[verb2]} {d[plnoun2]}, {d[verb3]} {d[plnoun3]} and {d[verb4]}.".format(d = result_dict).lower()

    return first_part + second_part

# deprecated
@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
      result = request.form
      summary = create_summary(result)
      return render_template("result.html",s = summary)
