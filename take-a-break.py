#!/usr/bin/python
# -*- coding: utf-8 -*-

#take-a-break.py

import sys, subprocess
from PyQt4 import QtGui, QtCore

class AboutDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		super(AboutDialog, self).__init__(parent)

		QtGui.QWidget.__init__(self, parent)
		self.setGeometry(10, 10, 340, 120) #starts at point (10,10) with width 340 px and height 120 px
		self.setWindowTitle('Take a Break')

		grid = QtGui.QGridLayout()
		
		self.textfield = QtGui.QTextEdit(self)
		self.textfield.setText("Begin 25 min session?")
		self.textfield.setStyleSheet("background-color:transparent;border:none;")
		self.textfield.setReadOnly(True)

		self.goButton = QtGui.QPushButton("Go")
		self.goButton.clicked.connect(self.goSession)
		self.cancelButton = QtGui.QPushButton("Exit")
		self.cancelButton.clicked.connect(self.abortSession)

		grid.addWidget(self.textfield, 0, 0, -1, -1, QtCore.Qt.AlignCenter)
		grid.addWidget(self.goButton, 1, 0)
		grid.addWidget(self.cancelButton, 1, 1)
		self.setLayout(grid)

		self.countingNow = False
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.tick)
		
	def goSession(self):
		# pass
		# add opening only once!!!
		if not self.countingNow:
			self.timer.start(1500000) # in ms 25 min -> 1500000
			self.textfield.setText("Session started ...")
			self.goButton.setText("On")
			self.cancelButton.setText("Abort")
			self.countingNow = True
		else:
			# do nothing if already counting
			pass

	def abortSession(self):
		if not self.countingNow:
			# quit program
			self.close()
		else:
			# cancel timer and print message
			self.timer.stop()
			self.textfield.setText("Mission abort. Start Again?")
			self.goButton.setText("Go")
			self.cancelButton.setText("Exit")
			self.countingNow = False

	def tick(self):
		self.textfield.setText("Done! Another one?")
		self.timer.stop() # to make sure it doesn't continue counting
		self.goButton.setText("Go")
		self.cancelButton.setText("Exit")
		self.countingNow = False
		# lock the screen
		subprocess.call('mate-screensaver-command -l')
		# other variations
		# subprocess.call('gnome-screensaver-command -l')
		# subprocess.call('xscreensaver-command -lock'.split())
		# subprocess.call('cinnamon-screensaver-command -l')

def main():   
    app = QtGui.QApplication(sys.argv)
    ad = AboutDialog()
    ad.show()
    sys.exit(app.exec_())

if __name__ == '__main__':	
	main()
	

