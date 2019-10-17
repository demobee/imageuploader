from flask import Flask
from flask_restful import Api

from api.apis import blueprint
import api.validate as helper
import api.config as config

def create_app():
    """
    Create the flask app
    """
    app = Flask(__name__)
    app.config['MEDIA_URL'] = config.MEDIA_URL
    app.register_blueprint(blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(config.APP_HOST, config.APP_PORT)