from api import app
from api.config import APP_HOST, APP_PORT

myapp = app.create_app()

if __name__ == "__main__":
    myapp.run(APP_HOST, APP_PORT)