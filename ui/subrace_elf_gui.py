from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,json
sys.path.append(sys.path[0][:-2]+"races")
sys.path.append(sys.path[0][:-2])
jf = open('../spells.json')
jsonobject = json.load(jf)
import elf



class SubraceElf(QWidget):
	def __init__(self,parent):
		QWidget.__init__(self)
		self.parent_window = parent
		self.setup()

	def setup(self):
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Elf Subrace")
				
		self.elfTitle=QLabel()
		self.elfTitle.setText("Elf")
		self.elfDetails = QTextEdit("Elves love nature and magic, art and artistry, music and poetry, and the good things of the world.<br>With their unearthly grace and fine features, elves appear hauntingly beautiful to humans and members of many other races.<br>------------Stats------------<br>Dexterity +2<br>Speed:30 Feet<br>Skills:Darkvision, Keen Senses, Fey Ancestry, Trance<br>Languages: Common and Elvish<br>Subrace: Yes")
		self.elfDetails.setReadOnly(True)
		self.elfDetails.resize(self.width(), self.height()*.15)


		self.highButton=QRadioButton("High Elf")
		self.highButton.setToolTip("As a high elf, you have a keen mind and a mastery of at least the basics of magic<br>------------Stats------------<br>All Elf Base stats<br>Intellignece +1<br>Skills:Elf Weapon Training, Cantrip, Extra Language")

		self.woodButton=QRadioButton("Wood Elf")
		self.woodButton.setToolTip("As a wood elf, you have keen senses and intuition, and your fleet feet carry you quickly and stealthily through your native forests.<br>------------Stats------------<br>All Elf Base stats<br>Wisdom +1<br>Skills:Elf Weapon Training, Fleet of Foot, Mask of the Wild")

		self.darkButton=QRadioButton("Dark Elf")
		self.darkButton.setToolTip("Descended from an earlier subrace of dark-skinned elves, the drow were banished from the surface world for following the goddess Lolth down the path to evil and corruption.<br> Now they have built their own civilization in the depths of the Underdark, patterned after the Way of Lolth<br>------------Stats------------<br>All Elf Base stats<br>Charisma +1<br>Skills:Superior Darkvision, Sunlight Sensitivity, Drow Magic, Drow Weapon Training")
		
		#issue with accepting on done click
		
		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.buttongroup = QButtonGroup()
		self.buttongroup.addButton(self.highButton)
		self.buttongroup.addButton(self.woodButton)
		self.buttongroup.addButton(self.darkButton)


		self.highlabel = QLabel(self)
		self.highlabel.resize(self.size()*.25)
		self.woodlabel = QLabel(self)
		self.woodlabel.resize(self.size()*.25)
		self.darklabel = QLabel(self)
		self.darklabel.resize(self.size()*.25)

		self.highpixmap = QPixmap('highelf.jpg').scaled(self.highlabel.size())
		self.woodpixmap = QPixmap('woodelf.jpg').scaled(self.woodlabel.size())
		self.darkpixmap = QPixmap('darkelf.jpg').scaled(self.darklabel.size())

		self.highlabel.setPixmap(self.highpixmap)
		self.woodlabel.setPixmap(self.woodpixmap)
		self.darklabel.setPixmap(self.darkpixmap)

		self.vbox.addWidget(self.elfTitle)
		self.vbox.addWidget(self.elfDetails)

		self.picbox.addWidget(self.highlabel)
		self.picbox.addWidget(self.woodlabel)
		self.picbox.addWidget(self.darklabel)

		self.vbox.addLayout(self.picbox)

		
		self.buttonbox.addWidget(self.highButton)
		self.buttonbox.addWidget(self.woodButton)
		self.buttonbox.addWidget(self.darkButton)

		self.vbox.addLayout(self.buttonbox)

		self.bottombuttonbox = QHBoxLayout()
		self.vbox.addLayout(self.bottombuttonbox)

		self.applyButton = QPushButton("Apply")
		self.applyButton.setToolTip("This will apply your choice of subrace")
		self.bottombuttonbox.addWidget(self.applyButton)
		self.applyButton.clicked.connect(self.applyRace)


		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Exit this window and choose your cantrip: If you are a High Elf")
		self.bottombuttonbox.addWidget(self.doneButton)
		self.doneButton.clicked.connect(self.close)
		
		
		

		self.setLayout(self.vbox)

		self.show()

	def applyRace(self):
		if self.woodButton.isChecked():
			self.parent_window.tab_window.main_window.race = elf.Elf("Wood Elf")
		elif self.darkButton.isChecked():
			self.parent_window.tab_window.main_window.race = elf.Elf("Dark Elf (Drow)")
		elif self.highButton.isChecked():
			print("High Elf Selected")




	def closeEvent(self,event):

		if self.highButton.isChecked():
			self.pCan = PickCantrip(self,"High Elf")
			self.pCan.show()
		else:
			print("Closing subrace elf window and printing")
			print(self.parent_window.tab_window.main_window.race)
			print("Just printed from subrace elf window")

		event.accept()



