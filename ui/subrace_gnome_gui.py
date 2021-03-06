'''
subrace for gnomes
'''
#UserInterface.py
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.append(sys.path[0][:-2]+"races")

import gnome

class SubraceGnome(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self)
		self.parent_window = parent
		self.setup()

	def setup(self):
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Gnome Subrace")
		self.label = QLabel()
		self.label.setText("Choose your subrace here!")

		self.gnomeTitle=QLabel()
		self.gnomeTitle.setText("Gnome")
		self.gnomeDetails =QTextEdit("Gnomes take delight in life, enjoying every moment of invention, exploration, investigation, creation, and play.<br>Gnomes average slightly over 3 feet tall and weigh 40 to 45 pounds.<br>------------Stats------------<br>Intelligence +2<br>Speed:25 Feet<br>Skills:Darkvision, Gnome Cunning<br>Languages: Common and Gnomish<br>Subrace: Yes")
		self.gnomeDetails.setReadOnly(True)


		self.forestButton=QRadioButton("Forest Gnome")
		self.forestButton.setToolTip("As a forest gnome, you have a natural knack for illusion and inherent quickness and stealth. In the worlds of D&D, forest gnomes are rare and secretive.<br> They gather in hidden communities in sylvan forests, using illusions and trickery to conceal themselves from threats or to mask their escape should they be detected.<br>------------Stats------------<br>All Gnome Base stats<br>Dexterity +1<br>Skills:Natural Illusionist, Speak with Small Beasts")
		self.rockButton=QRadioButton("Rock Gnome")
		self.rockButton.setToolTip("As a rock gnome, you have a natural inventiveness and hardiness beyond that of other gnomes.<br>Most gnomes in the worlds o f D&D are rock gnomes, including the tinker gnomes of the Dragonlance setting.<br>------------Stats------------<br>All Gnome Base stats<br>Constitution +1<br>Skills:Artificer's Lore, Tinker")
		
		
		
		


		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.buttongroup = QButtonGroup()
		self.buttongroup.addButton(self.forestButton)
		self.buttongroup.addButton(self.rockButton)

		self.pic1label = QLabel(self)
		self.pic1label.resize(self.size()*.25)
		self.pic2label = QLabel(self)
		self.pic2label.resize(self.size()*.25)
		
		self.db1pixmap = QPixmap('forestgnome.jpg').scaled(self.pic1label.size())
		self.db2pixmap = QPixmap('rockgnome.jpg').scaled(self.pic2label.size())

		self.pic1label.setPixmap(self.db1pixmap)	#hilllabel= pic1
		self.pic2label.setPixmap(self.db2pixmap)#mountainlable=pic2

		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.gnomeTitle)
		self.vbox.addWidget(self.gnomeDetails)
		

		self.picbox.addWidget(self.pic1label)
		self.picbox.addWidget(self.pic2label)

		self.vbox.addLayout(self.picbox)
		

		self.buttonbox.addWidget(self.forestButton)
		self.buttonbox.addWidget(self.rockButton)
		

		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Confirm your subrace selection and close this window")
		self.doneButton.clicked.connect(self.close)


		self.vbox.addLayout(self.buttonbox)
		self.vbox.addWidget(self.doneButton)
				
		self.setLayout(self.vbox)

		self.show()



	def closeEvent(self,event):
		if self.forestButton.isChecked():
			self.parent_window.tab_window.main_window.race = gnome.Gnome("Forest Gnome")
			self.parent_window.label.setText("Forest Gnome")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.rockButton.isChecked():
			self.parent_window.tab_window.main_window.race = gnome.Gnome("Rock Gnome")
			self.parent_window.label.setText("Rock Gnome")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		else:
			self.label.setText("YOU MUST SELECT A SUBRACE TO CONTINUE!")
			event.ignore()
		
			



	


if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainmain = QMainWindow()
	main_window = SubraceGnome(mainmain)
	app.exec_()
