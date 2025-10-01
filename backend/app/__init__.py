from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        DATABASE_URL='sqlite:///skillbridge.db'
    )

    # Register blueprints
    from .routes import profile, jobdata, gap, recommend
    app.register_blueprint(profile.profile_bp, url_prefix='/api/profile')
    app.register_blueprint(jobdata.jobdata_bp)
    app.register_blueprint(gap.gap_bp)
    app.register_blueprint(recommend.recommend_bp)

    return app