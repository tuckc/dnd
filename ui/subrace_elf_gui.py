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
		self.setWindowTitle("Dungeons and Dragons Character Creator: Elf Subrace")
		
		self.elfButton=QPushButton("Elf")
		self.elfButton.setToolTip("Elves love nature and magic, art and artistry, music and poetry, and the good things of the world.<br>With their unearthly grace and fine features, elves appear hauntingly beautiful to humans and members of many other races.<br>------------Stats------------<br>Dexterity +2<br>Speed:30 Feet<br>Skills:Darkvision, Keen Senses, Fey Ancestry, Trance<br>Languages: Common and Elvish<br>Subrace: Yes")
		
		self.highButton=QPushButton("High Elf")
		self.highButton.setToolTip("As a high elf, you have a keen mind and a mastery of at least the basics of magic<br>------------Stats------------<br>All Elf Base stats<br>Intellignece +1<br>Skills:Elf Weapon Training, Cantrip, Extra Language")

		self.woodButton=QPushButton("Wood Elf")
		self.woodButton.setToolTip("As a wood elf, you have keen senses and intuition, and your fleet feet carry you quickly and stealthily through your native forests.<br>------------Stats------------<br>All Elf Base stats<br>Wisdom +1<br>Skills:Elf Weapon Training, Fleet of Foot, Mask of the Wild")

		self.darkButton=QPushButton("Dark Elf")
		self.darkButton.setToolTip("Descended from an earlier subrace of dark-skinned elves, the drow were banished from the surface world for following the goddess Lolth down the path to evil and corruption.<br> Now they have built their own civilization in the depths of the Underdark, patterned after the Way of Lolth<br>------------Stats------------<br>All Elf Base stats<br>Charisma +1<br>Skills:Superior Darkvision, Sunlight Sensitivity, Drow Magic, Drow Weapon Training")
		
			

		self.vbox = QtWidgets.QVBoxLayout()
		self.picbox = QtWidgets.QHBoxLayout()
		self.buttonbox = QtWidgets.QHBoxLayout()

		self.label = QLabel(self)
		self.pixmap = QPixmap('elf.jpg')
		self.label.setPixmap(self.pixmap)
		self.picbox.addWidget(self.label)

		
		self.buttonbox.addWidget(self.elfButton)
		self.buttonbox.addWidget(self.highButton)
		self.buttonbox.addWidget(self.woodButton)
		self.buttonbox.addWidget(self.darkButton)
		
		
		

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
