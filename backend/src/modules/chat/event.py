from flask_socketio import SocketIO, emit
from src import socketio


@socketio.on('send_message')
def handle_send_message(data):
    '''
        Persists the received message and
        emits the new_message event for all chat members

        :data(dict): The event data
            Must have the following keys:
            * message(str): The message sended by the user
            * chat_id(str): The id of the chat where the message will be persisted
            * user_id(str): The id of the user who sends the message

        emits: new_message 
        raises: 
            UnauthorizedUser: User not belongs to chat
    '''
    print(data['message'])
    emit('new_message', room=data['chat_id'])
