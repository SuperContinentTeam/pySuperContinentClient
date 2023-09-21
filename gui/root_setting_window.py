from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLabel, QLineEdit, QWidget, QPushButton, QApplication

from utils.settings import TITLE


class RootSettingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.last_window = self.parent()
        pos = self.last_window.pos()

        self.setWindowTitle(TITLE)
        self.setGeometry(pos.x(), pos.y(), 400, 300)

        self.arguments = {
            "ip": "",
            "port": "",
            "name": ""
        }

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
        self.hide()
        self.last_window.show()
