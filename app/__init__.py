from flask import Flask
from .views import view_pages

app = Flask(__name__)

def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(view_pages)
    return app