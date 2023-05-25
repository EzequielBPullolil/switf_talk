from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(logger=True, engineio_logger=True)


def create_app():
    app = Flask(__name__)

    socketio.init_app(app)

    import src.modules.chat.event
    return app
