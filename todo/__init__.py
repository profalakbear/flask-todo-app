from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    SWAGGER_URL = '/swagger/'
    API_URL = '/static/swagger/todo.yml'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Todo List API"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    
    from . import db
    DB = db.init_app(app)
    migrate = Migrate(app, DB)

    from . import schemas
    schemas.create_marhsmellow_instance(app)

    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')

    return app