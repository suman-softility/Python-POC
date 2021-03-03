import os
import requests
import operator
import re
import nltk
import json
from flask import Flask, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import Result


@app.route('/', methods=['POST'])
def index():
    errors = []
    results = {}
    try:
        url = request.form['url']
        r = requests.get(url)
    except:
        errors.append(
            "Unable to get URL:" + url + ". Please make sure it's valid and try again."
        )
        return custom_response(errors, 400)
    if r:
        # text processing
        raw = BeautifulSoup(r.text, 'html.parser').get_text()
        nltk.data.path.append('./nltk_data/')  # set the path
        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)
        # remove punctuation, count raw words
        nonPunct = re.compile('.*[A-Za-z].*')
        raw_words = [w for w in text if nonPunct.match(w)]
        raw_word_count = Counter(raw_words)
        # stop words
        no_stop_words = [w for w in raw_words if w.lower() not in stops]
        no_stop_words_count = Counter(no_stop_words)
        # save the results
        results = sorted(
            no_stop_words_count.items(),
            key=operator.itemgetter(1),
            reverse=True
        )
        try:
            result = Result(
                url=url,
                result_all=raw_word_count,
                result_no_stop_words=no_stop_words_count
            )
            db.session.add(result)
            db.session.commit()
        except:
            errors.append("Unable to add item to database.")
    return custom_response(results, 200)

def custom_response(res, status_code):
        """ Custom Response Function  """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
            )


if __name__ == '__main__':
    app.run()