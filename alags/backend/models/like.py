from backend.app import db # Import db from backend.app module
import datetime

class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # User who liked the post
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False) # Post that was liked
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # Unique constraint to prevent a user from liking the same post multiple times
    __table_args__ = (db.UniqueConstraint('user_id', 'post_id', name='_user_post_uc'),)

    # No explicit backref needed here if 'likes' on User and Post are sufficient

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id

    def __repr__(self):
        return f'<Like by User {self.user_id} on Post {self.post_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            # 'username': self.user.username, # If you need username directly
            'post_id': self.post_id,
            'created_at': self.created_at.isoformat()
        }