class PickCantrip(QWidget):
	def __init__(self, parent, race):
		QWidget.__init__(self)
		self.parent = parent
		self.race = race
		self.cantrip = ""
		self.setWindowTitle("Pick Cantrip")
		self.show()
		self.setup()


	def setup(self):
		self.setGeometry(50,50,400,400)
		self.vertbox = QVBoxLayout()
		self.label = QLabel()
		self.label.setText("Choose your Cantrip")
		self.vertbox.addWidget(self.label)
		self.setLayout(self.vertbox)

		self.spellButtons = QButtonGroup()
		self.init_cantrips("Cantrip",u"Wizard")
		

	def init_cantrips(self,level,jsclass):
		self.buttonidmapping = {}
		self.ids = 0
		for each in jsonobject:
			if each['level'] == level and each['class'].find(jsclass) > -1:
				newbutton = QRadioButton(each['name'])
				newbutton.setToolTip(each['desc'])
				print(each['name'],"button's id is", self.ids)
				self.spellButtons.setId(newbutton,self.ids)
				self.buttonidmapping[each['name']] = self.ids
				self.spellButtons.addButton(newbutton)
				self.vertbox.addWidget(newbutton)
				self.ids +=1


		self.bottombuttonbox = QHBoxLayout()
		self.vertbox.addLayout(self.bottombuttonbox)

		self.applyButton = QPushButton("Apply")
		self.applyButton.setToolTip("This will apply your choice of cantrip")
		self.bottombuttonbox.addWidget(self.applyButton)
		self.applyButton.clicked.connect(self.sendSpell)


		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Exit this window and choose your language")
		self.bottombuttonbox.addWidget(self.doneButton)
		self.doneButton.clicked.connect(self.close)
		self.show()



	def sendSpell(self):
		print(self.spellButtons.checkedId(),"is checkedID")
		if self.spellButtons.checkedId() != -1:
			self.checkedId = (self.spellButtons.checkedId() * -1) -1
			for each in self.buttonidmapping.keys():
				if self.buttonidmapping[each] == self.checkedId:
					self.cantrip = each
					print ("Cantrip set to ",each)
					break
				else:
					print ("self.spellButtons.checkedId() is currently",self.checkedId,"and self.buttonidmapping[each] is",self.buttonidmapping[each], "and each is", each)
		else:
			print("No button selected")


	def closeEvent(self,event):
		
		self.pickLang = PickLanguage(self,self.race,self.cantrip)
		self.pickLang.show()
		event.accept()
			
	


	


