import orjson as orjson
from PyQt6.QtCore import QThread, QUrl, pyqtSignal, QByteArray, QTimer
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
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.test_send_msg)  # type: ignore
        self.timer.start(1000)

    def test_send_msg(self):
        data = {
            "op": "test",
            "content": "hello"
        }
        self.client.sendBinaryMessage(QByteArray(orjson.dumps(data)))

    def received(self, message: QByteArray):
        self.message_received.emit(message.data())  # type: ignore

    def on_connected(self):
        print("Connected to WebSocket server")
        meta_data = {
            "op": "join",
            "name": self.state.name
        }
        self.client.sendBinaryMessage(QByteArray(orjson.dumps(meta_data)))
