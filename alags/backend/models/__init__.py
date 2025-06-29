# This file can be empty, or used to import models for easier access
# e.g., from .user import User
# from .post import Post

# For now, we'll define models directly in their respective files
# and ensure app.py imports them if necessary, or that blueprints do.

# Alternatively, to make db instance available for models:
# from ..app import db
# This creates a circular dependency if app.py imports models from here directly.
# A better pattern is to initialize db in app.py and have models import it from there.
# Or, pass 'db' to model definitions if they are in separate files.

# For simplicity with Flask-SQLAlchemy, models usually define themselves using a db instance
# that will be initialized by the app.

# Let's prepare for individual model files:
# from .user import User
# from .post import Post
# from .comment import Comment
# from .like import Like

# __all__ = ['User', 'Post', 'Comment', 'Like']
