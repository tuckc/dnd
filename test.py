import sys
from PyQt5 import QtWidgets, QtCore

class CharacterCreatorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup()
    
    def setup(self):
        self.setWindowTitle('Character Creator')
        self.tab_widget = TabView()
        self.setCentralWidget(self.tab_widget)
        self.show()

class TabView(QtWidgets.QTabWidget):
    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)
        self.setup()

    def setup(self):
        self.addTab(Information(), 'YEAH')
        self.addTab(QtWidgets.QWidget(self), 'NAW')

class Information(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)
        self.setup()

    def setup(self):
        self.setFixedSize(700, 460)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(QtWidgets.QRadioButton('One', self), 1, 1, 1, 1)
        self.layout.addWidget(QtWidgets.QRadioButton('Two', self), 2, 2, 1, 1)
        self.layout.addWidget(QtWidgets.QRadioButton('Three', self), 3, 3, 1, 1)
        self.layout.addWidget(QtWidgets.QRadioButton('Four', self), 4, 4, 1, 1)


app = QtWidgets.QApplication(sys.argv)
main_window = CharacterCreatorWindow()
app.setStyle('Fusion')
app.exec_()