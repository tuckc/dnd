#pre set char templates for now [Using the quick build template provided by book and intial set of equipment(a)]
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#print (sys.path)
sys.path.append(sys.path[0][:-2]+"classes")
sys.path.append(sys.path[0][:-2])
#print(sys.path)
import background_gui
import barbarian
import bard
import char_class
import cleric
import druid
import fighter
import monk
import paladin
import ranger
import rogue
import sorcerer
import warlock
import wizard

class ClassWindow(QWidget):
	def __init__(self, parent):
		QWidget.__init__(self)
		self.tab_window = parent
		self.window_title = QLabel("Choose your class!")
		self.window_title.setAlignment(Qt.AlignCenter)
		self.title = QLabel("Your current Class is: ")	
		self.label = QLabel()	
		self.setup()

	def handler(self,pickedClass):
		if pickedClass == 'barbarian':
			self.tab_window.main_window.classes=barbarian.Barbarian(['Nature','Perception'],['Great-Axe','Two Handaxe','Explorer Pack with 4 Javelins'])	
			self.label.setText("Barbarian\n{}".format(self.tab_window.main_window.classes.__str__()))
			

		elif pickedClass == 'bard':
			self.tab_window.main_window.classes=bard.Bard(['Persuasion', 'Stealth','Nature'],['Rapier','Diplomat Pack'],['Flute'],['Dancing Lights','Viscous Mockery'],['Charm Person','Detect Magic','Healing Word','Thunderwave'])			
			self.label.setText("Bard\n{}".format(self.tab_window.main_window.classes.__str__()))


		elif pickedClass == 'cleric':
			self.tab_window.main_window.classes=cleric.Cleric(['Persuasion','Religion'],['Mace','Scale mail','Light Crossbow','PriestPack','Shield'],['Guidance','Light','Mending'],['Command','Identify'],'Light Domain')			
			self.label.setText("Cleric\n{}".format(self.tab_window.main_window.classes.__str__()))


		elif pickedClass == 'druid':
			self.tab_window.main_window.classes=druid.Druid(["Animal Handling","Survival"],['Wooden Shield','Scimitar','Leather armor','Explorers Pack','Druidic Focus'],['Posion Spray','Frostbite'],["Calm Animal","Charm Animal"])			
			self.label.setText("Druid\n{}".format(self.tab_window.main_window.classes.__str__()))


		elif pickedClass == 'fighter':
			self.tab_window.main_window.classes=fighter.Fighter(['Intimidation','Athletics'],['Chain mail','Martial Weapon and Shield','Light Crossbow and 20 bolts','Dungeoneers pack'],'Dueling')			
			self.label.setText("Fighter\n{}".format(self.tab_window.main_window.classes.__str__()))


		elif pickedClass == 'monk':
			self.tab_window.main_window.classes=monk.Monk(['Acrobatics','Stealth'],['Shortsword','Dungeoneer pack','10 Darts'],'Guitar')
			self.label.setText("Monk\n{}".format(self.tab_window.main_window.classes.__str__()))

		
		elif pickedClass == 'paladin':
			self.tab_window.main_window.classes=paladin.Paladin(['Medicine','Religion'],['Martial weapon and Shield','5 Javelins','Priest Pack','Chain Mail','Holy Symbol'])
			self.label.setText("Paladin\n{}".format(self.tab_window.main_window.classes.__str__()))



		elif pickedClass == 'ranger':
			self.tab_window.main_window.classes=ranger.Ranger(['Animal Handling','Nature'],['Scale mail','Two shortswords','Dungeoneer pack','Longbow 20 arrows'])			
			self.label.setText("Ranger\n{}".format(self.tab_window.main_window.classes.__str__()))
			

		elif pickedClass == 'rogue':
			self.tab_window.main_window.classes=rogue.Rogue(['Stealth','Sleight of hand','Investigation','Athleticism'],['Rapier','Shortbow with 20 arrows','Burglars pack','Leather armor','Two daggers',"Thieve's tools"],'Thieves tools','Stealth')			
			self.label.setText("Rogue\n{}".format(self.tab_window.main_window.classes.__str__()))
			
		elif pickedClass == 'sorcerer':
			self.tab_window.main_window.classes=sorcerer.Sorcerer(['Arcana','Insight'],['Light crossbow 20 bolts','Component pouch','Dungeoneers pack','Two Daggers'],['Light','Prestidigitation','Ray of frost','Shocking grasp'],['Shield','Magic missile'],'Bloodline')
			self.label.setText("Sorceror\n{}".format(self.tab_window.main_window.classes.__str__()))
			


		elif pickedClass == 'warlock':
			self.tab_window.main_window.classes=warlock.Warlock(["Arcana","Religion"],['Light crossbow 20 bolts','Component pouch','Scholars pack','Leather armor','Shortsword','Two daggers'],['Eldrich blast','Chill touch'],['Ray of sickness','Witch bolt'],'The Fiend')	
			self.label.setText("Warlock\n{}".format(self.tab_window.main_window.classes.__str__()))
			


		elif pickedClass == 'wizard':
			self.tab_window.main_window.classes=wizard.Wizard(['History','Insight'],['Quarterstaff','Component pouch','Scholar pack','Spellbook'],['Mage hand','Light','Ray of Frost'],['Burning hands','Charm person','Feather fall','Mage armor','Missile','Sleep'])			
			self.label.setText("Wizard\n{}".format(self.tab_window.main_window.classes.__str__()))
			


		
		

	def setup(self):	
		self.barbarianButton=QPushButton('Barbarian')
		self.barbarianButton.setToolTip("A fierce warrior of primitive background who can enter a battle rage")
		self.barbarianButton.clicked.connect(lambda :self.handler("barbarian"))
						
		self.bardButton=QPushButton("Bard")
		self.bardButton.setToolTip("An inspiring magician whose power echoes the music of creation")
		self.bardButton.clicked.connect(lambda :self.handler("bard"))	

		self.clericButton=QPushButton("Cleric")
		self.clericButton.setToolTip("A priestly champion who wields divine magic in service of a higher power")
		self.clericButton.clicked.connect(lambda :self.handler("cleric"))	


		self.druidButton=QPushButton("Druid")
		self.druidButton.setToolTip("A priest of the Old Faith, wielding the powers of nature moonlight and plant growth, fire and lightning and adopting animal forms")
		self.druidButton.clicked.connect(lambda :self.handler("druid"))	


		self.fighterButton=QPushButton("Fighter")
		self.fighterButton.setToolTip("A master of martial combat, skilled with a variety of weapons and armor")
		self.fighterButton.clicked.connect(lambda :self.handler("fighter"))	


		self.monkButton=QPushButton("Monk")
		self.monkButton.setToolTip("An master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection")
		self.monkButton.clicked.connect(lambda :self.handler("monk"))	


		self.paladinButton=QPushButton("Paladin")
		self.paladinButton.setToolTip("A holy warrior bound to a sacred oath")
		self.paladinButton.clicked.connect(lambda :self.handler("paladin"))	


		self.rangerButton=QPushButton("Ranger")
		self.rangerButton.setToolTip("A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization")
		self.rangerButton.clicked.connect(lambda :self.handler("ranger"))	
		

		self.rogueButton=QPushButton("Rogue")
		self.rogueButton.setToolTip("A scoundrel who uses stealth and trickery to overcome obstacles and enemies")
		self.rogueButton.clicked.connect(lambda :self.handler("rogue"))	

		self.sorcererButton=QPushButton("Sorcerer")
		self.sorcererButton.setToolTip("A spellcaster who draws on inherent magic from a gift or bloodline")
		self.sorcererButton.clicked.connect(lambda :self.handler("sorcerer"))	


		self.warlockButton=QPushButton("Warlock")
		self.warlockButton.setToolTip("A wielder of magic that is derived from a bargain with an extraplanar entity")
		self.warlockButton.clicked.connect(lambda :self.handler("warlock"))	

		self.wizardButton=QPushButton("Wizard")
		self.wizardButton.setToolTip("A scholarly magic-user capable of manipulating the structures of reality")
		self.wizardButton.clicked.connect(lambda :self.handler("wizard"))	
		


		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()
		self.titlebox = QHBoxLayout()
		self.titlebox.addWidget(self.title)
		self.titlebox.addWidget(self.label)

		self.vbox.addWidget(self.window_title)
		self.vbox.addLayout(self.titlebox)
		self.classpic = QLabel(self)
		self.pixmap = QPixmap('classes.jpg')
		self.classpic.setPixmap(self.pixmap)
		self.picbox.addWidget(self.classpic)
		self.classpic.resize(self.width()-50,self.height()-400)
		
		self.buttonbox.addWidget(self.barbarianButton)		
		self.buttonbox.addWidget(self.bardButton)		
		self.buttonbox.addWidget(self.clericButton)
		self.buttonbox.addWidget(self.druidButton)
		self.buttonbox.addWidget(self.fighterButton)
		self.buttonbox.addWidget(self.monkButton)
		self.buttonbox.addWidget(self.paladinButton)
		self.buttonbox.addWidget(self.rangerButton)
		self.buttonbox.addWidget(self.rogueButton)
		self.buttonbox.addWidget(self.sorcererButton)
		self.buttonbox.addWidget(self.warlockButton)
		self.buttonbox.addWidget(self.wizardButton)

		self.confirmButton = QPushButton("Confirm")
		self.confirmButton.clicked.connect(self.confirm)
		

		self.setLayout(self.vbox)
		self.vbox.addLayout(self.picbox)
		self.vbox.addLayout(self.buttonbox)
		self.vbox.addWidget(self.confirmButton)

		self.show()

	def confirm(self):
		if self.tab_window.main_window.backgroundpagecount < 1:
			self.tab_window.BackgroundWindowObject = background_gui.BackgroundWindow(self.tab_window)
			self.tab_window.addTab(self.tab_window.BackgroundWindowObject, "&Background")
			self.tab_window.setCurrentIndex(4)
			self.window_title.setText("Class Confirmed")
			self.tab_window.main_window.backgroundpagecount = 1
		else:
			self.tab_window.setCurrentIndex(4)
			
	

if __name__ == "__main__":

	app = QApplication(sys.argv)
	main_window = ClassWindow()
	app.exec_()

