from flask_restplus import abort
from api.config import MEDIA_URL as mediaUrl

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

import os

cache = {}

class ImageUploader():

    def __init__(self):
        self.mediaUrl = mediaUrl
        self.filename = ''


    def __cacheImageInMemory(self, imageFile):
        """
        This function caches image in memory.
        """
        # Check if image does not exist in cache
        if self.filename not in cache:
            key = self.filename
            cache[key] = imageFile


    def __uploadToServer(self, imageFile):
        """
        Saves image to media location.
        """
        self.filename = secure_filename(imageFile.filename)
        storagePath = os.path.join(self.mediaUrl, self.filename)
        imageFile.seek(0)
        imageFile.save(storagePath)
        imageFile.seek(0)
        img = imageFile.read()
        imageFile.close()
        return img


    def upload(self, imageFile):
        img = self.__uploadToServer(imageFile)
        self.__cacheImageInMemory(img)


    def download(self, filename):
        # Check if file name exist in cache.
        print(cache)
        if filename in cache:
            image = cache[filename]
            return image
        else:
            try:
                image = open(self.mediaUrl + filename, 'rb')
                
                self.filename = filename
                img = image.read()
                image.close()

                self.__cacheImageInMemory(img)

                return img
            except FileNotFoundError as ex:
                raise abort(404, 'File not found!')
            except Exception as ex:
                raise abort(500, str(ex))
