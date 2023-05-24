# from PyQt5.QtCore import QTimer
from pprint import pprint
from PyQt5 import QtGui
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtCore import Qt, QEvent, QRegExp
from PyQt5.QtWidgets import (
    QMainWindow, QGridLayout, QPushButton, QLabel, QWidget, QLineEdit,
    QSlider, QComboBox, QColorDialog, QFontDialog, QDialog, QMessageBox
)

from utils.settings import TITLE

class PasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI() 

    def initUI(self):
        self.resize(350,100)
        self.setWindowTitle("密码输入框")

        self.lb = QLabel("请输入密码：",self)

        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)

        self.bt1 = QPushButton("确定",self)
        self.bt2 = QPushButton("取消",self)
   
        #怎么布局在布局篇介绍过，这里代码省略...

        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText("密码6-15位，只能有数字和字母，必须以字母开头")
        self.edit.setEchoMode(QLineEdit.Password)

        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validator)

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)

    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)
    
    def Ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            self.done(1)          # 结束对话框返回1

    def Cancel(self):
        self.done(0) 

class SingleSettingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.last_window = self.parent()
        pos = self.last_window.pos()

        self.setWindowTitle(TITLE)
        self.setGeometry(pos.x(), pos.y(), 400, 300)

        self.argumensts = {
            "worldSize": 10,
            "aiCount": 0,
            "resourceRatio": 1,
            "empireName": "",
            "empireColor": None
        }

        layout = QGridLayout()

        layout.addWidget(QLabel("世界宽度"), 0, 0)
        self.combo_box_world_size = QComboBox()
        self.combo_box_world_size.addItem("10x10", "10")
        self.combo_box_world_size.addItem("20x20", "20")
        self.combo_box_world_size.addItem("30x30", "30")
        self.combo_box_world_size.setCurrentIndex(0)
        self.combo_box_world_size.activated.connect(self.select_world_size_change_value)
        layout.addWidget(self.combo_box_world_size, 0, 1)

        layout.addWidget(QLabel("AI数量"), 1, 0)
        self.slider_ai_count = QSlider(Qt.Horizontal)
        self.slider_ai_count.setMinimum(1)
        self.slider_ai_count.setMaximum(4)
        self.slider_ai_count.valueChanged.connect(self.slider_ai_count_change_value)
        layout.addWidget(self.slider_ai_count, 1, 1)
        self.label_ai_count = QLabel(f"{self.slider_ai_count.value()} (未启用)")
        layout.addWidget(self.label_ai_count, 1, 2)

        self.combo_box_resource = QComboBox()
        self.combo_box_resource.addItem("贫瘠", "0")
        self.combo_box_resource.addItem("默认", "1")
        self.combo_box_resource.addItem("富饶", "2")
        self.combo_box_resource.setCurrentIndex(1)
        self.combo_box_resource.activated.connect(self.select_resource_ratio)
        layout.addWidget(QLabel("资源比例"), 2, 0)
        layout.addWidget(self.combo_box_resource, 2, 1)

        self.line_edit_empire_name = QLineEdit("")
        layout.addWidget(QLabel("国家名称"), 3, 0)
        layout.addWidget(self.line_edit_empire_name, 3, 1)

        layout.addWidget(QLabel("国家主色"), 4, 0)
        self.btn_empire_color = QPushButton(self)
        self.btn_empire_color.setStyleSheet("background-color: white; border-radius: 2px")
        self.btn_empire_color.clicked.connect(self.click_select_color)
        layout.addWidget(self.btn_empire_color, 4, 1)

        layout.addWidget(QLabel("启用AI"), 5, 0)
        layout.addWidget(QLineEdit(""), 5, 1)
        layout.addWidget(QLabel("(未启用)"), 5, 2)
        layout.addWidget(QLabel("导入AI模型"), 6, 0)
        layout.addWidget(QLineEdit(""), 6, 1)
        layout.addWidget(QPushButton("打开文件", self), 6, 2)

        btn_back = QPushButton("返回", self)
        btn_back.clicked.connect(self.close_window)
        layout.addWidget(btn_back, 7, 2)

        btn_start = QPushButton("开始", self)
        btn_start.clicked.connect(self.click_game_start)
        layout.addWidget(btn_start, 8, 2)

        center_widget = QWidget(self)
        center_widget.setLayout(layout)
        self.setCentralWidget(center_widget)

    def select_resource_ratio(self):
        self.argumensts["resourceRatio"] = int(self.combo_box_resource.currentData())

    def select_world_size_change_value(self):
        self.argumensts["worldSize"] = int(self.combo_box_world_size.currentData())

    def click_select_color(self):
        # color: QtGui.QColor = QColorDialog.getColor()
        # if color.isValid():
        #     self.btn_empire_color.setStyleSheet(f"background-color: {color.name()}")
        ...

    def slider_ai_count_change_value(self):
        value = self.slider_ai_count.value()
        self.label_ai_count.setText(f"{value} (未启用)")
        self.argumensts["aiCount"] = value

    def click_game_start(self):
        pprint(self.argumensts)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.last_window.show()

        return super().closeEvent(a0)
    
    def close_window(self):
        self.close()
