from flask_restful import Resource, reqparse
from app import api
from app import app
from flask import request, jsonify

from flask import render_template

from build_summary import build_summary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/_return_summary')
def return_summary():
    
    words = ['adj1', 'adj2', 'adj3', 'verb1', 'verb2', 'verb3', 'verb4', 'plnoun1', 'plnoun2', 'plnoun3', 'noun1']

    words_dict = {}
    for word in words:
        words_dict[word] = request.args.get(word, '', type=str)
    summary = build_summary(words_dict)

    return jsonify(result=summary)

# deprecated
@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
      result = request.form
      summary = create_summary(result)
      return render_template("result.html",s = summary)