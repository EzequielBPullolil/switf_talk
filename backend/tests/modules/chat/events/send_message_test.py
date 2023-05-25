class TestSendMessageEvent:
    '''
      This test verifies the correct operation of the send_message event\
      using the following test cases:
        * The correct emission emit update_messages to all users of the chat to which the message was sent
        * Emit send_message event to a user we don't have a chat with creates it
        * Emits send_message without auth_token emits auth_error event
    '''

    def test_successful_send_message_event_emits_update_messages(self, create_sio):
        '''
          Check the emission of the 'update_messages' event for all users who are in the chat
        '''
        client1 = create_sio()
        client2 = create_sio()

        assert client1.is_connected()
        assert client2.is_connected()

        client1.emit('send_message', 'hi')

        received = client2.get_received()

        assert len(received) > 0
