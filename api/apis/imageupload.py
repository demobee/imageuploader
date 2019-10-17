import flask
from flask import send_file, jsonify
from flask_restplus import Namespace, Resource, fields, abort, reqparse
from werkzeug.datastructures import FileStorage

from api.services.services import upload, download
from api.validate import *

api = Namespace('images', description='Image endpoints')

responseModel = api.model('imageUpload', {'message' : fields.String(),
'downloadUrl' : fields.String()})

@api.route('/upload')
@api.response(201, 'File uploaded successfully.')
@api.response(400, 'Bad request.')
@api.response(500, 'Internal server error.')
class ImageUpload(Resource):
    @api.marshal_with(responseModel)
    def post(self):
        """
        Uploads image file to server.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('image', type=FileStorage, location='files', required=True)

        args = parser.parse_args()
        image =args['image']

        # Performs the following validations:
        # 1.    Image must not be null
        # 2.    Must be of type image
        # 3.    Width and Height must not be greater than 10 and 20 respectively.
        checkIfImageIsNull(image)
        checkIfFileIsImageType(image)
        checkWidthAndHeight(image)

        # Upload image to server
        response = upload(image)
        return response


@api.route('/download/<string:filename>')
@api.response(200, 'File downloaded successfully.')
@api.response(404, 'File not found.')
@api.response(500, 'Internal server error.')
class ImageDownload(Resource):
    def get(self, filename):
        """
        Downloads image file to server.
        """
        # Validate user's input, ensure filename is image format
        checkIfFileNameIsNullOrEmpty(filename)
        checkFileFormat(filename)
        image = download(filename)
        image.seek(0)
        return send_file(image, as_attachment=True,attachment_filename='download.png', mimetype='image/png')