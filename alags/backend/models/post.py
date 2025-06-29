from backend.app import db # Import db from backend.app module
import datetime

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=True) # Optional image for the post
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationships
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")
    likes = db.relationship('Like', backref='post', lazy=True, cascade="all, delete-orphan")

    def __init__(self, user_id, content, image_url=None):
        self.user_id = user_id
        self.content = content
        self.image_url = image_url

    def __repr__(self):
        return f'<Post {self.id} by User {self.user_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'author_username': self.author.username, # Assumes backref 'author' on User model
            'content': self.content,
            'image_url': self.image_url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'like_count': len(self.likes),
            'comment_count': len(self.comments)
        }
