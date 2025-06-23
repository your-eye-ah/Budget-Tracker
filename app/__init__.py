from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'replace-with-a-secure-random-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/budget.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Import models AFTER db.init_app to bind models to the app context
    from . import models

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
