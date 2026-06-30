from flask import Flask

from config import Config
from extensions import db
from extensions import migrate

from courses.routes import courses_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(courses_bp)

    @app.route("/")
    def home():
        return {
            "message": "Flask Course Management API"
        }

    return app


app = create_app()

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)