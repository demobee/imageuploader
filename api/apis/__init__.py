from flask import Blueprint
from flask_restplus import Api

from .imageupload import api as imageupload

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='Image uploader.', version='1.0.0')

api.add_namespace(imageupload)