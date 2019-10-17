from flask_restplus import abort
from flask import request
import io

from api.utils.ImageUploader import ImageUploader
from api.models.models import ImageResponse


def upload(image):
    """
    This service uploads images to app server.
    """
    imageUploader = ImageUploader()
    try:
        imageUploader.upload(image)
        downloadUrl = request.base_url.replace('upload', 'download') + '/' + image.filename
        response = ImageResponse('Image upload was successful.', downloadUrl)
        return response
    except Exception as ex:
        raise abort(500, str(ex))


def download(filename):
    """
    This service dowloads images from server.
    """
    imageUploader = ImageUploader()
    try:
        byteImage = imageUploader.download(filename)
        image = io.BytesIO(byteImage)
        return image
    except Exception as ex:
        raise abort(500, str(ex))