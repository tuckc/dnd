
#UserInterface.py
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.append(sys.path[0][:-2]+"races")
##print 'NEW path --------------->', sys.path
import dwarf

class SubraceDwarf(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self)
		self.parent_window = parent
		self.setup()

	def setup(self):
		self.label = QLabel()
		self.label.setText("Choose your subrace here!")
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Dwarf Subrace")
		
		self.dwarfTitle=QLabel()
		self.dwarfTitle.setText("Dwarf")
		self.dwarfDetails =QTextEdit("Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.<br> Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller.<br> Their courage and endurance are also easily a match for any of the larger folk.<br>------------Stats------------<br>Constitution +2<br>Speed:25 Feet<br>Skills:Darkvision, Dwarven Resilience, Dwarven Combat Training, Tool Proficiency, Stonecunning<br>Languages: Dwarvish<br>Subrace: Yes")
		self.dwarfDetails.setReadOnly(True)


		self.hillButton=QRadioButton("Hill Dwarf")
		self.hillButton.setToolTip("As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience.<br>The gold dwarves of Faerun in their mighty southern kingdom are hill dwarves, as are the exiled<br>------------Stats------------<br>All Dwarf Base stats<br>Wisdom +1<br>Skills:Dwarven Toughness")

		self.mountainButton=QRadioButton("Mountain Dwarf")
		self.mountainButton.setToolTip("As a mountain dwarf, you're strong and hardy, accustomed to a difficult life in rugged terrain.<br>------------Stats------------<br>All Dwarf Base stats<br>Strength +2<br>Skills:Dwarven Armor Training")
		
		self.nextButton = QPushButton("Next")
		self.nextButton.setToolTip("Confirm your subrace and select a tool set")
		self.nextButton.clicked.connect(self.close)

		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()


		self.buttongroup = QButtonGroup()
		self.buttongroup.addButton(self.hillButton)
		self.buttongroup.addButton(self.mountainButton)



		

		self.hilllabel = QLabel(self)
		self.hilllabel.resize(self.size()*.25)
		self.mountainlabel = QLabel(self)
		self.mountainlabel.resize(self.size()*.25)

		self.hillpixmap = QPixmap('hilldwarf.jpg').scaled(self.hilllabel.size())
		self.mountainpixmap = QPixmap('mountaindwarf.jpg').scaled(self.mountainlabel.size())

		self.hilllabel.setPixmap(self.hillpixmap)
		self.mountainlabel.setPixmap(self.mountainpixmap)

		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.dwarfTitle)
		self.vbox.addWidget(self.dwarfDetails)
		

		self.picbox.addWidget(self.hilllabel)
		self.picbox.addWidget(self.mountainlabel)

		self.vbox.addLayout(self.picbox)
		

		self.buttonbox.addWidget(self.hillButton)
		self.buttonbox.addWidget(self.mountainButton)


		self.vbox.addLayout(self.buttonbox)
		self.vbox.addWidget(self.nextButton)
		
		
		

		self.setLayout(self.vbox)

		self.show()







	def closeEvent(self,event):
		if self.mountainButton.isChecked():
			self.ptool = PickTool(self,"Mountain Dwarf")
			self.ptool.show()
			event.accept()
		elif self.hillButton.isChecked():
			self.ptool = PickTool(self,"Hill Dwarf")
			self.ptool.show()
			event.accept()
		else:
			self.label.setText("YOU MUST SELECT A SUBRACE TO CONTINUE!")
			event.ignore()



