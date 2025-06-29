import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
# Ensure migrations are stored within the backend directory
migrate = Migrate(directory='backend/migrations')
jwt = JWTManager()

def create_app(config_class='backend.config.DevelopmentConfig'): # Adjusted config path
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app) # Enable CORS for all routes and origins by default

    # Import and register blueprints (routes)
    # from .routes.auth import auth_bp
    # from .routes.posts import posts_bp
    # from .routes.interactions import interactions_bp

    # app.register_blueprint(auth_bp, url_prefix='/api/auth')
    # app.register_blueprint(posts_bp, url_prefix='/api/posts')
    # app.register_blueprint(interactions_bp, url_prefix='/api') # e.g., /api/posts/<post_id>/like

    @app.route('/')
    def hello():
        return "Hello from Alags Backend!"

    return app

# Import models here to ensure they are known to SQLAlchemy
# This is crucial for Flask-Migrate to detect the models.
# These imports should be relative to the 'backend' package.
from .models.user import User
from .models.post import Post
from .models.comment import Comment
from .models.like import Like

if __name__ == '__main__':
    # This is for development only.
    # In production, use a WSGI server like Gunicorn or uWSGI.
    app = create_app()
    app.run(debug=True)
