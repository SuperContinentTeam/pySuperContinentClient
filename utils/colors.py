from PyQt6.QtGui import QColor

RED = QColor(255, 0, 0)
GREEN = QColor(0, 255, 0)
BLUE = QColor(0, 0, 255)
BLACK = QColor(0, 0, 0)
WHITE = QColor(255, 255, 255)

DIM_GREY = QColor(105, 105, 105)

# 无色
COLOR_LESS = QColor(0, 0, 0, 0)

TechnologyColor = {
    "economy": QColor(0, 255, 127),  # 科技: 经济领域指定颜色
    "military": QColor(0, 191, 255),  # 科技: 军工领域指定颜色
    "beyond": QColor(255, 215, 0)  # 科技: 超越领域指定颜色
}

EnvironmentColor = {
    -2: QColor(255, 105, 180),  # 地块环境: 死寂
    -1: QColor(255, 165, 0),  # 地块环境: 恶劣
    0: QColor(0, 255, 255),  # 地块环境: 一般
    1: QColor(100, 149, 237),  # 地块环境: 优秀
    2: QColor(0, 255, 127),  # 地块环境: 理想
}
