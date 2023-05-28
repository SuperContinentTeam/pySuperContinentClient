from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QListView, QAbstractItemView

from utils.size import SCHEDULE_LEFT, SCHEDULE_TOP, SCHEDULE_WIDTH, SCHEDULE_HEIGHT


class SchedulePanel(QListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(
            SCHEDULE_LEFT,
            SCHEDULE_TOP,
            SCHEDULE_WIDTH,
            SCHEDULE_HEIGHT
        )
        self.setViewMode(QListView.ViewMode.ListMode)
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)

        self.setModel(QStringListModel([str(i) for i in range(50)]))

    def mouseReleaseEvent(self, e) -> None:
        print("Click in Schedule")