class PickTool(QWidget):
	def __init__(self, parent, race):
		QWidget.__init__(self)
		self.parent = parent
		self.race = race
		self.setWindowTitle("Pick Dwarven Tool Set")
		self.show()
		self.setup()

	def setup(self):
		self.setGeometry(100,100,300,300)
		self.vertbox = QVBoxLayout()
		self.label = QLabel()
		self.label.resize(self.size()*.25)
		self.label.setText("Choose your tools here")
		self.mason = QRadioButton("Mason's Tools")
		self.mason.setToolTip("")
		self.smith = QRadioButton("Smith's Tools")
		self.mason.setToolTip("")
		self.brewer = QRadioButton("Brewer's Supplies")
		self.mason.setToolTip("")

		self.toolButtonGroup = QButtonGroup()
		self.toolButtonGroup.addButton(self.mason)
		self.toolButtonGroup.addButton(self.smith)
		self.toolButtonGroup.addButton(self.brewer)

		self.masonpic = QLabel(self)
		self.masonpic.resize(self.size()*.25)
		self.smithpic = QLabel(self)
		self.smithpic.resize(self.size()*.25)
		self.brewerpic = QLabel(self)
		self.brewerpic.resize(self.size()*.25)

		self.masonpixmap = QPixmap('masontools.jpeg').scaled(self.masonpic.size())
		self.smithpixmap = QPixmap('smithtools.jpeg').scaled(self.smithpic.size())
		self.brewerpixmap = QPixmap('brewersupplies.jpeg').scaled(self.brewerpic.size())

		self.masonpic.setPixmap(self.masonpixmap)
		self.smithpic.setPixmap(self.smithpixmap)
		self.brewerpic.setPixmap(self.brewerpixmap)



		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Confirm your selection and return to race window")
		self.doneButton.clicked.connect(self.close)


		self.setLayout(self.vertbox)
		self.vertbox.addWidget(self.label)
		self.vertbox.addWidget(self.masonpic)
		self.vertbox.addWidget(self.mason)
		self.vertbox.addWidget(self.smithpic)
		self.vertbox.addWidget(self.smith)
		self.vertbox.addWidget(self.brewerpic)
		self.vertbox.addWidget(self.brewer)
		self.vertbox.addWidget(self.doneButton)




	def closeEvent(self,event):
		if self.mason.isChecked():
			if self.race == "Mountain Dwarf":
				self.parent.parent_window.tab_window.main_window.race = dwarf.Dwarf("Mountain Dwarf","Mason's Tools")
				self.parent.parent_window.label.setText("Mountain Dwarf with Mason's Tools")
				#print("Character set to")
				#print(self.parent.parent_window.tab_window.main_window.race)
				event.accept()
			elif self.race == "Hill Dwarf":
				self.parent.parent_window.tab_window.main_window.race = dwarf.Dwarf("Hill Dwarf","Mason's Tools")
				self.parent.parent_window.label.setText("Hill Dwarf with Mason's Tools")
				#print("Character set to")
				#print(self.parent.parent_window.tab_window.main_window.race)
				event.accept()

		elif self.smith.isChecked():
			if self.race == "Mountain Dwarf":
				self.parent.parent_window.tab_window.main_window.race = dwarf.Dwarf("Mountain Dwarf","Smith's Tools")
				self.parent.parent_window.label.setText("Mountain Dwarf with Smith's Tools")
				#print("Character set to")
				#print(self.parent.parent_window.tab_window.main_window.race)
				event.accept()
			elif self.race == "Hill Dwarf":
				self.parent.parent_window.tab_window.main_window.race = dwarf.Dwarf("Hill Dwarf","Smith's Tools")
				self.parent.parent_window.label.setText("Hill Dwarf with Smith's Tools")
				#print("Character set to")
				#print(self.parent.parent_window.tab_window.main_window.race)
				event.accept()


		elif self.brewer.isChecked():
			if self.race == "Mountain Dwarf":
				self.parent.parent_window.tab_window.main_window.race = dwarf.Dwarf("Mountain Dwarf","Brewer's Supplies")
				self.parent.parent_window.label.setText("Mountain Dwarf with Brewer's Supplies")
				#print("Character set to")
				#print(self.parent.parent_window.tab_window.main_window.race)
				event.accept()
			elif self.race == "Hill Dwarf":
				self.parent.parent_window.tab_window.main_window.race = dwarf.Dwarf("Hill Dwarf","Brewer's Supplies")
				self.parent.parent_window.label.setText("Hill Dwarf with Brewer's Supplies")
				#print("Character set to")
				#print(self.parent.parent_window.tab_window.main_window.race)
				event.accept()
		else:
			self.label.setText("YOU MUST SELECT A TOOL SET TO CONTINUE!")
			event.ignore()

		
		






	

if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainmain = QMainWindow()
	main_window = SubraceDwarf(mainmain)
	app.exec_()
