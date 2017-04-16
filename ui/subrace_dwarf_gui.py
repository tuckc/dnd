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
		self.setWindowTitle("Dungeons and Dragons Character Creator: Dwarf Subrace")
		
		self.dwarfButton=QPushButton("Dwarf")
		self.dwarfButton.setToolTip("Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.<br> Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller.<br> Their courage and endurance are also easily a match for any of the larger folk.<br>------------Stats------------<br>Constitution +2<br>Speed:25 Feet<br>Skills:Darkvision, Dwarven Resilience, Dwarven Combat Training, Tool Proficiency, Stonecunning<br>Languages: Dwarvish<br>Subrace: Yes")
		
		self.hillButton=QPushButton("Hill Dwarf")
		self.hillButton.setToolTip("As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience.<br>The gold dwarves of Faerun in their mighty southern kingdom are hill dwarves, as are the exiled<br>------------Stats------------<br>All Dwarf Base stats<br>Wisdom +1<br>Skills:Dwarven Toughness")

		self.mountainButton=QPushButton("Mountain Dwarf")
		self.mountainButton.setToolTip("As a mountain dwarf, you're strong and hardy, accustomed to a difficult life in rugged terrain.<br>------------Stats------------<br>All Dwarf Base stats<br>Strength +2<br>Skills:Dwarven Armor Training")
		
			

		self.vbox = QtWidgets.QVBoxLayout()
		self.picbox = QtWidgets.QHBoxLayout()
		self.buttonbox = QtWidgets.QHBoxLayout()

		self.label = QLabel(self)
		self.pixmap = QPixmap('dwarf.jpg')
		self.label.setPixmap(self.pixmap)
		self.picbox.addWidget(self.label)

		
		self.buttonbox.addWidget(self.dwarfButton)
		self.buttonbox.addWidget(self.hillButton)
		self.buttonbox.addWidget(self.mountainButton)
		
		
		

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
