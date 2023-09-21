from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QGridLayout, QPushButton, QLabel, QWidget, QLineEdit,
    QSlider, QComboBox, QColorDialog, QCheckBox, QApplication
)

from gui.game.main_panel import MainGamePanel
from utils.colors import BLACK
from utils.settings import TITLE


class SingleSettingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.last_window = self.parent()
        pos = self.last_window.pos()

        self.setWindowTitle(TITLE)
        self.setGeometry(pos.x(), pos.y(), 400, 300)

        self.arguments = {
            "worldSize": 10,
            "aiCount": 0,
            "resourceRatio": 1,
            "empireName": "",
            "empireColor": BLACK,
            "activeAiModel": False,
            "aiModelPath": ""
        }

        layout = QGridLayout()

        layout.addWidget(QLabel("世界宽度"), 0, 0)
        self.combo_box_world_size = QComboBox()
        self.combo_box_world_size.addItem("10x10", "10")
        self.combo_box_world_size.addItem("20x20", "20")
        self.combo_box_world_size.addItem("30x30", "30")
        self.combo_box_world_size.setCurrentIndex(0)
        self.combo_box_world_size.activated.connect(self.select_world_size_change_value)  # type: ignore
        layout.addWidget(self.combo_box_world_size, 0, 1)

        layout.addWidget(QLabel("AI数量"), 1, 0)
        self.slider_ai_count = QSlider(Qt.Orientation.Horizontal)
        self.slider_ai_count.setMinimum(0)
        self.slider_ai_count.setMaximum(20)
        self.slider_ai_count.valueChanged.connect(self.slider_ai_count_change_value)  # type: ignore
        layout.addWidget(self.slider_ai_count, 1, 1)
        self.label_ai_count = QLabel(f"{self.slider_ai_count.value()} (该功能未启用)")
        layout.addWidget(self.label_ai_count, 1, 2)

        self.combo_box_resource = QComboBox()
        self.combo_box_resource.addItem("贫瘠", "0")
        self.combo_box_resource.addItem("默认", "1")
        self.combo_box_resource.addItem("富饶", "2")
        self.combo_box_resource.setCurrentIndex(1)
        self.combo_box_resource.activated.connect(self.select_resource_ratio)  # type: ignore
        layout.addWidget(QLabel("资源比例"), 2, 0)
        layout.addWidget(self.combo_box_resource, 2, 1)

        self.line_edit_empire_name = QLineEdit("")
        layout.addWidget(QLabel("国家名称"), 3, 0)
        layout.addWidget(self.line_edit_empire_name, 3, 1)

        layout.addWidget(QLabel("国家主色"), 4, 0)
        self.btn_empire_color = QPushButton(self)
        self.btn_empire_color.setStyleSheet(f"background-color: black; border-radius: 1px")
        self.btn_empire_color.clicked.connect(self.click_select_color)  # type: ignore
        layout.addWidget(self.btn_empire_color, 4, 1)

        layout.addWidget(QLabel("启用AI"), 5, 0)
        self.check_box_active_ai = QCheckBox()
        self.check_box_active_ai.stateChanged.connect(self.active_ai_mode)  # type: ignore
        layout.addWidget(self.check_box_active_ai, 5, 1)
        layout.addWidget(QLabel("(该功能未启用)"), 5, 2)

        layout.addWidget(QLabel("导入AI模型"), 6, 0)
        layout.addWidget(QLineEdit(""), 6, 1)
        layout.addWidget(QPushButton("打开文件", self), 6, 2)

        btn_back = QPushButton("返回", self)
        btn_back.clicked.connect(self.close_window)  # type: ignore
        layout.addWidget(btn_back, 7, 2)

        btn_start = QPushButton("开始游戏", self)
        btn_start.clicked.connect(self.click_game_start)  # type: ignore
        layout.addWidget(btn_start, 8, 2)

        center_widget = QWidget(self)
        center_widget.setLayout(layout)
        self.setCentralWidget(center_widget)

    def active_ai_mode(self):
        print(self.check_box_active_ai.isChecked())

    def select_resource_ratio(self):
        self.arguments["resourceRatio"] = int(self.combo_box_resource.currentData())

    def select_world_size_change_value(self):
        self.arguments["worldSize"] = int(self.combo_box_world_size.currentData())

    def click_select_color(self):
        color = QColorDialog.getColor(parent=self)
        if color.isValid():
            self.btn_empire_color.setStyleSheet(f"background-color: {color.name()}; border-radius: 1px")
            self.arguments["empireColor"] = color

    def slider_ai_count_change_value(self):
        value = self.slider_ai_count.value()
        self.label_ai_count.setText(f"{value} (该功能未启用)")
        self.arguments["aiCount"] = value

    def click_game_start(self):
        self.hide()
        self.last_window.close()
        temp = MainGamePanel(parent=self.last_window, arguments=self.arguments)
        temp.show()

    def closeEvent(self, a0) -> None:
        QApplication.quit()

    def close_window(self):
        self.hide()
        self.last_window.show()
