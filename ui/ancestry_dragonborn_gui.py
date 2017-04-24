'''
Ancestry
'''
#UserInterface.py
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
sys.path.append(sys.path[0][:-2]+"races")

import dragonborn

class AncestryDragonborn(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self)
		self.parent_window = parent
		self.label = QLabel()
		self.label.setText("Choose your ancestry here!")
		self.setup()

	def setup(self):
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Dragonborn Ancestry")
		
		self.dragonbornTitle=QLabel()
		self.dragonbornTitle.setText("Dragonborn")
		self.dragonbornDetails =QTextEdit("Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension.<br> Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids.<br>------------Stats------------<br>Strength +1 and Charisma +1<br>Speed:30 Feet<br>Skills:Dragonic Ancestry, Breath Weapon, Damage Resistance<br>Languages: Common and Dragonic<br>Subrace: No")
		self.dragonbornDetails.setReadOnly(True)


		self.blackButton=QRadioButton("Black")
		self.blackButton.setToolTip("Acid Damage<br>5 by 30ft.line (Dex.save)")
		self.blueButton=QRadioButton("Blue")
		self.blueButton.setToolTip("Lightning Damage<br>5 by 30ft.line (Dex.save)")
		self.brassButton=QRadioButton("Brass")
		self.brassButton.setToolTip("Fire Damage<br>5 by 30ft.line (Dex.save)")
		self.bronzeButton=QRadioButton("Bronze")
		self.bronzeButton.setToolTip("Lightning Damage<br>5 by 30ft.line (Dex.save)")
		self.copperButton=QRadioButton("Copper")
		self.copperButton.setToolTip("Acid Damage<br>5 by 30ft.line (Dex.save)")
		self.goldButton=QRadioButton("Gold")
		self.goldButton.setToolTip("Fire Damage<br>15ft.cone (Dex.save)")
		self.greenButton=QRadioButton("Green")
		self.greenButton.setToolTip("Poison Damage<br>15 ft.cone (Con.save)")
		self.redButton=QRadioButton("Red")
		self.redButton.setToolTip("Fire Damage<br>15ft.cone (Dex.save)")
		self.silverButton=QRadioButton("Silver")
		self.silverButton.setToolTip("Cold Damage<br> 15ft.cone (Con.save)")
		self.whiteButton=QRadioButton("White")
		self.whiteButton.setToolTip("Cold Damage<br>15ft.cone (Con.save)")
		
		
		

		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()


		self.buttongroup = QButtonGroup()
		self.buttongroup.addButton(self.blackButton)
		self.buttongroup.addButton(self.blueButton)
		self.buttongroup.addButton(self.brassButton)
		self.buttongroup.addButton(self.bronzeButton)
		self.buttongroup.addButton(self.copperButton)
		self.buttongroup.addButton(self.goldButton)
		self.buttongroup.addButton(self.greenButton)
		self.buttongroup.addButton(self.redButton)
		self.buttongroup.addButton(self.silverButton)
		self.buttongroup.addButton(self.whiteButton)


		self.pic1label = QLabel(self)
		self.pic1label.resize(self.size()*.25)
		self.pic2label = QLabel(self)
		self.pic2label.resize(self.size()*.25)
		
		self.db1pixmap = QPixmap('dragonborn1.jpg').scaled(self.pic1label.size())
		self.db2pixmap = QPixmap('dragonborn2.jpg').scaled(self.pic2label.size())

		self.pic1label.setPixmap(self.db1pixmap)	#hilllabel= pic1
		self.pic2label.setPixmap(self.db2pixmap)#mountainlable=pic2

		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.dragonbornTitle)
		self.vbox.addWidget(self.dragonbornDetails)
		

		self.picbox.addWidget(self.pic1label)
		self.picbox.addWidget(self.pic2label)


		self.vbox.addLayout(self.picbox)
		

		self.buttonbox.addWidget(self.blackButton)
		self.buttonbox.addWidget(self.blueButton)
		self.buttonbox.addWidget(self.brassButton)
		self.buttonbox.addWidget(self.bronzeButton)
		self.buttonbox.addWidget(self.copperButton)
		self.buttonbox.addWidget(self.goldButton)
		self.buttonbox.addWidget(self.greenButton)
		self.buttonbox.addWidget(self.redButton)
		self.buttonbox.addWidget(self.silverButton)
		self.buttonbox.addWidget(self.whiteButton)

		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Confirm your choice and return to race screen")
		self.doneButton.clicked.connect(self.close)
		

		self.vbox.addLayout(self.buttonbox)
		self.vbox.addWidget(self.doneButton)
				
		self.setLayout(self.vbox)

		self.show()



	def closeEvent(self,event):
		if self.blackButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Black")
			self.parent_window.label.setText("Black Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.blueButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Blue")
			self.parent_window.label.setText("Blue Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.brassButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Brass")
			self.parent_window.label.setText("Brass Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.bronzeButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Bronze")
			self.parent_window.label.setText("Bronze Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.copperButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Copper")
			self.parent_window.label.setText("Copper Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.goldButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Gold")
			self.parent_window.label.setText("Gold Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.greenButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Green")
			self.parent_window.label.setText("Green Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.redButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Red")
			self.parent_window.label.setText("Red Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.silverButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("Silver")
			self.parent_window.label.setText("Silver Dragonborn")

			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		elif self.whiteButton.isChecked():
			self.parent_window.tab_window.main_window.race = dragonborn.Dragonborn("White")
			self.parent_window.label.setText("White Dragonborn")
			#print("Character is now")
			#print(self.parent_window.tab_window.main_window.race)
			event.accept()
		else:
			self.label.setText("YOU MUST SELECT AN ANCESTRY TO CONTINUE!")
			event.ignore()



if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainmain = QMainWindow()
	main_window = AncestryDragonborn(mainmain)
	app.exec_()
