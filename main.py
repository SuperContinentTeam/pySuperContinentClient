import sys
import multiprocessing

from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow


def start_gui():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


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
