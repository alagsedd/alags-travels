from backend.app import db # Import db from backend.app module
import datetime

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # User who made the comment
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False) # Post being commented on
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # No explicit backref needed here if 'comments' on User and Post are sufficient

    def __init__(self, user_id, post_id, content):
        self.user_id = user_id
        self.post_id = post_id
        self.content = content

    def __repr__(self):
        return f'<Comment {self.id} by User {self.user_id} on Post {self.post_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'commenter_username': self.commenter.username, # Assumes backref 'commenter' on User model
            'post_id': self.post_id,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }
