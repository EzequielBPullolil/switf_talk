from src import create_app, socketio
import pytest


@pytest.fixture()
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def create_sio(app, client):
    def create_sio():
        sio = socketio.test_client(
            app, flask_test_client=client)
        return sio

    return create_sio
