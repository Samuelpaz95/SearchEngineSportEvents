from flask_script import Manager

from app import init_app
from config import config

app = init_app(config['development'])
manager = Manager(app)
if __name__ == "__main__":
    manager.run();
