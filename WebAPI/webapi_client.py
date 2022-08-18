from WebAPI import websocket
from WebAPI.webapi_2_pb2 import *


class WebApiClient:
    def __init__(self, need_to_log=True):
        self._need_to_log = need_to_log
        self._connection = None

    def __del__(self):
        self.disconnect()

    def connection(self):
        return self._connection

    def connect(self, url, timeout=1000000.0):
        self._connection = websocket.create_connection(url, timeout)

    def disconnect(self):
        if self._connection:
            self._connection.close()

    def send_client_message(self, client_msg):
        self._connection.send(client_msg.SerializeToString(), websocket.ABNF.OPCODE_BINARY)
        if self._need_to_log:
            print("Client message sent:\n" + str(client_msg))

    def send_partial_client_message(self, client_msg):
        self._connection.send(client_msg.SerializePartialToString(), websocket.ABNF.OPCODE_BINARY)
        if self._need_to_log:
            print("Incomplete client message sent:\n" + str(client_msg))

    def receive_server_message(self):
        server_msg = ServerMsg()
        opcode, data = self._connection.recv_data()
        if opcode == websocket.ABNF.OPCODE_TEXT:
            raise Exception("Received unexpected text message from WebAPI server")
        elif opcode == websocket.ABNF.OPCODE_CLOSE:
            raise websocket.WebSocketConnectionClosedException(
                "Can't receive message - WebAPI server closed connection")

        server_msg.ParseFromString(data)

        if self._need_to_log:
            print("Server message received:\n" + str(server_msg))
        return server_msg
