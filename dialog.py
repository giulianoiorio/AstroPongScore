# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.dialog_ok = QtGui.QDialogButtonBox(Dialog)
        self.dialog_ok.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.dialog_ok.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_ok.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dialog_ok.setObjectName(_fromUtf8("dialog_ok"))
        self.b1 = QtGui.QRadioButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(20, 170, 31, 18))
        self.b1.setChecked(True)
        self.b1.setObjectName(_fromUtf8("b1"))
        self.b2 = QtGui.QRadioButton(Dialog)
        self.b2.setGeometry(QtCore.QRect(70, 170, 31, 18))
        self.b2.setObjectName(_fromUtf8("b2"))
        self.b3 = QtGui.QRadioButton(Dialog)
        self.b3.setGeometry(QtCore.QRect(120, 170, 41, 18))
        self.b3.setObjectName(_fromUtf8("b3"))
        self.dialog_position = QtGui.QCheckBox(Dialog)
        self.dialog_position.setGeometry(QtCore.QRect(20, 200, 131, 18))
        self.dialog_position.setObjectName(_fromUtf8("dialog_position"))
        self.dialog_ball = QtGui.QCheckBox(Dialog)
        self.dialog_ball.setGeometry(QtCore.QRect(20, 230, 131, 18))
        self.dialog_ball.setObjectName(_fromUtf8("dialog_ball"))
        self.b4 = QtGui.QRadioButton(Dialog)
        self.b4.setGeometry(QtCore.QRect(160, 170, 41, 18))
        self.b4.setObjectName(_fromUtf8("b4"))
        self.b5 = QtGui.QRadioButton(Dialog)
        self.b5.setGeometry(QtCore.QRect(210, 170, 41, 18))
        self.b5.setObjectName(_fromUtf8("b5"))
        self.name_home = QtGui.QLineEdit(Dialog)
        self.name_home.setGeometry(QtCore.QRect(20, 50, 231, 21))
        self.name_home.setObjectName(_fromUtf8("name_home"))
        self.name_away = QtGui.QLineEdit(Dialog)
        self.name_away.setGeometry(QtCore.QRect(20, 100, 231, 21))
        self.name_away.setObjectName(_fromUtf8("name_away"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.dialog_ok, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.dialog_ok, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.b1.setText(_translate("Dialog", "1", None))
        self.b2.setText(_translate("Dialog", "2", None))
        self.b3.setText(_translate("Dialog", "3", None))
        self.dialog_position.setText(_translate("Dialog", "Random Position", None))
        self.dialog_ball.setText(_translate("Dialog", "Random first ball", None))
        self.b4.setText(_translate("Dialog", "4", None))
        self.b5.setText(_translate("Dialog", "5", None))

