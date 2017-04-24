'''
Languages for Humans
'''
#UserInterface.py
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.append(sys.path[0][:-2]+"races")

import human

class LanguageHuman(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self)
		self.parent_window = parent
		self.label = QLabel()
		self.label.setText("Choose your language here!")
		self.setup()

	def setup(self):
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Human Language")
		
		self.humanTitle=QLabel()
		self.humanTitle.setText("Human")
		self.humanDetails =QTextEdit("In the reckonings of most worlds, humans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to dwarves, elves, and dragons.<br>Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.<br>------------Stats------------<br>Each Base Score +1<br>Speed:30 Feet<br>Skills: 1 Skill and Feat of your choice<br>Languages: Common and Another of Your Choice<br>Subrace: No")
		self.humanDetails.setReadOnly(True)


		self.abyssalButton=QRadioButton("Abyssal")
		self.abyssalButton.setToolTip("Spoken by: Demons, chaotic evil outsiders")
		
		self.aquanButton=QRadioButton("Aquan")
		self.aquanButton.setToolTip("Spoken by: Water-based creatures")	

		self.auranButton=QRadioButton("Auran")
		self.auranButton.setToolTip("Spoken by: Air-based creatures")



		self.celestialButton=QRadioButton("Celestial")
		self.celestialButton.setToolTip("Spoken by: Celestials (angels, devas)")

		self.deepspeechButton=QRadioButton("Deep Speech")
		self.deepspeechButton.setToolTip("Spoken by: Mind flayers, beholders")
		
		
		self.draconicButton=QRadioButton("Draconic")
		self.draconicButton.setToolTip("Spoken by: Kobolds, troglodytes, lizardfolk, dragons, dragonborn")
		
		self.druidicButton=QRadioButton("Druidic")
		self.druidicButton.setToolTip("Spoken by: Druids(only)")
		
		self.dwarvishButton=QRadioButton("Dwarvish")
		self.dwarvishButton.setToolTip("Spoken by: Dwarves")
		
		self.elvishButton=QRadioButton("Elvish")
		self.elvishButton.setToolTip("Spoken by: Elves")

		self.giantButton=QRadioButton("Giant")
		self.giantButton.setToolTip("Spoken by: Ogres, giants")
		
		self.gnomishButton=QRadioButton("Gnomish")
		self.gnomishButton.setToolTip("Spoken by: Gnomes")

		self.goblinButton=QRadioButton("Goblin")
		self.goblinButton.setToolTip("Spoken by: Goblinoids, hobgoblins, bugbears")

		self.gnollButton=QRadioButton("Gnoll")
		self.gnollButton.setToolTip("Spoken by: Gnolls")

		self.halflingButton=QRadioButton("Halfling")
		self.halflingButton.setToolTip("Spoken by: Halflings")

		self.ignanButton=QRadioButton("Ignan")
		self.ignanButton.setToolTip("Spoken by: Fire-based creatures")

		self.infernalButton=QRadioButton("Infernal")
		self.infernalButton.setToolTip("Spoken by: Devils, Tieflings")

		self.orcButton=QRadioButton("Orc")
		self.orcButton.setToolTip("Spoken by: Orcs")

		self.primordialButton=QRadioButton("Primordial")
		self.primordialButton.setToolTip("Spoken by: Elementals")

		self.sylvanButton=QRadioButton("Sylvan")
		self.sylvanButton.setToolTip("Spoken by: Fey creatures (dyrads, brownies, leprechauns)")

		self.terranButton=QRadioButton("Terran")
		self.terranButton.setToolTip("Spoken by: Xorns and other earth-based creatures")

		self.undercommonButton=QRadioButton("Undercommon")
		self.undercommonButton.setToolTip("Spoken by: Drow, Underdark, traders")

		self.hbox = QHBoxLayout()
		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QVBoxLayout()


		self.buttongroup = QButtonGroup()
		self.buttongroup.addButton(self.abyssalButton)
		self.buttongroup.addButton(self.aquanButton)
		self.buttongroup.addButton(self.auranButton)
		self.buttongroup.addButton(self.celestialButton)
		self.buttongroup.addButton(self.deepspeechButton)
		self.buttongroup.addButton(self.draconicButton)
		self.buttongroup.addButton(self.druidicButton)
		self.buttongroup.addButton(self.dwarvishButton)
		self.buttongroup.addButton(self.elvishButton)
		self.buttongroup.addButton(self.giantButton)
		self.buttongroup.addButton(self.gnomishButton)
		self.buttongroup.addButton(self.goblinButton)
		self.buttongroup.addButton(self.gnollButton)
		self.buttongroup.addButton(self.halflingButton)
		self.buttongroup.addButton(self.ignanButton)
		self.buttongroup.addButton(self.infernalButton)
		self.buttongroup.addButton(self.orcButton)
		self.buttongroup.addButton(self.primordialButton)
		self.buttongroup.addButton(self.sylvanButton)
		self.buttongroup.addButton(self.terranButton)
		self.buttongroup.addButton(self.undercommonButton)


		self.pic1label = QLabel(self)
		self.pic1label.resize(self.size()*.25)
		self.pic2label = QLabel(self)
		self.pic2label.resize(self.size()*.25)
		
		self.db1pixmap = QPixmap('human1.jpg').scaled(self.pic1label.size())
		self.db2pixmap = QPixmap('human2.jpg').scaled(self.pic2label.size())

		self.pic1label.setPixmap(self.db1pixmap)	
		self.pic2label.setPixmap(self.db2pixmap)

		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.humanTitle)
		self.vbox.addWidget(self.humanDetails)
		

		self.picbox.addWidget(self.pic1label)
		self.picbox.addWidget(self.pic2label)


		self.vbox.addLayout(self.picbox)
		

		self.buttonbox.addWidget(self.abyssalButton)
		self.buttonbox.addWidget(self.aquanButton)
		self.buttonbox.addWidget(self.auranButton)
		self.buttonbox.addWidget(self.celestialButton)

		self.buttonbox.addWidget(self.deepspeechButton)
		self.buttonbox.addWidget(self.draconicButton)
		self.buttonbox.addWidget(self.druidicButton)
		self.buttonbox.addWidget(self.dwarvishButton)
		self.buttonbox.addWidget(self.elvishButton)
		self.buttonbox.addWidget(self.giantButton)
		self.buttonbox.addWidget(self.gnomishButton)
		self.buttonbox.addWidget(self.goblinButton)
		self.buttonbox.addWidget(self.gnollButton)
		self.buttonbox.addWidget(self.halflingButton)
		self.buttonbox.addWidget(self.ignanButton)
		self.buttonbox.addWidget(self.infernalButton)
		self.buttonbox.addWidget(self.orcButton)
		self.buttonbox.addWidget(self.primordialButton)
		self.buttonbox.addWidget(self.sylvanButton)
		self.buttonbox.addWidget(self.terranButton)
		self.buttonbox.addWidget(self.undercommonButton)


		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Confirm your choice and return to race screen")
		self.doneButton.clicked.connect(self.close)
		

		#self.vbox.addLayout(self.buttonbox)
		self.vbox.addWidget(self.doneButton)
				

		self.hbox.addLayout(self.vbox)
		self.hbox.addLayout(self.buttonbox)
		self.setLayout(self.hbox)


		self.show()



	def closeEvent(self,event):
		if self.abyssalButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Abyssal")
			self.parent_window.label.setText("Human with Abyssal language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()		
		elif self.aquanButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Aquan")
			self.parent_window.label.setText("Human with Aquan language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.auranButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Auran")
			self.parent_window.label.setText("Human with Auran language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.celestialButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Celestial")
			self.parent_window.label.setText("Human with Celestial language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()

		elif self.deepspeechButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Deepspeech")
			self.parent_window.label.setText("Human with Deepspeech language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.draconicButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Draconic")
			self.parent_window.label.setText("Human with Draconic language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.druidicButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Druidic")
			self.parent_window.label.setText("Human with Druidic language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.dwarvishButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Dwarvish")
			self.parent_window.label.setText("Human with Dwarvish language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.elvishButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Elvish")
			self.parent_window.label.setText("Human with Evlish language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.giantButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Giant")
			self.parent_window.label.setText("Human with Giant language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.gnomishButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Gnomish")
			self.parent_window.label.setText("Human with Gnomish language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.goblinButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Goblin")
			self.parent_window.label.setText("Human with Goblin language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.gnollButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Gnoll")
			self.parent_window.label.setText("Human with Gnoll language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.halflingButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Halfling")
			self.parent_window.label.setText("Human with Halfling language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.ignanButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Ignan")
			self.parent_window.label.setText("Human with Ignan language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.infernalButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Infernal")
			self.parent_window.label.setText("Human with Infernal language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.orcButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Orc")
			self.parent_window.label.setText("Human with Orc language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.primordialButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Primordial")
			self.parent_window.label.setText("Human with Primordial language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.sylvanButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Sylvan")
			self.parent_window.label.setText("Human with Sylvan language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.terranButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Terran")
			self.parent_window.label.setText("Human with Terran language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.undercommonButton.isChecked():
			self.parent_window.tab_window.main_window.race = human.Human("Undercommon")
			self.parent_window.label.setText("Human with Undercommon language")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()

		else:
			self.label.setText("YOU MUST SELECT A LANGUAGE TO CONTINUE!")
			event.ignore()



if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainmain = QMainWindow()
	main_window = LanguageHuman(mainmain)
	app.exec_()
