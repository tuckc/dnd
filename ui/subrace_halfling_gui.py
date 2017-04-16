#UserInterface.py
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class DND_CC_Window(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setup()

	def setup(self):
		self.setGeometry(200, 200, 700, 700)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Halfling Subrace")
		
		self.halflingButton=QPushButton("Halfling")
		self.halflingButton.setToolTip("these wanderers love peace, food, hearth, and home, though home might be a wagon jostling along an dirt road or a raft floating downriver.<br>The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense.<br> Standing about 3 feet tall, they appear relatively harmless and so have managed to survive for centuries in the shadow of empires and on the edges of wars and political strife<br>------------Stats------------<br>Dexterity +2<br>Speed:25 Feet<br>Skills:Lucky, Brave, Halfling Nimbleness<br>Languages: Common and Halfling<br>Subrace: Yes")
		
		self.lightfootButton=QPushButton("Lightfoot Halfling")
		self.lightfootButton.setToolTip("As a lightfoot halfling, you can easily hide from notice, even using other people as cover.<br>------------Stats------------<br>All Halfling Base stats<br>Charisma +1<br>Skills:Naturally Stealthy")

		self.stoutButton=QPushButton("Stout Halfling")
		self.stoutButton.setToolTip("As a stout halfling, you're hardier than average and have some resistance to poison.<br>Some say Stouts have Dwarven blood.<br>In the south they are called Stronghearts<br>------------Stats------------<br>All Halfling Base stats<br>Constitution +1<br>Skills:Stout Resilience")
		
			

		self.vbox = QtWidgets.QVBoxLayout()
		self.picbox = QtWidgets.QHBoxLayout()
		self.buttonbox = QtWidgets.QHBoxLayout()

		self.label = QLabel(self)
		self.pixmap = QPixmap('halfling.jpg')
		self.label.setPixmap(self.pixmap)
		self.picbox.addWidget(self.label)

		
		self.buttonbox.addWidget(self.halflingButton)
		self.buttonbox.addWidget(self.lightfootButton)
		self.buttonbox.addWidget(self.stoutButton)
		
		
		

		self.setLayout(self.vbox)
		self.vbox.addLayout(self.picbox)
		self.vbox.addLayout(self.buttonbox)
		self.show()


		self.resize(800, 800)
	

if __name__ == "__main__":
	'''
	Code from slide 15 of lecture 17
	'''
	app = QtWidgets.QApplication(sys.argv)
	main_window = DND_CC_Window()
	app.exec_()
