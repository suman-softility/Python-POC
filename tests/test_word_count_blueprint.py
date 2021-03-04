import pytest
from flask import Flask, Response
import json
from main import config
from app import app
from models.models import db
from blueprints import wordCountBluePrint
from .mock_data import dummy_result, dummy_word_count, dummy_url


@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    app.register_blueprint(wordCountBluePrint.bp)
    db.init_app(app)
    return app


@pytest.fixture
def mock_empty_db_call(mocker):
    mocker.patch("models.models.Result.get_all", return_value=[])


@pytest.fixture
def mock_dummy_db_results(mocker):
    mocker.patch("models.models.Result.get_all", return_value=[dummy_result])


@pytest.fixture
def mock_db_save(mocker):
    mocker.patch("models.models.Result.save")


def test_empty_get(client, mock_empty_db_call):
    response = client.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b'[]'


def test_get(client, mock_dummy_db_results):
    response = client.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json()[0]["wordCounts"] == dummy_word_count


def test_get_with_filter(client, mock_dummy_db_results):
    response = client.test_client().get("/?url_filter=redhat")
    assert response.status_code == 200
    assert response.get_json()[0]["wordCounts"] == dummy_word_count


def test_post(client, mock_db_save):
    response = client.test_client().post("/", json={"url": dummy_url})
    assert response.status_code == 200
    assert response.get_json() == dummy_word_count
