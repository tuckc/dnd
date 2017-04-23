#UserInterface.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from race_gui import *
from stats_gui import *
from class_gui import *
from background_gui import *
import sys



class DND_CC_Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle("Dungeons and Dragons Character Creator")
		self.setup()

	def setup(self):
		self.raceset = False
		self.tab_widget = TabView(self)
		self.setCentralWidget(self.tab_widget)
		self.Menu = self.menuBar()
		self.quitmenu = self.Menu.addMenu("Quit")
		self.exitButton = QAction(QIcon('exit24.png'),'Exit', self)
		self.exitButton.setShortcut('Ctrl+Q')
		self.exitButton.setStatusTip("Exit Application")
		self.exitButton.triggered.connect(self.close)
		self.quitmenu.addAction(self.exitButton)
		self.racepagecount = 0
		self.classpagecount = 0
		self.statspagecount = 0
		self.show()



class TabView(QTabWidget):
	def __init__(self, parent):
		QTabWidget.__init__(self,parent)
		self.main_window = parent
		self.setup()

	def setup(self):
		self.addTab(WelcomeWindow(self), '&Welcome!')

		

		

class WelcomeWindow(QWidget):
	def __init__(self,parent):
		QTabWidget.__init__(self)	
		self.tab_window = parent
		self.start_button = QPushButton("Start")
		self.quit_button = QuitButton(self)
		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.label = QLabel(self)
		self.pixmap = QPixmap('welcome.jpeg')
		self.label.setPixmap(self.pixmap)
		self.picbox.addWidget(self.label)



		self.start_button.clicked.connect(self.nextpage)

		self.buttonbox.addWidget(self.start_button)
		self.buttonbox.addWidget(self.quit_button)
		
		self.setLayout(self.vbox)
		self.vbox.addLayout(self.picbox)
		self.vbox.addLayout(self.buttonbox)
		self.show()


	def nextpage(self):
		if self.tab_window.main_window.racepagecount < 1:
			self.tab_window.RaceWindowObject = RaceWindow(self.tab_window)
			self.tab_window.addTab(self.tab_window.RaceWindowObject, "&Race")
			self.tab_window.setCurrentIndex(1)
			self.tab_window.main_window.racepagecount = 1
		else:
			self.tab_window.setCurrentIndex(1)


		




class QuitButton(QPushButton):
	def __init__(self, parent):
		QPushButton.__init__(self, parent)
		self.setText("Quit")
		self.clicked.connect(qApp.quit)



 


if __name__ == "__main__":
	'''
	Code from slide 15 of lecture 17
	'''
	app = QApplication(sys.argv)
	main_window = DND_CC_Window()
	app.exec_()

