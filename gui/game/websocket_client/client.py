import orjson as orjson
from PyQt6.QtCore import QThread, QUrl, pyqtSignal, QByteArray
from PyQt6.QtWebSockets import QWebSocket

from gui.game.game_state.state import State


def on_disconnected():
    print("Disconnected from WebSocket server")


class WSClientThread(QThread):
    state = State({"name": "Axious"})
    message_received = pyqtSignal(bytes)

    def __init__(self, server_uri):
        super().__init__()
        self.client = QWebSocket()
        self.client.connected.connect(self.on_connected)  # type: ignore
        self.client.disconnected.connect(on_disconnected)  # type: ignore
        self.client.binaryMessageReceived.connect(self.received)  # type: ignore

        self.server_uri = server_uri
        self.client.open(QUrl(self.server_uri))

    def received(self, message: QByteArray):
        self.message_received.emit(message.data())  # type: ignore

    def on_connected(self):
        print("Connected to WebSocket server")
        meta_data = {
            "op": "join",
            "name": "axious",
            "room": "A"
        }
        self.client.sendBinaryMessage(QByteArray(orjson.dumps(meta_data)))
