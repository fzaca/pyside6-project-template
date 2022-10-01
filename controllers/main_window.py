from PySide6.QtWidgets import QWidget

from views.ui_main_window import MainWindow

class MainWindowForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.num1_button.clicked.connect(self.hello)

    def hello(self):
        print('Hello World')