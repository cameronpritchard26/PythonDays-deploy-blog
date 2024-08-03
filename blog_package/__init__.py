# Description: This file initializes the Flask app and configures the database, login manager, and gravatar.
# Dependencies: flask, flask_bootstrap, flask_sqlalchemy, sqlalchemy.orm, flask_ckeditor, flask_login, flask_gravatar, blog_package.constants
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_gravatar import Gravatar
from blog_package.constants import *

# Create the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# Create the database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure the login manager
login_manager = LoginManager()
login_manager.init_app(app)