class PickLanguage(QWidget):
	def __init__(self, parent, race, cantrip):
		QWidget.__init__(self)
		self.parent = parent
		self.race = race
		self.cantrip = cantrip
		self.buttonidmapping = {}
		self.idcounter = 1
		self.setWindowTitle("Pick Language")
		self.show()
		self.setup()

	def setup(self):
		self.setGeometry(50,50,400,400)
		self.vertbox = QVBoxLayout()
		self.label = QLabel()
		self.label.setText("Choose your Language")
		self.languageButtonGroup = QButtonGroup()
		self.setLanguageButtons()
		self.setLayout(self.vertbox)
		


	def setLanguageButtons(self):
		self.langbutton1 = QRadioButton("Abyssal")
		self.languageButtonGroup.addButton(self.langbutton1)
		self.languageButtonGroup.setId(self.langbutton1,self.idcounter)
		self.buttonidmapping["Abyssal"] = self.idcounter
		self.vertbox.addWidget(self.langbutton1)
		self.idcounter +=1
		#9108

		self.langbutton2 = QRadioButton("Aquan")
		self.languageButtonGroup.addButton(self.langbutton2)
		self.languageButtonGroup.setId(self.langbutton2,self.idcounter)
		self.buttonidmapping["Aquan"] = self.idcounter
		self.vertbox.addWidget(self.langbutton2)
		self.idcounter +=1

		self.langbutton3 = QRadioButton("Auran")
		self.languageButtonGroup.addButton(self.langbutton3)
		self.languageButtonGroup.setId(self.langbutton3,self.idcounter)
		self.buttonidmapping["Auran"] = self.idcounter
		self.vertbox.addWidget(self.langbutton3)
		self.idcounter +=1

		self.langbutton4 = QRadioButton("Celestial")
		self.languageButtonGroup.addButton(self.langbutton4)
		self.languageButtonGroup.setId(self.langbutton4,self.idcounter)
		self.buttonidmapping["Celestial"] = self.idcounter
		self.vertbox.addWidget(self.langbutton4)
		self.idcounter +=1

		self.langbutton5 = QRadioButton("Deep Speech")
		self.languageButtonGroup.addButton(self.langbutton5)
		self.languageButtonGroup.setId(self.langbutton5,self.idcounter)
		self.buttonidmapping["Deep Speech"] = self.idcounter
		self.vertbox.addWidget(self.langbutton5)
		self.idcounter +=1

		self.langbutton6 = QRadioButton("Draconic")
		self.languageButtonGroup.addButton(self.langbutton6)
		self.languageButtonGroup.setId(self.langbutton6,self.idcounter)
		self.buttonidmapping["Draconic"] = self.idcounter
		self.vertbox.addWidget(self.langbutton6)
		self.idcounter +=1

		self.langbutton7 = QRadioButton("Druidic")
		self.languageButtonGroup.addButton(self.langbutton7)
		self.languageButtonGroup.setId(self.langbutton7,self.idcounter)
		self.buttonidmapping["Druidic"] = self.idcounter
		self.vertbox.addWidget(self.langbutton7)
		self.idcounter +=1

		self.langbutton8 = QRadioButton("Dwarvish")
		self.languageButtonGroup.addButton(self.langbutton8)
		self.languageButtonGroup.setId(self.langbutton8,self.idcounter)
		self.buttonidmapping["Dwarvish"] = self.idcounter
		self.vertbox.addWidget(self.langbutton8)
		self.idcounter +=1

		self.langbutton9 = QRadioButton("Giant")
		self.languageButtonGroup.addButton(self.langbutton9)
		self.languageButtonGroup.setId(self.langbutton9,self.idcounter)
		self.buttonidmapping["Giant"] = self.idcounter
		self.vertbox.addWidget(self.langbutton9)
		self.idcounter +=1

		self.langbutton10 = QRadioButton("Gnomish")
		self.languageButtonGroup.addButton(self.langbutton10)
		self.languageButtonGroup.setId(self.langbutton10,self.idcounter)
		self.buttonidmapping["Gnomish"] = self.idcounter
		self.vertbox.addWidget(self.langbutton10)
		self.idcounter +=1

		self.langbutton11 = QRadioButton("Goblin")
		self.languageButtonGroup.addButton(self.langbutton11)
		self.languageButtonGroup.setId(self.langbutton11,self.idcounter)
		self.buttonidmapping["Goblin"] = self.idcounter
		self.vertbox.addWidget(self.langbutton11)
		self.idcounter +=1

		self.langbutton12 = QRadioButton("Gnoll")
		self.languageButtonGroup.addButton(self.langbutton12)
		self.languageButtonGroup.setId(self.langbutton12,self.idcounter)
		self.buttonidmapping["Gnoll"] = self.idcounter
		self.vertbox.addWidget(self.langbutton12)
		self.idcounter +=1

		self.langbutton13 = QRadioButton("Halfling")
		self.languageButtonGroup.addButton(self.langbutton13)
		self.languageButtonGroup.setId(self.langbutton13,self.idcounter)
		self.buttonidmapping["Halfling"] = self.idcounter
		self.vertbox.addWidget(self.langbutton13)
		self.idcounter +=1

		self.langbutton14 = QRadioButton("Ignan")
		self.languageButtonGroup.addButton(self.langbutton14)
		self.languageButtonGroup.setId(self.langbutton14,self.idcounter)
		self.buttonidmapping["Ignan"] = self.idcounter
		self.vertbox.addWidget(self.langbutton14)
		self.idcounter +=1

		self.langbutton15 = QRadioButton("Infernal")
		self.languageButtonGroup.addButton(self.langbutton15)
		self.languageButtonGroup.setId(self.langbutton15,self.idcounter)
		self.buttonidmapping["Infernal"] = self.idcounter
		self.vertbox.addWidget(self.langbutton15)
		self.idcounter +=1

		self.langbutton16 = QRadioButton("Orc")
		self.languageButtonGroup.addButton(self.langbutton16)
		self.languageButtonGroup.setId(self.langbutton16,self.idcounter)
		self.buttonidmapping["Orc"] = self.idcounter
		self.vertbox.addWidget(self.langbutton16)
		self.idcounter +=1

		self.langbutton17 = QRadioButton("Primordial")
		self.languageButtonGroup.addButton(self.langbutton17)
		self.languageButtonGroup.setId(self.langbutton17,self.idcounter)
		self.buttonidmapping["Primordial"] = self.idcounter
		self.vertbox.addWidget(self.langbutton17)
		self.idcounter +=1

		self.langbutton18 = QRadioButton("Sylvan")
		self.languageButtonGroup.addButton(self.langbutton18)
		self.languageButtonGroup.setId(self.langbutton18,self.idcounter)
		self.buttonidmapping["Sylvan"] = self.idcounter
		self.vertbox.addWidget(self.langbutton18)
		self.idcounter +=1

		self.langbutton19 = QRadioButton("Terran")
		self.languageButtonGroup.addButton(self.langbutton19)
		self.languageButtonGroup.setId(self.langbutton19,self.idcounter)
		self.buttonidmapping["Terran"] = self.idcounter
		self.vertbox.addWidget(self.langbutton19)
		self.idcounter +=1

		self.langbutton20 = QRadioButton("Undercommon")
		self.languageButtonGroup.addButton(self.langbutton20)
		self.languageButtonGroup.setId(self.langbutton20,self.idcounter)
		self.buttonidmapping["Undercommon"] = self.idcounter
		self.vertbox.addWidget(self.langbutton20)
		self.idcounter +=1

		self.bottombuttonbox = QHBoxLayout()
		self.vertbox.addLayout(self.bottombuttonbox)

		self.applyButton = QPushButton("Apply")
		self.applyButton.setToolTip("This will confirm your choice of language")
		self.bottombuttonbox.addWidget(self.applyButton)
		self.applyButton.clicked.connect(self.done)

		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Exit this window")
		self.bottombuttonbox.addWidget(self.doneButton)
		self.doneButton.clicked.connect(self.close)

	def done(self):
		self.parent.parent.parent_window.tab_window.main_window.race = elf.Elf("High Elf",self.cantrip, self.getLanguage())


	def getLanguage(self):
		for lang in self.buttonidmapping.keys():
			if self.buttonidmapping[lang] == self.languageButtonGroup.checkedId():
				return lang


	def closeEvent(self,event):
		if self.languageButtonGroup.checkedId() != -1:
			print("Closing Language window and printing")
			print(self.parent.parent.parent_window.tab_window.main_window.race)
			print("Just printed from Language window")
			event.accept()

		else:
			print ("No language chosen so no cantrip chosen so no subrace chosen")
			event.accept()




	

if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainmain = QMainWindow()
	main_window = SubraceElf(mainmain)
	app.exec_()

