from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLabel, QLineEdit, QWidget, QPushButton, QApplication

from gui.game.game_state.state import GameState
from utils.settings import TITLE, BASE_DIR


def init_arguments():
    result = {
        "ip": "",
        "port": "",
        "name": ""
    }
    try:
        with open(BASE_DIR.joinpath("cache"), "r", encoding="utf-8") as f:
            lines = f.read().strip().split("\n")
            result["name"] = lines[0].strip()
            result["ip"] = lines[1].strip()
            result["port"] = lines[2].strip()
    except Exception as e:
        _ = e

    return result


def stay_arguments(arguments: dict):
    with open(BASE_DIR.joinpath("cache"), "w", encoding="utf-8") as f:
        f.writelines(arguments["name"] + "\n")
        f.writelines(arguments["ip"] + "\n")
        f.writelines(arguments["port"] + "\n")


class RootSettingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.last_window = self.parent()
        pos = self.last_window.pos()

        self.setWindowTitle(TITLE)
        self.setGeometry(pos.x(), pos.y(), 400, 300)

        self.arguments = init_arguments()

        layout = QGridLayout()

        layout.addWidget(QLabel("联机帝国名"), 0, 0)
        self.name_edit = QLineEdit(self.arguments["name"])
        layout.addWidget(self.name_edit, 0, 1)

        layout.addWidget(QLabel("服务器地址"), 1, 0)
        self.ip_edit = QLineEdit(self.arguments["ip"])
        layout.addWidget(self.ip_edit, 1, 1)

        layout.addWidget(QLabel("服务器端口"), 2, 0)
        self.port_edit = QLineEdit(self.arguments["port"])
        layout.addWidget(self.port_edit, 2, 1)

        btn_submit = QPushButton("确认", self)
        btn_submit.clicked.connect(self.submit)  # type: ignore
        layout.addWidget(btn_submit, 3, 1)

        center_widget = QWidget(self)
        center_widget.setLayout(layout)
        self.setCentralWidget(center_widget)

    def closeEvent(self, a0) -> None:
        QApplication.quit()

    def submit(self):
        self.arguments.update({
            "name": self.name_edit.text().strip(),
            "ip": self.ip_edit.text().strip(),
            "port": self.port_edit.text().strip()
        })
        stay_arguments(self.arguments)
        GameState.arguments = self.arguments
        self.hide()
        self.last_window.show()
