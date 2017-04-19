from __future__ import print_function

from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import json
import sys
sys.path.append(sys.path[0][:-3])
jf = open('../spells.json')
jsonobject = json.load(jf)


class ButtonScrollBar(QWidget):
	def __init__(self,parent):
		QWidget.__init__(self)
		
		self.parent = parent
		self.setGeometry(0,0,parent.width()-100, parent.height()-100)
		self.layout = QVBoxLayout(self)
		self.scrollArea = QScrollArea(self)
		self.layout.addWidget(self.scrollArea)
		self.scrollButtons = QButtonGroup()
		self.setLayout(self.layout)

		self.init_scroll("Cantrip",u"Wizard")
		self.show()
		

	def init_scroll(self,level,jsclass):
		for each in jsonobject:
			if each['level'] == level and each['class'].find(jsclass) > -1:
				newbutton = QRadioButton(each['name'])
				newbutton.setToolTip(each['desc'])
				'''print(each['name'])
				print(each['desc'])
				print(each['class'])
				print(each['level'])
				print('\n'*4)'''
				self.scrollButtons.addButton(newbutton)
				self.layout.addWidget(newbutton)




class Main(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setGeometry(200, 200, 700, 700)
		self.setWindowTitle("Button scroll test")
		self.setup()

	def setup(self):
		self.main_wind = ButtonScrollBar(self)
		self.setCentralWidget(self.main_wind)
		self.show()
		print("In main window")

if __name__ == "__main__":

	app = QApplication(sys.argv)
	starthere = Main()
	app.exec_()

