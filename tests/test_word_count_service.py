import pytest
from flask import Flask, Response
import json
from main import config
from app import app
from models.models import db
from services.wordCountService import getWordCounts, countWordsFromUrl
from .mock_data import dummy_result, dummy_url, dummy_service_result, dummy_word_count_dict, dummy_web_page



@pytest.fixture
def mock_dummy_db_results(mocker):
    mocker.patch("models.models.Result.get_all", return_value=[dummy_result])


@pytest.fixture
def mock_db_save(mocker):
    mocker.patch("models.models.Result.save")


@pytest.fixture
def mock_html_parser(mocker):
    mocker.patch("services.wordCountService.parseHtmlText", return_value=([], dummy_word_count_dict))


@pytest.fixture
def mock_response_text(mocker):
    mocker.patch("requests.Response.text", return_value=dummy_web_page)


def test_get_word_count(mock_dummy_db_results):
    _, results = getWordCounts(None)
    assert results[0]["wordCounts"] == dummy_service_result


def test_get_word_count_with_filter(mock_dummy_db_results):
    _, results = getWordCounts("redhat")
    assert results[0]["wordCounts"] == dummy_service_result


def test_calculate_word_count(mock_db_save, mock_html_parser):
    _, results = countWordsFromUrl(dummy_url)
    assert results == dummy_service_result
