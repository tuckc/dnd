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
		self.tab_widget = TabView(self)
		self.setCentralWidget(self.tab_widget)
		self.Menu = self.menuBar()
		self.quitmenu = self.Menu.addMenu("Quit")
		self.exitButton = QAction(QIcon('exit24.png'),'Exit', self)
		self.exitButton.setShortcut('Ctrl+Q')
		self.exitButton.setStatusTip("Exit Application")
		self.exitButton.triggered.connect(self.close)
		self.quitmenu.addAction(self.exitButton)
		self.show()



class TabView(QTabWidget):
	def __init__(self, parent):
		QTabWidget.__init__(self,parent)
		self.main_window = parent
		self.setup()

	def setup(self):
		self.addTab(WelcomeWindow(self), 'Welcome!')
		self.addTab(RaceWindow(self), 'Race')
		#self.setTabEnabled(2, False)
		self.addTab(StatsWindow(self), 'Stats')
		#self.setTabEnabled(3, False)
		self.addTab(ClassWindow(self), 'Class')
		#self.setTabEnabled(4, False)
		self.addTab(BackgroundWindow(self), 'Background')
		#self.setTabEnabled(5, False)
		

class WelcomeWindow(QWidget):
	def __init__(self,parent):
		QTabWidget.__init__(self)	
		self.tab_window = parent
		#self.start_button = StartButton(self)
		self.quit_button = QuitButton(self)
		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.label = QLabel(self)
		self.pixmap = QPixmap('welcome.jpeg')
		self.label.setPixmap(self.pixmap)
		self.picbox.addWidget(self.label)

		'''self.label2 = QLabel(self)
		self.pixmap2 = QPixmap('welcometitle.jpg')
		self.pixmap2 = self.pixmap2.scaledToWidth(self.width())
		self.label2.setPixmap(self.pixmap2)
		self.picbox.addWidget(self.label2)
		self.picbox.setAlignment(self.label2, Qt.AlignCenter)'''


		#self.buttonbox.addWidget(self.start_button)
		self.buttonbox.addWidget(self.quit_button)
		
		self.setLayout(self.vbox)
		self.vbox.addLayout(self.picbox)
		self.vbox.addLayout(self.buttonbox)
		self.show()
	





'''class StartButton(QPushButton):
	def __init__(self, parent):
		QPushButton.__init__(self, parent)
		self.setText("Start")
		self.parent = parent
		self.clicked.connect(self.handleStart)

	def handleStart(self):
		self.parent.tab_window.setTabEnabled(1,True)
'''

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

