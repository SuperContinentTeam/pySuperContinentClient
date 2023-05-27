from functools import lru_cache

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from utils.settings import IMAGE_DIR

# 文字左对齐
FLAG_ALIGN_LEFT = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
# 文字居中
FLAG_ALIGN_CENTER = Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter


@lru_cache
def image(name):
    return QPixmap(str(IMAGE_DIR.joinpath(f"{name}.png")))


def format_number(number, monthly=False):
    abs_number = abs(number)
    pre = "-" if number < 0 else ("+" if monthly else "")

    if abs_number < 1000:
        result = abs_number
    elif 1000 <= abs_number < 1000000:
        result = str(round(abs_number / 1000, 2)) + "K"
    elif 1000000 <= abs_number < 1000000000:
        result = str(round(abs_number / 1000000, 2)) + "M"
    elif 1000000000 <= abs_number < 1000000000000:
        result = str(round(abs_number / 1000000000, 2)) + "G"
    else:
        result = "MAX"

    return f"{pre}{result}"
