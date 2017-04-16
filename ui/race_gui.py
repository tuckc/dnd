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
		
		
		self.halflingButton=QPushButton("Halfling")
		self.halflingButton.setToolTip("these wanderers love peace, food, hearth, and home, though home might be a wagon jostling along an dirt road or a raft floating downriver.<br>The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense.<br> Standing about 3 feet tall, they appear relatively harmless and so have managed to survive for centuries in the shadow of empires and on the edges of wars and political strife<br>------------Stats------------<br>Dexterity +2<br>Speed:25 Feet<br>Skills:Lucky, Brave, Halfling Nimbleness<br>Languages: Common and Halfling<br>Subrace: Yes")
		
		self.dwarfButton=QPushButton("Dwarf")
		self.dwarfButton.setToolTip("Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.<br> Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller.<br> Their courage and endurance are also easily a match for any of the larger folk.<br>------------Stats------------<br>Constitution +2<br>Speed:25 Feet<br>Skills:Darkvision, Dwarven Resilience, Dwarven Combat Training, Tool Proficiency, Stonecunning<br>Languages: Dwarvish<br>Subrace: Yes")

		self.elfButton=QPushButton("Elf")
		self.elfButton.setToolTip("Elves love nature and magic, art and artistry, music and poetry, and the good things of the world.<br>With their unearthly grace and fine features, elves appear hauntingly beautiful to humans and members of many other races.<br>------------Stats------------<br>Dexterity +2<br>Speed:30 Feet<br>Skills:Darkvision, Keen Senses, Fey Ancestry, Trance<br>Languages: Common and Elvish<br>Subrace: Yes")

		self.halfelfButton=QPushButton("Half-Elf")
		self.halfelfButton.setToolTip("Walking in two w orlds but truly belonging to neither,half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes o f the elves.<br>Many half-elves,unable to fit into either society, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life.<br>------------Stats------------<br>Charisma +2 and 2 Skills of your choice +1<br>Speed:30 Feet<br>Skills:Darkvision, Fey Ancestry, Skill Versatility<br>Languages: Common, Elvish, And 1 more of your choice<br>Subrace: No")

		self.tieflingButton=QPushButton("Tiefling")
		self.tieflingButton.setToolTip("To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye.<br> This is the lot of the tiefling. <br>Their appearance and their nature are not their fault but the result of an ancient sin.<br>------------Stats------------<br>Charisma +2 and Intelligence +1<br>Speed:30 Feet<br>Skills:Darkvision, Hellish Resistance, Infernal Legacy<br>Languages: Common and Infernal<br>Subrace: No")

		self.humanButton=QPushButton("Human")
		self.humanButton.setToolTip("In the reckonings of most worlds, humans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to dwarves, elves, and dragons.<br>Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.<br>------------Stats------------<br>Each Base Score +1<br>Speed:30 Feet<br>Skills: 1 Skill and Feat of your choice<br>Languages: Common and Another of Your Choice<br>Subrace: No")

		self.dragonbornButton=QPushButton("Dragonborn")
		self.dragonbornButton.setToolTip("Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension.<br> Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids.<br>------------Stats------------<br>Strength +1 and Charisma +1<br>Speed:30 Feet<br>Skills:Dragonic Ancestry, Breath Weapon, Damage Resistance<br>Languages: Common and Dragonic<br>Subrace: No")

		self.halforcButton=QPushButton("Half-Orc")
		self.halforcButton.setToolTip("Whether united under the leadership of a mighty warlock or having fought to a standstill after years of conflict, orc and human tribes sometimes form alliances, joining forces into a larger horde to the terror of civilized lands nearby. When these alliances are sealed by marriages, half-orcs are born.<br> Some half-orcs rise to become proud chiefs of orc tribes, their human blood giving them an edge over their full-blooded orc rivals.<br>------------Stats------------<br>Strength +2 and Constitution +1<br>Speed:30 Feet<br>Skills:Darkvision, Menacing, Relentless Endurance, Savage Attack<br>Languages: Common and Orc<br>Subrace: No")		

		self.vbox = QtWidgets.QVBoxLayout()
		self.picbox = QtWidgets.QHBoxLayout()
		self.buttonbox = QtWidgets.QHBoxLayout()

		self.label = QLabel(self)
		self.pixmap = QPixmap('race.jpg')
		self.label.setPixmap(self.pixmap)
		self.picbox.addWidget(self.label)

		
		self.buttonbox.addWidget(self.gnomeButton)		
		self.buttonbox.addWidget(self.halflingButton)		
		self.buttonbox.addWidget(self.dwarfButton)
		self.buttonbox.addWidget(self.elfButton)
		self.buttonbox.addWidget(self.halfelfButton)
		self.buttonbox.addWidget(self.tieflingButton)
		self.buttonbox.addWidget(self.humanButton)
		self.buttonbox.addWidget(self.dragonbornButton)
		self.buttonbox.addWidget(self.halforcButton)
		

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
