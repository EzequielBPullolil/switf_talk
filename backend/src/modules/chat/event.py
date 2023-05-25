from flask_socketio import SocketIO, emit
from src import socketio


@socketio.on('send_message')
def handle_send_message(message):
    print(message)
    emit('update_messages', broadcast=True)
