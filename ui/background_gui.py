from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

class BackgroundWindow(QWidget):
	def __init__(self, parent):	
		QWidget.__init__(self)
		self.tab_window = parent
		self.setup()	

	def add_skills(self):
		self.layout2 = QWidget()
		self.hbox = QHBoxLayout()
		self.vbox2 = QVBoxLayout()
		self.vbox3 = QVBoxLayout()
		self.gbox = QGridLayout()

		self.l1 = QLabel()
		self.l1.setText("Choose Two More Profincies")
		self.l1.setAlignment(Qt.AlignCenter)

		self.b1 = QPushButton("Add Languages/Tools")

		self.languages = ["Common","Dwarvish","Elvish","Giant","Gnomish","Goblin","Halfling","Orc","Abyssal", "Celestial","Draconic","Deep Speech","Infernal","Primordial","Sylvan","Undercommon"]
		self.tools = ["Artisan's Tools", "Disguise Kit", "Forgery Kit", "Gaming Kit","Gaming Set", "Herbalism Kit", "Musical Instrument", "Navigator's Tools", "Poisoner's Kit", "Thieves" ]

		self.langauges_label = QLabel()
		self.tools_label = QLabel()

		self.langauges_label.setText("Languages")
		self.langauges_label.setAlignment(Qt.AlignCenter)
		self.tools_label.setAlignment(Qt.AlignCenter)
		self.tools_label.setText("Tools")

		self.vbox2.addWidget(self.langauges_label)
		self.vbox3.addWidget(self.tools_label)



		i = 0
		while i < len(self.languages):
			self.vbox2.addWidget(QCheckBox(self.languages[i]))
			self.vbox2.itemAt(i+1).setAlignment(Qt.AlignCenter)
			i = i + 1

		i = 0
		while i < len(self.tools):
			self.vbox3.addWidget(QCheckBox(self.tools[i]))
			self.vbox3.itemAt(i+1).setAlignment(Qt.AlignCenter)
			i = i + 1


		self.hbox.addLayout(self.vbox2)
		self.hbox.addLayout(self.vbox3)

		self.gbox.addWidget(self.l1,1,1,1,1)
		self.gbox.addLayout(self.hbox,2,1,5,1)
		self.gbox.addWidget(self.b1,7,1,1,1)

		self.layout2.setLayout(self.gbox)
		self.stacked_layout.addWidget(self.layout2)
		self.stacked_layout.setCurrentIndex(1)





	def setup(self):

		self.stacked_layout = QStackedLayout()
	

		self.vbox = QVBoxLayout()
		self.skills_label = QLabel()
		self.skills_label.setText("Choose Two Additional Skills")
		self.skills_label.setAlignment(Qt.AlignCenter)
		self.confirmSkillsButton = QPushButton("Add Skills")
		self.confirmSkillsButton.clicked.connect(self.add_skills)
		self.skills = ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana", "Hsitory", "Investigation", "Nature", "Religion", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"] 

		self.vbox.addWidget(self.skills_label)

		i = 0
		while i < len(self.skills):
			self.vbox.addWidget(QCheckBox(self.skills[i]))
			self.vbox.itemAt(i+1).setAlignment(Qt.AlignCenter)
			i = i + 1

		self.vbox.addWidget(self.confirmSkillsButton)

		self.layout1 = QWidget()
		self.layout1.setLayout(self.vbox)


		self.stacked_layout.addWidget(self.layout1)

		self.setLayout(self.stacked_layout)
		self.show()








