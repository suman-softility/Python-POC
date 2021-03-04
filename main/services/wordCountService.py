import requests
import operator
import re
import nltk
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup
from models.models import Result


def countWordsFromUrl(url):
    """ Contains the buisiness logic to calculate the number of words in the webpage of the URL. """
    errors = []
    results = {}
    try:
        r = requests.get(url)
    except:
        errors.append(
            "Unable to get URL:" + url + ". Please make sure it's valid and try again."
        )
    if r:
        # get the word counts from html text.
        raw_word_count, no_stop_words_count = parseHtmlText(r)
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
            result.save()
        except Exception as exc:
            errors.append("Unable to add item to database." + str (exc))
    return errors, results


def getWordCounts(urlFilter):
    errors = []
    results = {}
    try:
        results = Result.get_all(urlFilter)
    except:
        errors.append("Unable to fetch from DB.")
    processedResults = []
    for result in results:
        processedResult = {
            "url": result.url,
            "wordCounts": sorted(
                result.result_no_stop_words.items(),
                key=operator.itemgetter(1),
                reverse=True)
        }
        processedResults.append(processedResult)
    return errors, processedResults


def parseHtmlText(text):
    """ Parses the html text to return word counts. """
    # text processing
    raw = BeautifulSoup(text.text, 'html.parser').get_text()
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
    return raw_word_count, no_stop_words_count