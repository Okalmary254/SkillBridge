from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    

    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        SQLALCHEMY_DATABASE_URI='sqlite:///skillbridge.db'
    )

    # Enable CORS for all routes (allow frontend dev server)
    CORS(app, supports_credentials=True)


    # Register blueprints
    from .routes import profile, jobdata, gap, recommend, auth, password, avatar
    app.register_blueprint(profile.profile_bp, url_prefix='/api/profile')
    app.register_blueprint(jobdata.jobdata_bp)
    app.register_blueprint(gap.gap_bp)
    app.register_blueprint(recommend.recommend_bp)
    app.register_blueprint(auth.auth_bp, url_prefix='/api/auth')
    app.register_blueprint(password.password_bp, url_prefix='/api/password')
    app.register_blueprint(avatar.avatar_bp, url_prefix='/api/avatar')

    # Initialize database
    from .models import db
    db.init_app(app)

    # Create tables if they do not exist
    with app.app_context():
        db.create_all()

    return app