from enum import unique
from app import db
import datetime

# Create Models based off of ERD (Database Tables)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(150), nullable=False, unique=True)
    email = db.column(db.String(150), nullable=False, unique=True)
    password = db.column(db.string(250), nullable=False)
    post= db.relationship('Post', backref='author', lazy=True)
    
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(150), nullable=False, unique=True)
    email = db.column(db.String(150), nullable=False, unique=True)
    password = db.column(db.string(250), nullable=False)
    content = db.colum(db.string(300))
    date_created = db.column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.colum(db.Integer,db.ForeignKey('user.id'), nullable=False)
    
    def __init(self,title,image,content):
        self.title = title
        self.image = image
        self.content = content
