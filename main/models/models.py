from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Result(db.Model):
    __tablename__ = 'results'

    url = db.Column(db.String(), primary_key=True)
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def save(self):
        if not Result.query.get(self.url):
            db.session.add(self)
            db.session.commit()

    @staticmethod
    def get_all(urlFilter):
        if urlFilter:
            search = '%{}%'.format(urlFilter)
            return Result.query.filter(Result.url.like(search)).all()
        return Result.query.all()