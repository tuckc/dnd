from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

class StatsWindow(QWidget):
	def __init__(self, parent):	
		QTabWidget.__init__(self)
		self.tab_window = parent

	def setup(self):
		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.buttonbox.addWidget(QPushButton('Stats', self), 2, 2, 2, 2)

		self.vbox.addLayout(self.picbox)	
		self.vbox.addLayout(self.buttonbox)	

		self.setFixedSize(600, 600)
		self.setLayout(self.vbox)
		self.show()