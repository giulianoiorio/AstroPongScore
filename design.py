# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1227, 724)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ball_away = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ball_away.setFont(font)
        self.ball_away.setObjectName(_fromUtf8("ball_away"))
        self.gridLayout.addWidget(self.ball_away, 3, 1, 1, 1)
        self.score_away = QtGui.QLCDNumber(self.centralwidget)
        self.score_away.setEnabled(False)
        self.score_away.setMinimumSize(QtCore.QSize(545, 429))
        self.score_away.setSmallDecimalPoint(False)
        self.score_away.setNumDigits(1)
        self.score_away.setProperty("intValue", 0)
        self.score_away.setObjectName(_fromUtf8("score_away"))
        self.gridLayout.addWidget(self.score_away, 1, 1, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 78))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gol_away = QtGui.QPushButton(self.centralwidget)
        self.gol_away.setEnabled(False)
        self.gol_away.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gol_away.setFont(font)
        self.gol_away.setObjectName(_fromUtf8("gol_away"))
        self.gridLayout.addWidget(self.gol_away, 2, 1, 1, 1)
        self.gol_home = QtGui.QPushButton(self.centralwidget)
        self.gol_home.setEnabled(False)
        self.gol_home.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gol_home.setFont(font)
        self.gol_home.setObjectName(_fromUtf8("gol_home"))
        self.gridLayout.addWidget(self.gol_home, 2, 0, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 78))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 0, 1, 1, 1)
        self.ball_home = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ball_home.setFont(font)
        self.ball_home.setObjectName(_fromUtf8("ball_home"))
        self.gridLayout.addWidget(self.ball_home, 3, 0, 1, 1)
        self.score_home = QtGui.QLCDNumber(self.centralwidget)
        self.score_home.setEnabled(False)
        self.score_home.setMinimumSize(QtCore.QSize(546, 429))
        self.score_home.setNumDigits(1)
        self.score_home.setObjectName(_fromUtf8("score_home"))
        self.gridLayout.addWidget(self.score_home, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.minus_home = QtGui.QPushButton(self.centralwidget)
        self.minus_home.setEnabled(False)
        self.minus_home.setObjectName(_fromUtf8("minus_home"))
        self.horizontalLayout.addWidget(self.minus_home)
        self.plus_home = QtGui.QPushButton(self.centralwidget)
        self.plus_home.setEnabled(False)
        self.plus_home.setObjectName(_fromUtf8("plus_home"))
        self.horizontalLayout.addWidget(self.plus_home)
        self.zero_home = QtGui.QPushButton(self.centralwidget)
        self.zero_home.setEnabled(False)
        self.zero_home.setObjectName(_fromUtf8("zero_home"))
        self.horizontalLayout.addWidget(self.zero_home)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.minus_away = QtGui.QPushButton(self.centralwidget)
        self.minus_away.setEnabled(False)
        self.minus_away.setObjectName(_fromUtf8("minus_away"))
        self.horizontalLayout_2.addWidget(self.minus_away)
        self.plus_away = QtGui.QPushButton(self.centralwidget)
        self.plus_away.setEnabled(False)
        self.plus_away.setObjectName(_fromUtf8("plus_away"))
        self.horizontalLayout_2.addWidget(self.plus_away)
        self.zero_away = QtGui.QPushButton(self.centralwidget)
        self.zero_away.setEnabled(False)
        self.zero_away.setObjectName(_fromUtf8("zero_away"))
        self.horizontalLayout_2.addWidget(self.zero_away)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1227, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setCheckable(True)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionReset)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AstroPong", None))
        self.ball_away.setText(_translate("MainWindow", "FIRST BALL", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:65pt;\">HOME</span></p></body></html>", None))
        self.gol_away.setText(_translate("MainWindow", "SCORE!!!", None))
        self.gol_home.setText(_translate("MainWindow", "SCORE!!!", None))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:65pt;\">AWAY</span></p></body></html>", None))
        self.ball_home.setText(_translate("MainWindow", "FIRST BALL", None))
        self.minus_home.setText(_translate("MainWindow", "-1", None))
        self.plus_home.setText(_translate("MainWindow", "+1", None))
        self.zero_home.setText(_translate("MainWindow", "0", None))
        self.minus_away.setText(_translate("MainWindow", "-1", None))
        self.plus_away.setText(_translate("MainWindow", "+1", None))
        self.zero_away.setText(_translate("MainWindow", "0", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

