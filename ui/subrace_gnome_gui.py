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
		self.setWindowTitle("Dungeons and Dragons Character Creator")
		
		self.gnomeButton=QPushButton("Gnome")
		self.gnomeButton.setToolTip("Gnomes take delight in life, enjoying every moment of invention, exploration, investigation, creation, and play.<br>Gnomes average slightly over 3 feet tall and weigh 40 to 45 pounds.<br>------------Stats------------<br>Intelligence +2<br>Speed:25 Feet<br>Skills:Darkvision, Gnome Cunning<br>Languages: Common and Gnomish<br>Subrace: Yes")
		
		self.forestButton=QPushButton("Forest Gnome")
		self.forestButton.setToolTip("As a forest gnome, you have a natural knack for illusion and inherent quickness and stealth. In the worlds of D&D, forest gnomes are rare and secretive.<br> They gather in hidden communities in sylvan forests, using illusions and trickery to conceal themselves from threats or to mask their escape should they be detected.<br>------------Stats------------<br>All Gnome Base stats<br>Dexterity +1<br>Skills:Natural Illusionist, Speak with Small Beasts")

		self.rockButton=QPushButton("Rock Gnome")
		self.rockButton.setToolTip("As a rock gnome, you have a natural inventiveness and hardiness beyond that of other gnomes.<br>Most gnomes in the worlds o f D&D are rock gnomes, including the tinker gnomes of the Dragonlance setting.<br>------------Stats------------<br>All Gnome Base stats<br>Constitution +1<br>Skills:Artificer's Lore, Tinker")
		
			

		self.vbox = QtWidgets.QVBoxLayout()
		self.picbox = QtWidgets.QHBoxLayout()
		self.buttonbox = QtWidgets.QHBoxLayout()

		self.label = QLabel(self)
		self.pixmap = QPixmap('gnome3.jpg')
		self.label.setPixmap(self.pixmap)
		self.picbox.addWidget(self.label)

		
		self.buttonbox.addWidget(self.gnomeButton)
		self.buttonbox.addWidget(self.forestButton)
		self.buttonbox.addWidget(self.rockButton)
		
		
		

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
