import imghdr
from PIL import Image
from flask_restplus import abort
from api.config import MAX_HEIGHT, MAX_WIDTH

def checkIfImageIsNull(image):
    """Checks if the image file exist."""
    if image is None:
        raise abort(400, 'ImageFile is null.')


def checkIfFileIsImageType(image):
    """Checks file type. Only images are accepted."""
    if imghdr.what(image) == None:
        raise abort(400, 'Unsupported image format.')


def checkWidthAndHeight(image):
    """Checks if the width or height is more than maximum sepcified"""
    im = Image.open(image)
    width, height = im.size
    if width > MAX_WIDTH:
        raise abort(400, 'Invaid width')
    if height > MAX_HEIGHT:
        raise abort(400, 'Invaid height')


def checkIfFileNameIsNullOrEmpty(filename):
    """Check if file name is empty"""
    if filename is None or filename.strip() == "":
        raise abort(400, 'Invalid filename specified')


def checkFileFormat(filename):
    """ Check file format to confirm it's image type """
    acceptedImageFormats = ['png','jpeg', 'jpg', 'jpe', 'gif', 'tiff']
    if filename.lower().split('.')[-1] not in acceptedImageFormats:
        raise abort(400, 'Unrecognised image format.')
