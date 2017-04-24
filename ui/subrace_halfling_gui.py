'''
subrace for halflings
'''
#UserInterface.py
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.append(sys.path[0][:-2]+"races")

import halfling

class SubraceHalfling(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self)
		self.parent_window = parent
		self.label = QLabel()
		self.label.setText("Choose your subrace here!")
		self.setup()

	def setup(self):
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Halfling Subrace")
		
		self.halflingTitle=QLabel()
		self.halflingTitle.setText("Halfling")
		self.halflingDetails =QTextEdit("these wanderers love peace, food, hearth, and home, though home might be a wagon jostling along an dirt road or a raft floating downriver.<br>The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense.<br> Standing about 3 feet tall, they appear relatively harmless and so have managed to survive for centuries in the shadow of empires and on the edges of wars and political strife<br>------------Stats------------<br>Dexterity +2<br>Speed:25 Feet<br>Skills:Lucky, Brave, Halfling Nimbleness<br>Languages: Common and Halfling<br>Subrace: Yes")
		self.halflingDetails.setReadOnly(True)


		self.lightfootButton=QRadioButton("Lightfoot Halfling")
		self.lightfootButton.setToolTip("As a lightfoot halfling, you can easily hide from notice, even using other people as cover.<br>------------Stats------------<br>All Halfling Base stats<br>Charisma +1<br>Skills:Naturally Stealthy")
		
		self.stoutButton=QRadioButton("Stout Halfling")
		self.stoutButton.setToolTip("As a stout halfling, you're hardier than average and have some resistance to poison.<br>Some say Stouts have Dwarven blood.<br>In the south they are called Stronghearts<br>------------Stats------------<br>All Halfling Base stats<br>Constitution +1<br>Skills:Stout Resilience")
		
		
		
	

		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.buttongroup = QButtonGroup()
		self.buttongroup.addButton(self.lightfootButton)
		self.buttongroup.addButton(self.stoutButton)
		


		self.pic1label = QLabel(self)
		self.pic1label.resize(self.size()*.25)
		self.pic2label = QLabel(self)
		self.pic2label.resize(self.size()*.25)
		
		self.db1pixmap = QPixmap('lightfoot.jpg').scaled(self.pic1label.size())
		self.db2pixmap = QPixmap('stout.jpg').scaled(self.pic2label.size())

		self.pic1label.setPixmap(self.db1pixmap)	#hilllabel= pic1
		self.pic2label.setPixmap(self.db2pixmap)#mountainlable=pic2


		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.halflingTitle)
		self.vbox.addWidget(self.halflingDetails)
		

		self.picbox.addWidget(self.pic1label)
		self.picbox.addWidget(self.pic2label)

		self.vbox.addLayout(self.picbox)
		

		self.buttonbox.addWidget(self.lightfootButton)
		self.buttonbox.addWidget(self.stoutButton)
		
		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Confirm your subrace selection and close this window")
		self.doneButton.clicked.connect(self.close)


		self.vbox.addLayout(self.buttonbox)
		self.vbox.addWidget(self.doneButton)
				
		self.setLayout(self.vbox)

		self.show()



	def closeEvent(self,event):
		if self.lightfootButton.isChecked():
			self.parent_window.tab_window.main_window.race = halfling.Halfling("Lightfoot Halfling")
			self.parent_window.label.setText("Lightfoot Halfling")
			#print("Character now ")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.stoutButton.isChecked():
			self.parent_window.tab_window.main_window.race = halfling.Halfling("Stout Halfling")
			self.parent_window.label.setText("Stout Halfling")
			#print("Character now ")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		
		else:
			self.label.setText("YOU MUST SELECT A SUBRACE TO CONTINUE!")
			event.ignore()

		


if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainmain = QMainWindow()
	main_window = SubraceHalfling(mainmain)
	app.exec_()
