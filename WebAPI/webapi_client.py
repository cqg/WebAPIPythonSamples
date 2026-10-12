from WebAPI import websocket
from WebAPI.webapi_2_pb2 import *


class WebApiClient:
    def __init__(self, need_to_log=True, connected=False):
        self._need_to_log = need_to_log
        self._connected = connected
        self.websocket_client = websocket.WebSocket()

    def __del__(self):
        if self._connected:
            self.disconnect()

    def connect(self, url):
        self.websocket_client.connect(url)

    def disconnect(self):
        self.websocket_client.close()
        self._connected = False
        print("Disconnect by request\n")

    def send_client_message(self, client_msg):
        self.websocket_client.send(client_msg.SerializeToString())
        if self._need_to_log:
            print("Client message sent:\n" + str(client_msg))

    def send_partial_client_message(self, client_msg):
        self._connection.send(client_msg.SerializePartialToString())
        if self._need_to_log:
            print("Incomplete client message sent:\n" + str(client_msg))

    def receive_server_message(self):
        server_msg = ServerMsg()
        while True:
            try:
                data = self.websocket_client.recvmsg()
                break
            except websocket.WebSocketWantReadError:
                # Only part of a message has been received yet, keep reading
                continue
        if data is None:
            raise ConnectionError(
                f"Connection closed: {self.websocket_client.close_code} {self.websocket_client.close_reason}"
            )
        server_msg.ParseFromString(data)

        if self._need_to_log:
            print("Server message received:\n" + str(server_msg))
        return server_msg
