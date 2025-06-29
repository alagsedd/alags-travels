from backend.app import db # Import db from backend.app module
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False) # Increased length for stronger hashes
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    bio = db.Column(db.Text, nullable=True)
    profile_picture_url = db.Column(db.String(255), nullable=True)

    # Relationships
    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='commenter', lazy=True, cascade="all, delete-orphan")
    likes = db.relationship('Like', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, email, password, bio=None, profile_picture_url=None):
        self.username = username
        self.email = email
        self.set_password(password)
        self.bio = bio
        self.profile_picture_url = profile_picture_url

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email, # Be cautious about exposing email
            'created_at': self.created_at.isoformat(),
            'bio': self.bio,
            'profile_picture_url': self.profile_picture_url,
            'post_count': len(self.posts)
        }
