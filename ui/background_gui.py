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

		self.l4.setText("Character outputted to pdf")

		
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

		self.lawful_good_tt = "A lawful good character acts as a good person is expected or required to act.\n He combines a commitment to oppose evil with the discipline to fight relentlessly.\n He tells the truth, keeps his word, helps those in need, and speaks out against injustice.\n A lawful good character hates to see the guilty go unpunished. " 
		self.neutral_good_tt = "A neutral good character does the best that a good person can do.\n He is devoted to helping others.\n He works with kings and magistrates but does not feel beholden to them.\n "
		self.chaotic_good_tt = "A chaotic good character acts as his conscience directs him with little regard for what others expect of him.\n He makes his own way, but he's kind and benevolent.\n He believes in goodness and right but has little use for laws and regulations.\n He hates it when people try to intimidate others and tell them what to do.\n He follows his own moral compass, which, although good, may not agree with that of society. "
		self.lawful_neutral_tt = "A lawful neutral character acts as law, tradition, or a personal code directs her.\n Order and organization are paramount to her.\n She may believe in personal order and live by a code or standard, or she may believe in order for all and favor a strong, organized government. "
		self.neutral_tt = "A neutral character does what seems to be a good idea.\n She doesn't feel strongly one way or the other when it comes to good vs. evil or law vs. chaos.\n Most neutral characters exhibit a lack of conviction or bias rather than a commitment to neutrality.\n Such a character thinks of good as better than evil-after all, she would rather have good neighbors and rulers than evil ones.\n Still, she's not personally committed to upholding good in any abstract or universal way.\nSome neutral characters, on the other hand, commit themselves philosophically to neutrality.\n They see good, evil, law, and chaos as prejudices and dangerous extremes.\n They advocate the middle way of neutrality as the best, most balanced road in the long run."
		self.chaotic_neutral_tt = "A chaotic neutral character follows his whims.\n He is an individualist first and last.\n He values his own liberty but doesn't strive to protect others' freedom.\n He avoids authority, resents restrictions, and challenges traditions.\n A chaotic neutral character does not intentionally disrupt organizations as part of a campaign of anarchy.\n To do so, he would have to be motivated either by good (and a desire to liberate others) or evil (and a desire to make those different from himself suffer).\n A chaotic neutral character may be unpredictable, but his behavior is not totally random.\n He is not as likely to jump off a bridge as to cross it. "
		self.lawful_evil_tt = "A lawful evil villain methodically takes what he wants within the limits of his code of conduct without regard for whom it hurts.\n He cares about tradition, loyalty, and order but not about freedom, dignity, or life.\n He plays by the rules but without mercy or compassion.\n He is comfortable in a hierarchy and would like to rule, but is willing to serve.\n He condemns others not according to their actions but according to race, religion, homeland, or social rank.\n He is loath to break laws or promises. "
		self.neutral_evil_tt = "A neutral evil villain does whatever she can get away with.\n She is out for herself, pure and simple.\n She sheds no tears for those she kills, whether for profit, sport, or convenience.\n She has no love of order and holds no illusion that following laws, traditions, or codes would make her any better or more noble.\n On the other hand, she doesn't have the restless nature or love of conflict that a chaotic evil villain has. "
		self.chaotic_evil_tt = "A chaotic evil character does whatever his greed, hatred, and lust for destruction drive him to do.\n He is hot-tempered, vicious, arbitrarily violent, and unpredictable.\n If he is simply out for whatever he can get, he is ruthless and brutal.\n If he is committed to the spread of evil and chaos, he is even worse.\n Thankfully, his plans are haphazard, and any groups he joins or forms are poorly organized.\n Typically, chaotic evil people can be made to work together only by force, and their leader lasts only as long as he can thwart attempts to topple or assassinate him."

		self.alignment_descriptions = []
		self.alignment_descriptions.append(self.lawful_good_tt)	
		self.alignment_descriptions.append(self.neutral_good_tt)
		self.alignment_descriptions.append(self.chaotic_good_tt)
		self.alignment_descriptions.append(self.lawful_neutral_tt)
		self.alignment_descriptions.append(self.neutral_tt)
		self.alignment_descriptions.append(self.chaotic_neutral_tt)
		self.alignment_descriptions.append(self.lawful_evil_tt)
		self.alignment_descriptions.append(self.neutral_evil_tt)
		self.alignment_descriptions.append(self.chaotic_evil_tt)	

		self.l3 = QLabel()
		self.l3.setText("Choose a Background Alignment")
		self.l3.setAlignment(Qt.AlignCenter)

		self.vbox5.addWidget(self.l3)

		i = 0
		while i < len(self.alignments):
			self.vbox5.addWidget(QCheckBox(self.alignments[i]))
			self.vbox5.itemAt(i+1).setAlignment(Qt.AlignCenter)
			self.vbox5.itemAt(i+1).widget().setToolTip(self.alignment_descriptions[i])
			i = i + 1

		self.vbox5.addWidget(self.b3)


		self.addedFeatures = []
		i = 0 
		while i < len(self.features)+1:
			if self.vbox4.itemAt(i+1).widget().isChecked():
				self.addedFeatures = [self.vbox4.itemAt(i+1).widget().text()]

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



		self.soh_tt = "You command the respect of those who share your faith, and you can\n perform the religious ceremonies of your deity. You and your adventuring companions can\n expect to receive free healing and care at a temple, shrine, or other established presence\n of your faith, though you must provide any material components needed for spells.\n Those who share your religion will support you (but only you) at a modest lifestyle."
		self.fi_tt = "You have created a second identity that includes documentation, established\n acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge\n documents including official papers and personal letters, as long as you have seen an\n example of the kind of document or the handwriting you are trying to copy."
		self.cc_tt = "You have a reliable and trustworthy contact who acts as your liaison to a\n network of other criminals. You know how to get messages to and from your contact, even over\n great distances; specifically, you know the local messengers, corrupt caravan masters,\n and seedy sailors who can deliver messages for you."
		self.pd_tt = "You can always find a place to perform, usually in an inn or tavern but\n possibly with a circus, at a theater, or even in a noble’s court. At such a place, you receive free\n lodging and food of a modest or comfortable standard (depending on the quality of the\n  establishment), as long as you perform each night. In addition, your performance makes you\n something of a local figure. When strangers recognize you in a town where you have performed,\n  they typically take a liking to you."
		self.rh_tt = "Since you come from the ranks of the common folk, you fit in among them\n with ease. You can find a place to hide, rest, or recuperate among other commoners,\n unless you have shown yourself to be a danger to them. They will shield you from the law or\n anyone else searching for you, though they will not risk their lives for you."
		self.gm_tt = "As an established and respected member of a guild, you can rely on\n certain benefits that membership provides. Your fellow guild members will provide you with\n lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a\n guildhall offers a central place to meet other members of your profession, which can be a good\n place to meet potential patrons, allies, or hirelings. Guilds often wield tremendous political power.\n If you are accused of a crime, your guild will support you if a good case can be made\n for your innocence or the crime is justifiable. You can also gain access to powerful political\n figures through the guild, if you are a member in good standing. Such connections might require\n the donation of money or magic items to the guild’s coffers. You must pay dues of 5 gp\n per month to the guild. If you miss payments, you must make up back dues to remain in\n the guild’s good graces. "
		self.d_tt = "The quiet seclusion of your extended hermitage gave you access to a unique and\n powerful discovery. The exact nature of this revelation depends on the nature of your seclusion.\nIt might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might\n have uncovered a fact that has long been forgotten, or unearthed some relic of the past\n that could rewrite history. It might be information that would be damaging to the people\n who or consigned you to exile, and hence the reason for your return to society. Work with your\n DM to determine the details of your discovery and its impact on the campaign."
		self.pp_tt = "Thanks to your noble birth, people are inclined to think the best of you. \n You are welcome in high society, and people assume you have the right to be wherever you are.\n The common folk make every effort to accommodate you and avoid your displeasure,\n and other people of high birth treat you as a member of the same social sphere. You can secure\n an audience with a local noble if you need to."
		self.w_tt = "You have an excellent memory for maps and geography, and you can always recall\n the general layout of terrain, settlements, and other features around you. In addition, you\n can find food and fresh water for yourself and up to five other people each day, provided\n that the land offers berries, small game, water, and so forth."
		self.r_tt = "When you attempt to learn or recall a piece of lore, if you do not know that\n information, you often know where and from whom you can obtain it. Usually, this information\n comes from a library, scriptorium, university, or a sage or other learned person or creature. Your\n  DM might rule that the knowledge you seek is secreted away in an almost inaccessible\n place, or that it simply cannot be found. Unearthing the deepest secrets of the\n multiverse can require an adventure or even a whole campaign."
		self.sp_tt = "When you need to, you can secure free passage on a sailing ship for yourself\n and your adventuring companions. You might sail on the ship you served on, or\n another ship you have good relations with (perhaps one captained by a former crewmate). \n Because you’re calling in a favor, you can’t be certain of a schedule or route that will meet your\n every need. Your Dungeon Master will determine how long it takes to get where you need to go.\n In return for your free passage, you and your companions are expected to assist the crew\n during the voyage."
		self.mr_tt = "You have a military rank from your career as a soldier. Soldiers loyal to your\n former military organization still recognize your authority and influence, and they defer to you if\n they are of a lower rank. You can invoke your rank to exert influence over other soldiers and\n requisition simple equipment or horses for temporary use. You can also usually gain access to\n friendly military encampments and fortresses where your rank is recognized."
		self.cs_tt = "You know the secret patterns and flow to cities and can find passages through\n the urban sprawl that others would miss. When you are not in combat, you (and companions\n you lead) can travel between any two locations in the city twice as fast as your speed would\n normally allow."

		self.feature_descriptions = []
		self.feature_descriptions.append(self.soh_tt)
		self.feature_descriptions.append(self.fi_tt)
		self.feature_descriptions.append(self.cc_tt)
		self.feature_descriptions.append(self.pd_tt)
		self.feature_descriptions.append(self.rh_tt)
		self.feature_descriptions.append(self.gm_tt)
		self.feature_descriptions.append(self.d_tt)
		self.feature_descriptions.append(self.pp_tt)
		self.feature_descriptions.append(self.w_tt)
		self.feature_descriptions.append(self.r_tt)
		self.feature_descriptions.append(self.sp_tt)
		self.feature_descriptions.append(self.mr_tt)
		self.feature_descriptions.append(self.cs_tt)



		self.l2 = QLabel()
		self.l2.setText("Choose a Background Feature")
		self.l2.setAlignment(Qt.AlignCenter)

		self.vbox4.addWidget(self.l2)

		i = 0
		while i < len(self.features):
			self.vbox4.addWidget(QCheckBox(self.features[i]))
			self.vbox4.itemAt(i+1).setAlignment(Qt.AlignCenter)
			self.vbox4.itemAt(i+1).widget().setToolTip(self.feature_descriptions[i])
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








