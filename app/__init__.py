from flask import Flask
from config import Config

# import our blueprinst for registration
from .shop.routes import shop
from .auth.routes import auth

#import database related
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db= SQLAlchemy()
migrate = Migrate(app, db)

app.config.from_object(Config)

# initialize database to work with our app
db.init_app(app)

app.register_blueprint(shop)
app.register_blueprint(auth)


from app import routes
from app import models