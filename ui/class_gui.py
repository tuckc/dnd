from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

class ClassWindow(QWidget):
	def __init__(self, parent):	
		QTabWidget.__init__(self)
		self.tab_window = parent

	def setup(self):
		self.setFixedSize(700, 460)
		self.layout = QGridLayout()
		self.setLayout(self.layout)
		self.layout.addWidget(QPushButton('Classes', self), 2, 2, 2, 2)
		self.show()