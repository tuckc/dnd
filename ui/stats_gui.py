from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import sys
#<<<<<<< HEAD
#sys.path = sys.path[:7]
#=======
#>>>>>>> fe578e1809b9c74567c3d5fc60540bd60ba54b58
sys.path.append(sys.path[0][:-2]+"stats")
sys.path.append(sys.path[0][:-2])
import stats
import class_gui
import stats_gui
from random import *

class StatsWindow(QWidget):
	def __init__(self, parent):	
		QWidget.__init__(self)
		self.tab_window = parent
		self.errnum = 0
		self.setup()

	def dice_rolled(self):
		self.rolls = []
		self.totals = []

		i = 0
		j = 0
		while j < 6:
			while i < 4:
				self.rolls.append(randint(1,6))
				i = i +1
			#print(self.rolls)
			num1 = max(self.rolls)
			self.rolls.remove(num1)
			num2 = max(self.rolls)
			self.rolls.remove(num2)
			num3 = max(self.rolls)
			self.totals.append([(num1+num2+num3), False])
			i = 0
			self.rolls = []
			j = j+1


		self.confirmButton = QPushButton("Assign Stats")
		self.confirmButton.clicked.connect(self.assign_stats)
		self.total1Label.setText(str(self.totals[0][0]))
		self.total2Label.setText(str(self.totals[1][0]))
		self.total3Label.setText(str(self.totals[2][0]))
		self.total4Label.setText(str(self.totals[3][0]))
		self.total5Label.setText(str(self.totals[4][0]))
		self.total6Label.setText(str(self.totals[5][0]))
		self.rollButton.setText("Re-Roll")
		self.gbox2.addWidget(self.confirmButton,1,2,1,1)



	def confirm_stats(self):

		self.vbox = QVBoxLayout()
		self.done_label = QLabel(self)
		self.done_label.setText("Stats Added")
		self.stat_info = QLabel()
		self.labelbox = QHBoxLayout()
		self.labelbox.addWidget(self.done_label)
		self.labelbox.addWidget(self.stat_info)

		self.vbox.addLayout(self.labelbox)

		self.buttonbox = QHBoxLayout()

		self.confirmButton = QPushButton("Confirm")
		self.confirmButton.clicked.connect(self.confirm)

		self.restartButton = QPushButton("Restart")
		self.restartButton.clicked.connect(self.restart)

		self.buttonbox.addWidget(self.restartButton)
		self.buttonbox.addWidget(self.confirmButton)
		

		self.vbox.addLayout(self.buttonbox)

		self.show()



		self.layout3 = QWidget()
		self.layout3.setLayout(self.vbox)
		self.stacked_layout.addWidget(self.layout3)


		if self.check_stats():
			race = self.tab_window.main_window.race
			self.tab_window.main_window.stats_object = stats.Stats(race,self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma)
			self.stacked_layout.setCurrentIndex(2)
			self.stat_info.setText(self.tab_window.main_window.stats_object.__str__())

			
		
		
	def check_totals(self, num):
		for total in self.totals:
			if num == total[0] and total[1] == False:
				total[1] = True
				return True
			else:
				pass
				#print ("num, total[0], total[1]", num, total[0], total[1])
		else:
			#print("self.totals", self.totals)
			return False				

	def resetTotals(self):
		for total in self.totals:
			total[1] = False

	def check_stats(self):
		try:
			if self.check_totals(int(self.strengthInput.text())):
				self.strength = int(self.strengthInput.text())
				self.statsLabel.setText("Stats")
			else:
				self.statsLabel.setText("YOU MUST INPUT VALUES BASED ON YOUR ROLLED STATS!")
				self.resetTotals()
				return False

			if self.check_totals(int(self.dexterityInput.text())):
				self.dexterity = int(self.dexterityInput.text())
				self.statsLabel.setText("Stats")
			else:
				self.statsLabel.setText("YOU MUST INPUT VALUES BASED ON YOUR ROLLED STATS!")
				self.resetTotals()
				return False	

			if self.check_totals(int(self.constitutionInput.text())):
				self.constitution = int(self.constitutionInput.text())
				self.statsLabel.setText("Stats")
			else:
				self.statsLabel.setText("YOU MUST INPUT VALUES BASED ON YOUR ROLLED STATS!")
				self.resetTotals()
				return False

			if self.check_totals(int(self.intelligenceInput.text())):
				self.intelligence = int(self.intelligenceInput.text())
				self.statsLabel.setText("Stats")
			else:
				self.statsLabel.setText("YOU MUST INPUT VALUES BASED ON YOUR ROLLED STATS!")
				self.resetTotals()
				return False

			if self.check_totals(int(self.wisdomInput.text())):
				self.wisdom = int(self.wisdomInput.text())
				self.statsLabel.setText("Stats")
			else:
				self.statsLabel.setText("YOU MUST INPUT VALUES BASED ON YOUR ROLLED STATS!")
				self.resetTotals()
				return False

			if self.check_totals(int(self.charismaInput.text())):
				self.charisma = int(self.charismaInput.text())
				self.statsLabel.setText("Stats")
			else:
				self.statsLabel.setText("YOU MUST INPUT VALUES BASED ON YOUR ROLLED STATS!")
				self.resetTotals()
				return False

			return True

		except ValueError:
			self.statsLabel.setText("YOU MUST INPUT INTEGER VALUES!")
			self.resetTotals()
			return False
		

		


	def confirm(self):
		if self.tab_window.main_window.classpagecount < 1:
			self.tab_window.ClassWindowObject = class_gui.ClassWindow(self.tab_window)
			self.tab_window.addTab(self.tab_window.ClassWindowObject, "&Classes")	
			self.tab_window.setCurrentIndex(3)
			self.tab_window.main_window.classpagecount = 1
		else:
			self.tab_window.setCurrentIndex(3)

	def restart(self):
		self.tab_window.removeTab(2)
		self.tab_window.StatsWindowObject = self.tab_window.main_window.returnStatsWindow(self.tab_window)
		self.tab_window.insertTab(2,self.tab_window.StatsWindowObject, "&Stats")
		self.tab_window.setCurrentIndex(2)
		self.tab_window.main_window.statspagecount = 1
		


	def assign_stats(self):
		self.fbox = QFormLayout()
		self.gbox3 = QGridLayout()
		self.assignButton = QPushButton("Confirm")
		self.assignButton.clicked.connect(self.confirm_stats)
		self.hbox2 = QHBoxLayout()

		self.l0 = QLabel(self)
		self.l0.setText("Your Numbers: ")
		self.l1 = QLabel(self)
		self.l1.setText(str(self.totals[0][0]))
		self.l2 = QLabel(self)
		self.l2.setText(str(self.totals[1][0]))
		self.l3 = QLabel(self)
		self.l3.setText(str(self.totals[2][0]))
		self.l4 = QLabel(self)
		self.l4.setText(str(self.totals[3][0]))
		self.l5 = QLabel(self)
		self.l5.setText(str(self.totals[4][0]))
		self.l6 = QLabel(self)
		self.l6.setText(str(self.totals[5][0]))


		self.hbox2.addWidget(self.l0)
		self.hbox2.addWidget(self.l1)
		self.hbox2.addWidget(self.l2)
		self.hbox2.addWidget(self.l3)
		self.hbox2.addWidget(self.l4)
		self.hbox2.addWidget(self.l5)
		self.hbox2.addWidget(self.l6)





		self.statsLabelsBox = QVBoxLayout()
		self.statsInputsBox = QVBoxLayout()

		self.statsLabel = QLabel(self)
		self.statsLabel.setText("Stats")
		self.strengthLabel = QLabel(self)
		self.strengthLabel.setText("Strength")
		self.dexterityLabel = QLabel(self)
		self.dexterityLabel.setText("Dexterity")
		self.constitutionLabel = QLabel(self)
		self.constitutionLabel.setText("Constitution")
		self.intelligenceLabel = QLabel(self)
		self.intelligenceLabel.setText("Intelligence")
		self.wisdomLabel = QLabel(self)
		self.wisdomLabel.setText("Wisdom")
		self.charismaLabel = QLabel(self)
		self.charismaLabel.setText("Charisma")

		self.strengthInput = QLineEdit()
		self.dexterityInput = QLineEdit()
		self.constitutionInput = QLineEdit()
		self.intelligenceInput = QLineEdit()
		self.wisdomInput = QLineEdit()
		self.charismaInput = QLineEdit()




		self.statsLabel.setAlignment(Qt.AlignCenter)
		self.strengthLabel.setAlignment(Qt.AlignCenter)
		self.dexterityLabel.setAlignment(Qt.AlignCenter)
		self.constitutionLabel.setAlignment(Qt.AlignCenter)
		self.intelligenceLabel.setAlignment(Qt.AlignCenter)
		self.wisdomLabel.setAlignment(Qt.AlignCenter)
		self.charismaLabel.setAlignment(Qt.AlignCenter)


		#self.statsLabel.setAlignment(Qt.AlignCenter)
		self.strengthInput.setAlignment(Qt.AlignCenter)
		self.dexterityInput.setAlignment(Qt.AlignCenter)
		self.constitutionInput.setAlignment(Qt.AlignCenter)
		self.intelligenceInput.setAlignment(Qt.AlignCenter)
		self.wisdomInput.setAlignment(Qt.AlignCenter)
		self.charismaInput.setAlignment(Qt.AlignCenter)


		#self.statsLabelsBox.addWidget(self.statsLabel)
		self.fbox.addRow(self.strengthLabel,self.strengthInput)
		self.fbox.addRow(self.dexterityLabel, self.dexterityInput)
		self.fbox.addRow(self.constitutionLabel, self.constitutionInput)
		self.fbox.addRow(self.intelligenceLabel,self.intelligenceInput)
		self.fbox.addRow(self.wisdomLabel,self.wisdomInput)
		self.fbox.addRow(self.charismaLabel,self.charismaInput)


		#self.hbox2.addLayout(self.statsLabelsBox)
		#self.hbox2.addLayout(self.statsInputsBox)

		self.gbox3.addWidget(self.statsLabel,1,1,1,1)
		self.gbox3.addLayout(self.hbox2,2,1,1,1)
		self.gbox3.addLayout(self.fbox,3,1,5,1)
		self.gbox3.addWidget(self.assignButton,8,1,1,1)

		self.layout2 = QWidget()
		self.layout2.setLayout(self.gbox3)

		self.stacked_layout.addWidget(self.layout2)

		self.stacked_layout.setCurrentIndex(1)

		



	def setup(self):

		self.stacked_layout = QStackedLayout()

		self.gbox1 = QGridLayout()
		self.gbox2 = QGridLayout()
		self.hbox = QHBoxLayout()
		self.rollsBox = QVBoxLayout()
		self.totalsBox = QVBoxLayout()

		self.rollLabel = QLabel(self)
		self.rollLabel.setText("Roll Attempts")
		self.roll1Label = QLabel(self)
		self.roll1Label.setText("Roll 1")
		self.roll2Label = QLabel(self)
		self.roll2Label.setText("Roll 2")
		self.roll3Label = QLabel(self)
		self.roll3Label.setText("Roll 3")
		self.roll4Label = QLabel(self)
		self.roll4Label.setText("Roll 4")
		self.roll5Label = QLabel(self)
		self.roll5Label.setText("Roll 5")
		self.roll6Label = QLabel(self)
		self.roll6Label.setText("Roll 6")

		self.totalLabel = QLabel(self)
		self.totalLabel.setText("Totals")
		self.total1Label = QLabel(self)
		self.total2Label = QLabel(self)
		self.total3Label = QLabel(self)
		self.total4Label = QLabel(self)
		self.total5Label = QLabel(self)
		self.total6Label = QLabel(self)
		
		self.rollButton = QPushButton("Roll Dice")
		self.rollButton.clicked.connect(self.dice_rolled)

		self.rollLabel.setAlignment(Qt.AlignCenter)
		self.roll1Label.setAlignment(Qt.AlignCenter)
		self.roll2Label.setAlignment(Qt.AlignCenter)
		self.roll3Label.setAlignment(Qt.AlignCenter)
		self.roll4Label.setAlignment(Qt.AlignCenter)
		self.roll5Label.setAlignment(Qt.AlignCenter)
		self.roll6Label.setAlignment(Qt.AlignCenter)
		self.totalLabel.setAlignment(Qt.AlignCenter)
		self.total1Label.setAlignment(Qt.AlignCenter)
		self.total2Label.setAlignment(Qt.AlignCenter)
		self.total3Label.setAlignment(Qt.AlignCenter)
		self.total4Label.setAlignment(Qt.AlignCenter)
		self.total5Label.setAlignment(Qt.AlignCenter)
		self.total6Label.setAlignment(Qt.AlignCenter)


		self.rollsBox.addWidget(self.rollLabel)
		self.rollsBox.addWidget(self.roll1Label)
		self.rollsBox.addWidget(self.roll2Label)
		self.rollsBox.addWidget(self.roll3Label)
		self.rollsBox.addWidget(self.roll4Label)
		self.rollsBox.addWidget(self.roll5Label)
		self.rollsBox.addWidget(self.roll6Label)


		self.totalsBox.addWidget(self.totalLabel)
		self.totalsBox.addWidget(self.total1Label)
		self.totalsBox.addWidget(self.total2Label)
		self.totalsBox.addWidget(self.total3Label)
		self.totalsBox.addWidget(self.total4Label)
		self.totalsBox.addWidget(self.total5Label)
		self.totalsBox.addWidget(self.total6Label)


		self.hbox.addLayout(self.rollsBox)
		self.hbox.addLayout(self.totalsBox)
		self.gbox2.addWidget(self.rollButton,1,1,1,1)
		self.gbox1.addLayout(self.hbox,1,1,4,1)
		self.gbox1.addLayout(self.gbox2,5,1,1,1)

		self.layout1 = QWidget()
		self.layout1.setLayout(self.gbox1)
		self.stacked_layout.addWidget(self.layout1)

		self.setLayout(self.stacked_layout) 
		self.show()


if __name__ == "__main__":
	'''
	Code from slide 15 of lecture 17
	'''
	app = QApplication(sys.argv)
	main_window = StatsWindow()
	app.exec_()

