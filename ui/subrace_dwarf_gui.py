'''
fix radiobutton isSelected at end
'''
#UserInterface.py
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.append(sys.path[0][:-2]+"races")
#print 'NEW path --------------->', sys.path
import dwarf

class SubraceDwarf(QtWidgets.QWidget):
	def __init__(self, parent):
		QtWidgets.QWidget.__init__(self)
		self.parent_window = parent
		self.setup()

	def setup(self):
		self.setGeometry(200, 200, 700, 700)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Dwarf Subrace")
		
		self.dwarfTitle=QLabel()
		self.dwarfTitle.setText("Dwarf")
		self.dwarfDetails =QTextEdit("Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.<br> Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller.<br> Their courage and endurance are also easily a match for any of the larger folk.<br>------------Stats------------<br>Constitution +2<br>Speed:25 Feet<br>Skills:Darkvision, Dwarven Resilience, Dwarven Combat Training, Tool Proficiency, Stonecunning<br>Languages: Dwarvish<br>Subrace: Yes")
		self.dwarfDetails.setReadOnly(True)


		self.hillButton=QRadioButton("Hill Dwarf")
		self.hillButton.setToolTip("As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience.<br>The gold dwarves of Faerun in their mighty southern kingdom are hill dwarves, as are the exiled<br>------------Stats------------<br>All Dwarf Base stats<br>Wisdom +1<br>Skills:Dwarven Toughness")

		self.mountainButton=QRadioButton("Mountain Dwarf")
		self.mountainButton.setToolTip("As a mountain dwarf, you're strong and hardy, accustomed to a difficult life in rugged terrain.<br>------------Stats------------<br>All Dwarf Base stats<br>Strength +2<br>Skills:Dwarven Armor Training")
		
		
		#self.addButton(self.dwarfButton)
		#self.addButton(self.hillButton)
		#self.addButton(self.mountainButton)

		self.vbox = QtWidgets.QVBoxLayout()
		self.picbox = QtWidgets.QHBoxLayout()
		self.buttonbox = QtWidgets.QHBoxLayout()

		#self.picbox = QtWidgets.QHBoxLayout()
		self.buttongroup = QtWidgets.QButtonGroup()
		#self.buttongroup.addButton(self.dwarfButton)
		self.buttongroup.addButton(self.hillButton)
		self.buttongroup.addButton(self.mountainButton)

		#self.vbox.addWidget(self.buttongroup)

		#self.dwarflabel = QLabel(self)
		self.hilllabel = QLabel(self)
		self.hilllabel.resize(self.size()*.25)
		self.mountainlabel = QLabel(self)
		self.mountainlabel.resize(self.size()*.25)

		#self.dwarfpixmap = QPixmap('dwarf.jpg')
		self.hillpixmap = QPixmap('hilldwarf.jpg').scaled(self.hilllabel.size())
		self.mountainpixmap = QPixmap('mountaindwarf.jpg').scaled(self.mountainlabel.size())

		#self.dwarflabel.setPixmap(self.dwarfpixmap)
		self.hilllabel.setPixmap(self.hillpixmap)
		self.mountainlabel.setPixmap(self.mountainpixmap)

		#self.vbox.addWidget(self.dwarflabel)
		self.vbox.addWidget(self.dwarfTitle)
		self.vbox.addWidget(self.dwarfDetails)
		

		self.picbox.addWidget(self.hilllabel)
		self.picbox.addWidget(self.mountainlabel)

		self.vbox.addLayout(self.picbox)
		

		self.buttonbox.addWidget(self.hillButton)
		self.buttonbox.addWidget(self.mountainButton)

		self.vbox.addLayout(self.buttonbox)
		
		
		

		self.setLayout(self.vbox)
		#self.vbox.addLayout(self.picbox)
		#self.vbox.addLayout(self.buttonbox)
		self.show()



		self.resize(800, 800)

	def closeEvent(self,event):
		if self.mountainButton.isSelected():
			self.parent_window.tab_window.main_window.race = dwarf.Dwarf("Mountain Dwarf",pickTool(self, self.parent_window))
		elif self.hillButton.isSelected():
			self.parent_window.tab_window.main_window.race = dwarf.Dwarf("Hill Dwarf", pickTool(self,self.parent_window))
		else:
			print("No sub-race selected")


class pickTool(QtWidgets.QWidget):
	def __init__(self,parent):
		QtWidgets.QWidget.__init__(self)
		self.setWindowTitle("Pick Dwarven Tool")
		self.parent = parent
		self.show()
		self.setup()

	def setup(self):
		self.setGeometry(100,100,500,500)
		self.label = QLabel()
		self.label.setText("List the 3 kinds of tools here")
		#use radiobuttons

	def closeEvent(self,event):
		pass
		#pass the tool choice back into the parent

	

if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	mainmain = QtWidgets.QMainWindow()
	main_window = SubraceDwarf(mainmain)
	app.exec_()
