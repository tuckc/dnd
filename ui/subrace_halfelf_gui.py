from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,json
sys.path.append(sys.path[0][:-2]+"races")
sys.path.append(sys.path[0][:-2])
import halfelf


class SubraceHalfelf(QWidget):
	def __init__(self,parent):
		QWidget.__init__(self)
		self.parent_window = parent
		self.setup()

	def setup(self):
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Dungeons and Dragons Character Creator: Halfelf Subrace")
	
		self.label = QLabel()
		self.label.setText("Choose your Ability here!")

		self.halfelfTitle=QLabel()
		self.halfelfTitle.setText("Halfelf")
		self.halfelfDetails = QTextEdit("Walking in two worlds but truly belonging to neither,half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes o f the elves.<br>Many half-elves,unable to fit into either society, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life.<br>------------Stats------------<br>Charisma +2 and 2 Skills of your choice +1<br>Speed:30 Feet<br>Skills:Darkvision, Fey Ancestry, Skill Versatility<br>Languages: Common, Elvish, And 1 more of your choice<br>Subrace: No")
		self.halfelfDetails.setReadOnly(True)
		self.halfelfDetails.resize(self.width(), self.height()*.15)


		self.strengthButton=QRadioButton("Strength")
		self.strengthButton.setToolTip("Strength +1")

		self.dexterityButton=QRadioButton("Dexterity")
		self.dexterityButton.setToolTip("Dexterity +1")

		self.constitutionButton=QRadioButton("Constitution")
		self.constitutionButton.setToolTip("Constitution +1")
		
		self.intelligenceButton=QRadioButton("Intelligence")
		self.intelligenceButton.setToolTip("Intelligence +1")

		self.wisdomButton=QRadioButton("Wisdom")
		self.wisdomButton.setToolTip("Wisdom +1")		
		
		
		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.buttongroup = QButtonGroup()
		self.buttongroup.addButton(self.strengthButton)
		self.buttongroup.addButton(self.dexterityButton)
		self.buttongroup.addButton(self.constitutionButton)
		self.buttongroup.addButton(self.intelligenceButton)
		self.buttongroup.addButton(self.wisdomButton)


		self.highlabel = QLabel(self)
		self.highlabel.resize(self.size()*.25) #maybe.25 if too big
		self.woodlabel = QLabel(self)
		self.woodlabel.resize(self.size()*.25)# same as top
		

		self.highpixmap = QPixmap('halfelf1.jpg').scaled(self.highlabel.size())
		self.woodpixmap = QPixmap('halfelf2.jpg').scaled(self.woodlabel.size())
		

		self.highlabel.setPixmap(self.highpixmap)
		self.woodlabel.setPixmap(self.woodpixmap)
		

		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.halfelfTitle)
		self.vbox.addWidget(self.halfelfDetails)

		self.picbox.addWidget(self.highlabel)
		self.picbox.addWidget(self.woodlabel)
		

		self.vbox.addLayout(self.picbox)

		
		self.buttonbox.addWidget(self.strengthButton)
		self.buttonbox.addWidget(self.dexterityButton)
		self.buttonbox.addWidget(self.constitutionButton)
		self.buttonbox.addWidget(self.intelligenceButton)
		self.buttonbox.addWidget(self.wisdomButton)
		

		self.vbox.addLayout(self.buttonbox)

		self.bottombuttonbox = QHBoxLayout()
		self.vbox.addLayout(self.bottombuttonbox)




		self.doneButton = QPushButton("Done/Next")
		self.doneButton.setToolTip("Exit this window and choose your language")
		self.bottombuttonbox.addWidget(self.doneButton)
		self.doneButton.clicked.connect(self.close)
		
		
		

		self.setLayout(self.vbox)

		self.show()


	def closeEvent(self,event):

		if self.strengthButton.isChecked():
			self.pCan = PickLanguage(self,"Strength")
			self.pCan.show()
			event.accept()
		elif self.dexterityButton.isChecked():
			self.pCan = PickLanguage(self,"Dexterity")
			self.pCan.show()
			event.accept()
		elif self.constitutionButton.isChecked():
			self.pCan = PickLanguage(self,"Constitution")
			self.pCan.show()
			event.accept()
		elif self.intelligenceButton.isChecked():
			self.pCan = PickLanguage(self,"Intelligence")
			self.pCan.show()
			event.accept()
		elif self.wisdomButton.isChecked():
			self.pCan = PickLanguage(self,"Wisdom")
			self.pCan.show()
			event.accept()
		else:
			self.label.setText("YOU MUST SELECT AN ABILITY TO CONTINUE!")
			event.ignore()
			

class PickLanguage(QWidget):
	def __init__(self, parent,ability):
		QWidget.__init__(self)
		self.parent = parent
		self.buttonidmapping = {}
		self.idcounter = 1
		self.setWindowTitle("Pick Language")
		self.ability=ability		
		self.show()
		self.setup()

	def setup(self):
		self.setGeometry(100,100,300,300)
		self.vertbox = QVBoxLayout()
		self.label = QLabel()
		self.label.setText("Choose your Language")
		self.languageButtonGroup = QButtonGroup()
		self.vertbox.addWidget(self.label)
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






		self.doneButton = QPushButton("Done")
		self.doneButton.setToolTip("Confirm your choice and close this window")
		self.doneButton.clicked.connect(self.close)

		self.vertbox.addWidget(self.doneButton)


	def getLanguage(self):
		for lang in self.buttonidmapping.keys():
			if self.buttonidmapping[lang] == self.languageButtonGroup.checkedId():
				return lang


	def closeEvent(self,event):
		if self.languageButtonGroup.checkedId() != -1:
			if self.ability == "Strength":
				self.parent.parent_window.tab_window.main_window.race = halfelf.Halfelf("Strength",self.getLanguage())
			elif self.ability == "Dexterity":
				self.parent.parent_window.tab_window.main_window.race = halfelf.Halfelf("Dexterity",self.getLanguage())
			elif self.ability == "Constitution":
				self.parent.parent_window.tab_window.main_window.race = halfelf.Halfelf("Constitution",self.getLanguage())
			elif self.ability == "Intelligence":
				self.parent.parent_window.tab_window.main_window.race = halfelf.Halfelf("Intelligence",self.getLanguage())
			elif self.ability == "Wisdom":
				self.parent.parent_window.tab_window.main_window.race = halfelf.Halfelf("Wisdom",self.getLanguage())
			self.parent.parent_window.label.setText("Halfelf with {} Language".format(self.getLanguage()))
			print("Character set to")
			print(self.parent.parent_window.tab_window.main_window.race)
			event.accept()
		else:
			self.label.setText("YOU MUST SELECT A LANGUAGE TO MOVE ON!")
			event.ignore()
		




	

if __name__ == "__main__":

	app = QApplication(sys.argv)
	mainmain = QMainWindow()
	main_window = SubraceHalfelf(mainmain)
	app.exec_()

