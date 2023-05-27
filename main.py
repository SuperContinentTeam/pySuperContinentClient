import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor
# from gui.start_window import StartWindow
from gui.game.main_panel import MainGamePanel


def start_gui():
    try:
        app = QApplication(sys.argv)
        # start_window = StartWindow()
        arguments = {'activeAiModel': False,
                     'aiCount': 0,
                     'aiModelPath': '',
                     'empireColor': QColor(255, 0, 0),
                     'empireName': '',
                     'resourceRatio': 1,
                     'worldSize': 10}
        start_window = MainGamePanel(arguments=arguments)
        start_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start_gui()

# def start_queue(pipe):
#     while True:
#         command = pipe.recv()
#         print("Command: ", command)
#
#         if command == "quit":
#             return


# if __name__ == '__main__':
#     queue_recv_pipe, queue_emit_pipe = multiprocessing.Pipe()
#     ws_pipe = multiprocessing.Pipe()
#
#     p1 = multiprocessing.Process(target=start_queue, args=(queue_recv_pipe,))
#     p2 = multiprocessing.Process(target=start_gui, args=(queue_emit_pipe,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()



