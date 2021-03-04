import os
from flask import Flask
from blueprints import wordCountBluePrint
from models.models import db


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(wordCountBluePrint.bp)
db.init_app(app)


if __name__ == '__main__':
    app.run()