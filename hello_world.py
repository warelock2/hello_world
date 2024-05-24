import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello!")
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        hello_action = QAction("Say &Hello",self,)
        hello_action.setStatusTip("Say Hello")
        hello_action.triggered.connect(self.onHelloActionClick)
        hello_action.setCheckable(True)
        hello_action.setShortcut(QKeySequence("Ctrl+h"))

        quit_action = QAction("E&xit",self,)
        quit_action.setStatusTip("End the program")
        quit_action.triggered.connect(self.quit)
        quit_action.setShortcut(QKeySequence("Ctrl+Shift+x"))

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(hello_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

    def onHelloActionClick(self, s):
        if s:
            self.label.setText("Hello, World!")
        else:
            self.label.setText("")

    def quit(self):
        # Perform any additional cleanup actions here
        sys.exit()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
