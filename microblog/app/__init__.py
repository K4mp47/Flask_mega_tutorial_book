from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 
login = LoginManager(app)
login.login_view = 'login'      
# this code come from stack and chatgpt, for make the 'context'
# it's actually works and i use it for made function
# db.session.add() and db.session.commit() works with all the other stuff 
# for db. If you remove, the python interpreter gives you a RuntimeError out of context.
app.app_context().push()

from app import routes, models
