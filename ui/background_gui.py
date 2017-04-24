from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import os
import sys
import fdfgen
sys.path.append(sys.path[0][:-2]+"backgrounds")
sys.path.append(sys.path[0][:-2])
import backgrounds
import character

class BackgroundWindow(QWidget):
	def __init__(self, parent):	
		QWidget.__init__(self)
		self.tab_window = parent
		self.setup()	


	def complete_background(self):

		self.addedtraits = []

		i = 1
		while i < self.fbox.count():
			self.addedtraits.append(self.fbox.itemAt(i).widget().text())
			i = i + 2

		#print(self.addedtraits)

		self.traits_object = backgrounds.Traits(self.addedtraits[0],self.addedtraits[1],self.addedtraits[2],self.addedtraits[3],self.addedtraits[4],self.addedAlignments)
		self.backgrounds_object = backgrounds.Background(self.addedSkills,self.other,self.addedLanguages,self.addedFeatures,self.traits_object)
		name = self.fbox.itemAt(4).widget().text()
		flaws = self.fbox.itemAt(3).widget().text()
		bonds = self.fbox.itemAt(2).widget().text()
		ideals = self.fbox.itemAt(1).widget().text()
		personality = self.fbox.itemAt(0).widget().text()
		stats = self.tab_window.main_window.stats_object
		race = self.tab_window.main_window.race
		char_class = self.tab_window.main_window.classes

		self.tab_window.main_window.character_object = character.Character(name,stats,race,char_class,self.backgrounds_object)

		all_fields = self.tab_window.main_window.character_object.get_form_fields()

		#Create FDF file with these fields
		fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
		fdf_file = open("file_fdf.fdf","w") 
		fdf_file.write(fdf_data) 
		fdf_file.close()
		#Run pdftk system command to populate the pdf file. The file "file_fdf.fdf" is pushed in to "input_pdf.pdf" thats generated as a new "output_pdf.pdf" file.
		pdftk_cmd = "pdftk ../charsheet.pdf fill_form file_fdf.fdf output ../output_pdf.pdf"
		os.system(pdftk_cmd)

		
		self.tab_window.main_window.character_object = character.Character(name,stats,race,char_class,self.backgrounds_object)
		self.l4.setText(self.tab_window.main_window.character_object.__str__())



	def add_personality(self):
		self.layout5 = QWidget()
		self.fbox = QFormLayout()
		self.vbox6 = QVBoxLayout()
		self.personality_attributes = ["Personality","Ideals","Bonds","Flaws", "Name"]
		self.b4 = QPushButton("Finish")
		self.b4.clicked.connect(self.complete_background)

		self.l4 = QTextEdit()
		self.l4.setText("Fill Out Traits")
		self.l4.setReadOnly(True)
		self.vbox6.addWidget(self.l4)


		i = 0
		while i < len(self.personality_attributes):
			self.temp_label = QLabel()
			self.temp_label.setText(self.personality_attributes[i])
			self.temp_label.setAlignment(Qt.AlignCenter)
			self.temp_textEdit = QLineEdit()
			self.fbox.addRow(self.temp_label,self.temp_textEdit)
			i = i + 1

		self.vbox6.addLayout(self.fbox)
		self.vbox6.addWidget(self.b4)


		i = 0 
		while i < len(self.alignments)+1:
			if self.vbox5.itemAt(i+1).widget().isChecked():
				self.addedAlignments = self.vbox5.itemAt(i+1).widget().text()
			i = i + 1

		#print(self.addedAlignments)


		self.layout5.setLayout(self.vbox6)
		self.stacked_layout.addWidget(self.layout5)
		self.stacked_layout.setCurrentIndex(4)


	def add_alignment(self):
		self.layout4 = QWidget()
		self.vbox5 = QVBoxLayout()
		self.alignments = ["Lawful Good","Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
		self.b3 = QPushButton("Go To Traits")
		self.b3.clicked.connect(self.add_personality)

		self.l3 = QLabel()
		self.l3.setText("Choose a Background Alignment")
		self.l3.setAlignment(Qt.AlignCenter)

		self.vbox5.addWidget(self.l3)

		i = 0
		while i < len(self.alignments):
			self.vbox5.addWidget(QCheckBox(self.alignments[i]))
			self.vbox5.itemAt(i+1).setAlignment(Qt.AlignCenter)
			i = i + 1

		self.vbox5.addWidget(self.b3)


		self.addedFeatures = []
		i = 0 
		while i < len(self.features)+1:
			if self.vbox4.itemAt(i+1).widget().isChecked():
				self.addedFeatures.append(self.vbox4.itemAt(i+1).widget().text())
			i = i + 1

		#print(self.addedFeatures)

		self.layout4.setLayout(self.vbox5)
		self.stacked_layout.addWidget(self.layout4)
		self.stacked_layout.setCurrentIndex(3)


	def add_feature(self):
		self.layout3 = QWidget()
		self.vbox4 = QVBoxLayout()
		self.features = ["Shelter of the Faithful", "False Identity", "Criminal Contact", "By Popular Demand", "Rustic Hospitality", "Guild Membership", "Discovery", "Position of Priviledge", "Wonderer", "Researcher", "Ship's Passage", "Military Rank", "City Secrets"]
		self.b2 = QPushButton("Go To Alignments")
		self.b2.clicked.connect(self.add_alignment)


		self.l2 = QLabel()
		self.l2.setText("Choose a Background Feature")
		self.l2.setAlignment(Qt.AlignCenter)

		self.vbox4.addWidget(self.l2)

		i = 0
		while i < len(self.features):
			self.vbox4.addWidget(QCheckBox(self.features[i]))
			self.vbox4.itemAt(i+1).setAlignment(Qt.AlignCenter)
			i = i + 1


		self.addedLanguages = []


		i = 0 
		while i < len(self.languages):
			if self.vbox2.itemAt(i+1).widget().isChecked():
				self.addedLanguages.append(self.vbox2.itemAt(i+1).widget().text())
			i = i + 1


		self.other	= []

		i = 0
		while i < len(self.tools):
			if self.vbox3.itemAt(i+1).widget().isChecked():
				self.other.append(self.vbox3.itemAt(i+1).widget().text())
			i = i + 1

		#print(self.addedLanguages)
		#print(self.other)

		self.vbox4.addWidget(self.b2)

		self.layout3.setLayout(self.vbox4)
		self.stacked_layout.addWidget(self.layout3)
		self.stacked_layout.setCurrentIndex(2)




	def add_skills(self):
		self.layout2 = QWidget()
		self.hbox = QHBoxLayout()
		self.vbox2 = QVBoxLayout()
		self.vbox3 = QVBoxLayout()
		self.gbox = QGridLayout()

		self.l1 = QLabel()
		self.l1.setText("Choose Two More Profincies")
		self.l1.setAlignment(Qt.AlignCenter)

		self.b1 = QPushButton("Go To Features")
		self.b1.clicked.connect(self.add_feature)

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



		self.addedSkills = []

		i = 0 
		while i < len(self.skills)+1:
			if self.vbox.itemAt(i+1).widget().isChecked():
				self.addedSkills.append(self.vbox.itemAt(i+1).widget().text())
			i = i + 1

		#print(self.addedSkills)

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
		self.confirmSkillsButton = QPushButton("Go To Languages/Tools")
		self.confirmSkillsButton.clicked.connect(self.add_skills)
		self.skills = ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"] 

		self.vbox.addWidget(self.skills_label)

		i = 0
		while i < len(self.skills):
			self.temp_cb = QCheckBox(self.skills[i])
			self.vbox.addWidget(self.temp_cb)
			self.vbox.itemAt(i+1).setAlignment(Qt.AlignCenter)
			i = i + 1

		self.vbox.addWidget(self.confirmSkillsButton)

		self.layout1 = QWidget()
		self.layout1.setLayout(self.vbox)


		self.stacked_layout.addWidget(self.layout1)

		self.setLayout(self.stacked_layout)
		self.show()








