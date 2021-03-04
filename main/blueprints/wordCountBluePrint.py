import json
from flask import Blueprint, request, Response
from services.wordCountService import countWordsFromUrl, getWordCounts

bp = Blueprint('word_count', __name__, url_prefix='/')


@bp.route('/', methods=['POST'])
def calculateWordCount():
    """ Parses the URL and calculates the number of words in that page. """
    url = request.get_json().get('url')
    errors, results = countWordsFromUrl(url)
    if errors:
        return create_response(errors, 400)
    return create_response(results, 200)


@bp.route('/', methods=['GET'])
def fetchWordCounts():
    url = request.args.get("url_filter", None)
    errors, results = getWordCounts(url)
    if errors:
        return create_response(errors, 400)
    return create_response(results, 200)


def create_response(res, status_code):
        """ Custom Response Function  """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
            )