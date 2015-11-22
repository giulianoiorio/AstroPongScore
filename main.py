from __future__ import division
from PyQt4 import QtGui as qt
from PyQt4 import QtCore as qc
import sys
import design
import os
import dialog
import numpy as np

class Dialog(qt.QDialog, dialog.Ui_Dialog):
	def __init__(self,parent=None):
		super(Dialog,self).__init__(parent)
		self.setupUi(self)
	
		
	'''
	def accept(self):
		self.text_home=self.name_home.text()
		self.text_away=self.name_away.text()
	
	def reject(self):
		self.text_home='HOME'
		self.text_home='AWAY'
	'''
		


class ExampleApp(qt.QMainWindow, design.Ui_MainWindow):
	def __init__(self,parent=None):
		super(ExampleApp,self).__init__(parent)
		self.setupUi(self)
		
		#Color ball
		self.palette_ball = qt.QPalette()
		self.palette_noball = qt.QPalette()
		
		brush = qt.QBrush(qt.QColor(252, 0, 13))
		brush.setStyle(qc.Qt.SolidPattern)
		self.palette_ball.setBrush(qt.QPalette.Active, qt.QPalette.WindowText, brush)
		brush = qt.QBrush(qt.QColor(0, 0, 0))
		brush.setStyle(qc.Qt.SolidPattern)
		self.palette_noball.setBrush(qt.QPalette.Active, qt.QPalette.WindowText, brush)
		
		self.counter=0
		self.point_change_ball=1
		self.check_ball=0
		##
		
		self.gol_home.clicked.connect(self.update_home)
		self.gol_away.clicked.connect(self.update_away)
		self.ball_home.clicked.connect(self.start_home)
		self.ball_away.clicked.connect(self.start_away)
		self.zero_home.clicked.connect(self.reset_score_home)
		self.zero_away.clicked.connect(self.reset_score_away)
		self.minus_home.clicked.connect(self.decrease_home)
		self.minus_away.clicked.connect(self.decrease_away)
		self.plus_home.clicked.connect(self.increase_home)
		#self.plus_away.clicked.connect(self.increase_away)
		#self.btnBrowse.clicked.connect(self.browse_folder)
		
		
		
		self.actionReset.triggered.connect(self.reset)
		self.actionExit.triggered.connect(self.exit)

		self.actionNew.triggered.connect(self.new_file)
		
	@qc.pyqtSlot()
	def new_file(self):
		dialog=Dialog(self)
		result=dialog.exec_()

		if result==1:
			self.reset()
			
			if(str(dialog.name_home.text())==''): text_home='HOME'
			else: text_home=dialog.name_home.text() 
			if(str(dialog.name_away.text())==''): text_away='AWAY'
			else: text_away=dialog.name_away.text()

			
			if dialog.b1.isChecked(): self.point_change_ball=1
			elif dialog.b2.isChecked(): self.point_change_ball=2
			elif dialog.b3.isChecked(): self.point_change_ball=3
			elif dialog.b4.isChecked(): self.point_change_ball=4
			elif dialog.b5.isChecked(): self.point_change_ball=5
			
			
			
			if dialog.dialog_position.isChecked(): 
				n= np.random.randint(2) #0 or 1
				if n==0:
					text_home_towrite=text_away
					text_away_towrite=text_home
				else:
					text_home_towrite=text_home
					text_away_towrite=text_away
			else:
					text_home_towrite=text_home
					text_away_towrite=text_away
			
			if dialog.dialog_ball.isChecked():
				n= np.random.randint(2)
				if n==0: self.start_home()
				else: self.start_away()
				
				
		
			
			
			
			
			
		
		self.textEdit.setHtml(design._translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:65pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:65pt;\">%s</span></p></body></html>"%text_home_towrite, None))

		self.textEdit_2.setHtml(design._translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:65pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:65pt;\">%s</span></p></body></html>"%text_away_towrite, None))




	def update_home(self):
		self.counter+=1
		new_value=self.score_home.value()+1
		if new_value>9: self.score_home.setDigitCount(2)
		self.score_home.display(self.score_home.value()+1)
		if self.counter%self.point_change_ball==0: self.change_ball()
		

	def update_away(self):
		self.counter+=1
		new_value=self.score_away.value()+1
		if new_value>9: self.score_away.setDigitCount(2)
		self.score_away.display(self.score_away.value()+1)
		if self.counter%self.point_change_ball==0: self.change_ball()
		
				
	def change_ball(self):
		if self.check_ball==0:
			#home ha la palla
			self.score_home.setPalette(self.palette_ball)
			#away no
			self.score_away.setPalette(self.palette_noball)
			self.check_ball=1
		else:
			#away ha la palla
			self.score_away.setPalette(self.palette_ball)
			#home no
			self.score_home.setPalette(self.palette_noball)
			self.check_ball=0
	
	def start_home(self):
			self.ball_home.setText(design._translate("MainWindow", "FIRST BALL - WIN!!! :)", None))
			self.ball_away.setText(design._translate("MainWindow", "FIRST BALL - LOSE!!! :(", None))
			self.enable_ini(True)
			self.enable_ball(False)
			#home ha la palla
			self.score_home.setPalette(self.palette_ball)
			#away no
			self.score_away.setPalette(self.palette_noball)
			self.check_ball=1
			
	def start_away(self):
			self.ball_home.setText(design._translate("MainWindow", "FIRST BALL - LOSE!!! :(", None))
			self.ball_away.setText(design._translate("MainWindow", "FIRST BALL - WIN!!! :)", None))
			self.enable_ini(True)
			self.enable_ball(False)
			#away ha la palla
			self.score_away.setPalette(self.palette_ball)
			#away no
			self.score_home.setPalette(self.palette_noball)
			self.check_ball=0
			

	def enable_ini(self,choice):
		self.score_home.setEnabled(choice)
		self.score_away.setEnabled(choice)
		self.gol_home.setEnabled(choice)
		self.gol_away.setEnabled(choice)
		self.minus_home.setEnabled(choice)	
		self.minus_away.setEnabled(choice)
		self.plus_home.setEnabled(choice)	
		self.plus_away.setEnabled(choice)		
		self.zero_home.setEnabled(choice)
		self.zero_away.setEnabled(choice)

	def enable_ball(self,choice):
		self.ball_home.setEnabled(choice)
		self.ball_away.setEnabled(choice)
		
	def reset_score_home(self):
		self.score_home.display(0)
	
	def reset_score_away(self):
		self.score_away.display(0)

	def decrease_home(self):
		new_value=self.score_home.value()-1
		if new_value<10: self.score_home.setDigitCount(1)
		if new_value<0: new_value=0
		self.score_home.display(new_value)

	def decrease_away(self):
		new_value=self.score_away.value()-1
		if new_value<0: new_value=0
		if new_value<10: self.score_away.setDigitCount(1)
		self.score_away.display(new_value)
		
	def increase_home(self):
		new_value=self.score_home.value()+1
		if new_value>9: self.score_home.setDigitCount(2)
		self.score_home.display(self.score_home.value()+1)

	def increase_away(self):
		new_value=self.score_away.value()+1
		if new_value>9: self.score_away.setDigitCount(2)
		self.score_away.display(new_value)
		
	def reset(self):
		self.ball_home.setText(design._translate("MainWindow", "FIRST BALL", None))
		self.ball_away.setText(design._translate("MainWindow", "FIRST BALL", None))
		self.score_home.setPalette(self.palette_noball)
		self.score_home.setPalette(self.palette_noball)
		self.reset_score_home()
		self.reset_score_away()
		self.enable_ball(True)
		self.enable_ini(False)
		self.counter=0
		self.check_ball=0
	
	def exit(self):
		self.deleteLater()
		
def main():
	app=qt.QApplication(sys.argv)
	form=ExampleApp()
	form.show()
	app.exec_()
	

if __name__ == '__main__':
	main()