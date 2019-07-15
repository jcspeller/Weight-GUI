from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

import os

class WeightCalculator(QTabWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle('Raw Weight to Number of Plates')
		
		# Getting application's icon
		scriptDir = os.path.dirname(os.path.realpath('barbell.png'))
		self.setWindowIcon(QtGui.QIcon(scriptDir+os.path.sep+'barbell.png'))
		
		# Creating Weightlifting Image
		self.picture = QLabel(self)
		self.pixmap = QPixmap('weightlifter.png')
		self.pixmap = self.pixmap.scaled(280,280,Qt.KeepAspectRatio,Qt.FastTransformation)
		self.picture.setPixmap(self.pixmap)
		self.picture.move(320,210)

		# Creating the tabs, text field, and button
		self.tabPounds = QWidget()
		self.tabKilograms = QWidget()
		
		# Creating pounds table
		self.numPoundsPlatesTable = QTableWidget(6,2)
		self.numPoundsPlatesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

		# Creating kilograms table
		self.numKilogramsPlatesTable = QTableWidget(6,2)
		self.numKilogramsPlatesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

		# Pounds widgets
		self.textFieldPounds = QLineEdit('')
		self.textFieldPounds.setAlignment(Qt.AlignHCenter)
		self.textFieldPounds.setMaxLength(5)
		self.calculateButtonPounds = QPushButton('Calculate')
		
		# Kilograms widgets
		self.textFieldKilograms = QLineEdit('')
		self.textFieldKilograms.setAlignment(Qt.AlignHCenter)
		self.textFieldKilograms.setMaxLength(5)
		self.calculateButtonKilograms = QPushButton('Calculate')
		
		# Adding tabs to main tab widget
		self.addTab(self.tabPounds, 'Pounds')
		self.addTab(self.tabKilograms, 'Kilograms')
		self.tabPoundsUI()
		self.tabKilogramsUI()
		
		# Centering application in middle of screen
		self.setFixedSize(515,500)
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
	def tabPoundsUI(self):
		# Creating the layout and adding text field, button, and table to it
		layout = QGridLayout()
		layout.addWidget(QLabel('Input the raw weight you want converted'),0,0, Qt.AlignHCenter)
		layout.addWidget(QLabel('minus the bar'),1,0, Qt.AlignHCenter)
		layout.addWidget(self.textFieldPounds,2,0, Qt.AlignTop)
		layout.addWidget(self.calculateButtonPounds,3,0, Qt.AlignCenter)
		layout.addWidget(self.numPoundsPlatesTable,4,0)
		self.numPoundsPlatesTable.setHorizontalHeaderItem(0,QTableWidgetItem('Plate Type'))
		self.numPoundsPlatesTable.setHorizontalHeaderItem(1,QTableWidgetItem('Number of Plates'))

		# Setting table items
		item = QTableWidgetItem('45lbs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numPoundsPlatesTable.setItem(0,0,item)
		item = QTableWidgetItem('35lbs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numPoundsPlatesTable.setItem(1,0,item)
		item = QTableWidgetItem('25lbs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numPoundsPlatesTable.setItem(2,0,item)
		item = QTableWidgetItem('10lbs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numPoundsPlatesTable.setItem(3,0,item)
		item = QTableWidgetItem('5lbs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numPoundsPlatesTable.setItem(4,0,item)
		item = QTableWidgetItem('2.5lbs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numPoundsPlatesTable.setItem(5,0,item)
		
		# Setting flags for button and text field
		self.calculateButtonPounds.clicked.connect(self.calculateTheWeight)
		self.textFieldPounds.returnPressed.connect(self.calculateTheWeight)
		
		self.tabPounds.setLayout(layout)
		
	def tabKilogramsUI(self):
		# Creating the layout and adding text field, button, and table to it
		layout = QGridLayout()
		layout = QGridLayout()
		layout.addWidget(QLabel('Input the raw weight you want converted'),0,0, Qt.AlignHCenter)
		layout.addWidget(QLabel('minus the bar'),1,0, Qt.AlignHCenter)
		layout.addWidget(self.textFieldKilograms,2,0, Qt.AlignTop)
		layout.addWidget(self.calculateButtonKilograms,3,0, Qt.AlignCenter)
		layout.addWidget(self.numKilogramsPlatesTable,4,0)
		self.numKilogramsPlatesTable.setHorizontalHeaderItem(0,QTableWidgetItem('Plate Type'))
		self.numKilogramsPlatesTable.setHorizontalHeaderItem(1,QTableWidgetItem('Number of Plates'))

		# Setting table items
		item = QTableWidgetItem('20kgs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numKilogramsPlatesTable.setItem(0,0,item)
		item = QTableWidgetItem('15kgs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numKilogramsPlatesTable.setItem(1,0,item)
		item = QTableWidgetItem('10kgs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numKilogramsPlatesTable.setItem(2,0,item)
		item = QTableWidgetItem('5kgs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numKilogramsPlatesTable.setItem(3,0,item)
		item = QTableWidgetItem('2.5kgs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numKilogramsPlatesTable.setItem(4,0,item)
		item = QTableWidgetItem('1.25kgs:')
		item.setTextAlignment(Qt.AlignCenter)
		self.numKilogramsPlatesTable.setItem(5,0,item)
		
		# Setting up flags for the button and text field
		self.calculateButtonKilograms.clicked.connect(self.calculateTheWeightKilograms)
		self.textFieldKilograms.returnPressed.connect(self.calculateTheWeightKilograms)
		
		self.tabKilograms.setLayout(layout)
		
	def calculateTheWeight(self):
		# Getting user input
							 # Have to use try block because a ' '
		try:				 # input throws an error that isn't important
			x = float(self.textFieldPounds.text())
			if int(x) > -1 and float(x)%5 == 0: 
				j = 0
				plates = [' 45', ' 35', ' 25', ' 10', ' 5', ' 2.5']
				# For each plate calculate if you need an even number of them
				for i in range(6):
					while x > -1:
						x = x - float(plates[i])
						j = j+1
					x = x + float(plates[i])
					j = j-1
					if j%2 != 0: # If the plate num is odd you sub 1
						j = j-1
						x = x + float(plates[i])
					# Filling in fields in table
					string = str(j)
					item = QTableWidgetItem(string)
					item.setTextAlignment(Qt.AlignCenter)
					self.numPoundsPlatesTable.setItem(i,1,item)	
					j = 0
		except:
			pass
	def calculateTheWeightKilograms(self):
		# Getting user input
							 # Have to use try block because a ' '
		try:				 # input throws an error that isn't important
			x = float(self.textFieldKilograms.text())
			if int(x) > -1 and float(x)%2.50 == 0: 
				j = 0
				plates = [' 20', ' 15', ' 10', ' 5', ' 2.5', ' 1.25']
				# For each plate calculate if you need an even number of them
				for i in range(6):
					while x > -1:
						x = x - float(plates[i])
						j = j+1
					x = x + float(plates[i])
					j = j-1
					if j%2 != 0: # If the plate num is odd you sub 1
						j = j-1
						x = x + float(plates[i])
					# Filling in fields in table
					string = str(j)
					item = QTableWidgetItem(string)
					item.setTextAlignment(Qt.AlignCenter)
					self.numKilogramsPlatesTable.setItem(i,1,item)	
					j = 0
		except:
			pass
	
if __name__ == '__main__':
	import sys
	import ctypes
	app = QApplication(sys.argv)
	print(QStyleFactory.keys())
	app.setStyle('Fusion')
	# Just allows me to add an image to the program
	myAppID = 'calculator'
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)
	
	weightWindow = WeightCalculator()
	weightWindow.show()
	sys.exit(app.exec_())
