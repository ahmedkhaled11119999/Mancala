# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstUI_Attempt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#! Command to Convert UI file -> Python :  pyuic5 -x FirstUI_Attempt.ui -o UIoutput.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import * 
import sys

from Board.Board import Board


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #! 
        self.BoardObj = Board()
        
        MainWindow.resize(1251, 797)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1251, 871))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.BT4 = QtWidgets.QPushButton(self.page)
        self.BT4.setEnabled(True)
        self.BT4.setGeometry(QtCore.QRect(800, 480, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT4.setFont(font)
        self.BT4.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT4.setObjectName("BT4")
        self.BT6 = QtWidgets.QPushButton(self.page)
        self.BT6.setEnabled(True)
        self.BT6.setGeometry(QtCore.QRect(1060, 400, 71, 121))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(35)
        self.BT6.setFont(font)
        self.BT6.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent;")
        self.BT6.setObjectName("BT6")
        self.Player2Turn_2 = QtWidgets.QLabel(self.page)
        self.Player2Turn_2.setGeometry(QtCore.QRect(500, 170, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Player2Turn_2.setFont(font)
        self.Player2Turn_2.setStyleSheet("color :  rgb(255, 252, 168);")
        self.Player2Turn_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Player2Turn_2.setObjectName("Player2Turn_2")
        self.BT11 = QtWidgets.QPushButton(self.page)
        self.BT11.setEnabled(True)
        self.BT11.setGeometry(QtCore.QRect(410, 260, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT11.setFont(font)
        self.BT11.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT11.setObjectName("BT11")
        self.SecCounterLabel = QtWidgets.QLabel(self.page)
        self.SecCounterLabel.setGeometry(QtCore.QRect(970, 140, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SecCounterLabel.setFont(font)
        self.SecCounterLabel.setStyleSheet("color :  rgb(255, 252, 168);")
        self.SecCounterLabel.setObjectName("SecCounterLabel")
        self.BT9 = QtWidgets.QPushButton(self.page)
        self.BT9.setEnabled(True)
        self.BT9.setGeometry(QtCore.QRect(670, 260, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT9.setFont(font)
        self.BT9.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT9.setObjectName("BT9")
        self.BT12 = QtWidgets.QPushButton(self.page)
        self.BT12.setEnabled(True)
        self.BT12.setGeometry(QtCore.QRect(280, 260, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT12.setFont(font)
        self.BT12.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT12.setObjectName("BT12")
        self.BT10 = QtWidgets.QPushButton(self.page)
        self.BT10.setEnabled(True)
        self.BT10.setGeometry(QtCore.QRect(540, 260, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT10.setFont(font)
        self.BT10.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT10.setObjectName("BT10")
        self.BT2 = QtWidgets.QPushButton(self.page)
        self.BT2.setEnabled(True)
        self.BT2.setGeometry(QtCore.QRect(540, 480, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT2.setFont(font)
        self.BT2.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT2.setObjectName("BT2")
        self.BT8 = QtWidgets.QPushButton(self.page)
        self.BT8.setEnabled(True)
        self.BT8.setGeometry(QtCore.QRect(800, 260, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT8.setFont(font)
        self.BT8.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT8.setObjectName("BT8")
        self.BT13 = QtWidgets.QPushButton(self.page)
        self.BT13.setEnabled(True)
        self.BT13.setGeometry(QtCore.QRect(140, 280, 71, 121))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(35)
        self.BT13.setFont(font)
        self.BT13.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent;")
        self.BT13.setObjectName("BT13")
        self.BT1 = QtWidgets.QPushButton(self.page)
        self.BT1.setEnabled(True)
        self.BT1.setGeometry(QtCore.QRect(410, 480, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT1.setFont(font)
        self.BT1.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT1.setObjectName("BT1")
        self.BackgroundImg = QtWidgets.QLabel(self.page)
        self.BackgroundImg.setGeometry(QtCore.QRect(0, 0, 1251, 801))
        self.BackgroundImg.setText("")
        self.BackgroundImg.setPixmap(QtGui.QPixmap("back.PNG"))
        self.BackgroundImg.setScaledContents(True)
        self.BackgroundImg.setWordWrap(False)
        self.BackgroundImg.setObjectName("BackgroundImg")
        self.BoardImgLabel = QtWidgets.QLabel(self.page)
        self.BoardImgLabel.setGeometry(QtCore.QRect(70, 110, 1131, 591))
        self.BoardImgLabel.setText("")
        self.BoardImgLabel.setPixmap(QtGui.QPixmap("Board.PNG"))
        self.BoardImgLabel.setScaledContents(True)
        self.BoardImgLabel.setObjectName("BoardImgLabel")
        self.BT0 = QtWidgets.QPushButton(self.page)
        self.BT0.setEnabled(True)
        self.BT0.setGeometry(QtCore.QRect(280, 480, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT0.setFont(font)
        self.BT0.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT0.setObjectName("BT0")
        self.BT5 = QtWidgets.QPushButton(self.page)
        self.BT5.setEnabled(True)
        self.BT5.setGeometry(QtCore.QRect(930, 480, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT5.setFont(font)
        self.BT5.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT5.setObjectName("BT5")
        self.MancalaLabel = QtWidgets.QLabel(self.page)
        self.MancalaLabel.setGeometry(QtCore.QRect(490, 20, 273, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.MancalaLabel.setFont(font)
        self.MancalaLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MancalaLabel.setStyleSheet("color: rgb(255, 252, 168);")
        self.MancalaLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MancalaLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MancalaLabel.setScaledContents(False)
        self.MancalaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MancalaLabel.setWordWrap(False)
        self.MancalaLabel.setObjectName("MancalaLabel")
        self.BT7 = QtWidgets.QPushButton(self.page)
        self.BT7.setEnabled(True)
        self.BT7.setGeometry(QtCore.QRect(930, 260, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT7.setFont(font)
        self.BT7.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT7.setObjectName("BT7")
        self.BT3 = QtWidgets.QPushButton(self.page)
        self.BT3.setEnabled(True)
        self.BT3.setGeometry(QtCore.QRect(670, 480, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.BT3.setFont(font)
        self.BT3.setStyleSheet("color: rgb(255, 252, 168);background-color: transparent")
        self.BT3.setObjectName("BT3")
        self.Player1Turn = QtWidgets.QLabel(self.page)
        self.Player1Turn.setGeometry(QtCore.QRect(500, 610, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Player1Turn.setFont(font)
        self.Player1Turn.setStyleSheet("color :  rgb(255, 252, 168);")
        self.Player1Turn.setAlignment(QtCore.Qt.AlignCenter)
        self.Player1Turn.setObjectName("Player1Turn")
        self.Plus1_P2Label = QtWidgets.QLabel(self.page)
        self.Plus1_P2Label.setGeometry(QtCore.QRect(590, 220, 81, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.Plus1_P2Label.setFont(font)
        self.Plus1_P2Label.setStyleSheet("color :  rgb(255, 252, 168);")
        self.Plus1_P2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Plus1_P2Label.setObjectName("Plus1_P2Label")
        self.Plus1_P1Label = QtWidgets.QLabel(self.page)
        self.Plus1_P1Label.setGeometry(QtCore.QRect(590, 540, 81, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.Plus1_P1Label.setFont(font)
        self.Plus1_P1Label.setStyleSheet("color :  rgb(255, 252, 168);")
        self.Plus1_P1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Plus1_P1Label.setObjectName("Plus1_P1Label")
        self.SaveBtn = QtWidgets.QPushButton(self.page)
        self.SaveBtn.setGeometry(QtCore.QRect(960, 650, 191, 55))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveBtn.sizePolicy().hasHeightForWidth())
        self.SaveBtn.setSizePolicy(sizePolicy)
        self.SaveBtn.setMaximumSize(QtCore.QSize(446, 16777215))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setItalic(False)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SaveBtn.setStyleSheet("border-radius: 25px;background-color: rgb(255, 252, 168);")
        self.SaveBtn.setObjectName("SaveBtn")
        self.BackgroundImg.raise_()
        self.BoardImgLabel.raise_()
        self.BT0.raise_()
        self.BT5.raise_()
        self.MancalaLabel.raise_()
        self.BT7.raise_()
        self.BT3.raise_()
        self.Player1Turn.raise_()
        self.BT1.raise_()
        self.BT10.raise_()
        self.BT11.raise_()
        self.BT12.raise_()
        self.BT13.raise_()
        self.BT2.raise_()
        self.BT4.raise_()
        self.BT6.raise_()
        self.BT9.raise_()
        self.BT8.raise_()
        self.Player2Turn_2.raise_()
        self.SecCounterLabel.raise_()
        self.Plus1_P2Label.raise_()
        self.Plus1_P1Label.raise_()
        self.SaveBtn.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 1251, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("back.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.page_2)
        self.splitter.setGeometry(QtCore.QRect(400, 100, 501, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.splitter.setStyleSheet("")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.MancalaLabel_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.MancalaLabel_2.setFont(font)
        self.MancalaLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MancalaLabel_2.setStyleSheet("color: rgb(255, 252, 168);")
        self.MancalaLabel_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MancalaLabel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MancalaLabel_2.setScaledContents(False)
        self.MancalaLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.MancalaLabel_2.setWordWrap(False)
        self.MancalaLabel_2.setObjectName("MancalaLabel_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SinglePlayerBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SinglePlayerBtn.sizePolicy().hasHeightForWidth())
        self.SinglePlayerBtn.setSizePolicy(sizePolicy)
        self.SinglePlayerBtn.setMaximumSize(QtCore.QSize(446, 16777215))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setItalic(False)
        self.SinglePlayerBtn.setFont(font)
        self.SinglePlayerBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SinglePlayerBtn.setStyleSheet("border-radius: 25px;background-color: rgb(255, 252, 168);margin-left : 50px;")
        self.SinglePlayerBtn.setObjectName("SinglePlayerBtn")
        self.verticalLayout.addWidget(self.SinglePlayerBtn)
        self.MultiPlayerBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MultiPlayerBtn.sizePolicy().hasHeightForWidth())
        self.MultiPlayerBtn.setSizePolicy(sizePolicy)
        self.MultiPlayerBtn.setMaximumSize(QtCore.QSize(446, 16777215))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setItalic(False)
        self.MultiPlayerBtn.setFont(font)
        self.MultiPlayerBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MultiPlayerBtn.setStyleSheet("border-radius: 25px;background-color: rgb(255, 252, 168);margin-left : 50px;")
        self.MultiPlayerBtn.setObjectName("MultiPlayerBtn")
        self.verticalLayout.addWidget(self.MultiPlayerBtn)
        self.widget = QtWidgets.QWidget(self.layoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 39))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(110, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RadioStealing = QtWidgets.QRadioButton(self.widget)
        self.RadioStealing.setStyleSheet("color: rgb(255, 252, 168);")
        self.RadioStealing.setObjectName("RadioStealing")
        self.horizontalLayout.addWidget(self.RadioStealing)
        self.RadioNoSteal = QtWidgets.QRadioButton(self.widget)
        self.RadioNoSteal.setStyleSheet("color: rgb(255, 252, 168);")
        self.RadioNoSteal.setObjectName("RadioNoSteal")
        self.horizontalLayout.addWidget(self.RadioNoSteal)
        self.verticalLayout.addWidget(self.widget)
        self.LoadBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadBtn.sizePolicy().hasHeightForWidth())
        self.LoadBtn.setSizePolicy(sizePolicy)
        self.LoadBtn.setMaximumSize(QtCore.QSize(446, 16777215))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setItalic(False)
        self.LoadBtn.setFont(font)
        self.LoadBtn.setStyleSheet("border-radius: 25px;background-color: rgb(255, 252, 168);margin-left : 50px;")
        self.LoadBtn.setObjectName("LoadBtn")
        self.verticalLayout.addWidget(self.LoadBtn)
        self.ExitGameBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitGameBtn.sizePolicy().hasHeightForWidth())
        self.ExitGameBtn.setSizePolicy(sizePolicy)
        self.ExitGameBtn.setMaximumSize(QtCore.QSize(446, 16777215))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(20)
        font.setItalic(False)
        self.ExitGameBtn.setFont(font)
        self.ExitGameBtn.setStyleSheet("border-radius: 25px;background-color: rgb(255, 252, 168);margin-left : 50px;")
        self.ExitGameBtn.setObjectName("ExitGameBtn")
        self.verticalLayout.addWidget(self.ExitGameBtn)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #! ------------- Add Here -------------
        self.stackedWidget.setCurrentIndex(1)
        self.MainWindow = MainWindow
        
        
        
        #! Make list of Buttons
        self.Btn_List = []
        self.Btn_List.append(self.BT0)
        self.Btn_List.append(self.BT1)
        self.Btn_List.append(self.BT2)
        self.Btn_List.append(self.BT3)
        self.Btn_List.append(self.BT4)
        self.Btn_List.append(self.BT5)
        self.Btn_List.append(self.BT6)
        self.Btn_List.append(self.BT7)
        self.Btn_List.append(self.BT8)
        self.Btn_List.append(self.BT9)
        self.Btn_List.append(self.BT10)
        self.Btn_List.append(self.BT11)
        self.Btn_List.append(self.BT12)
        self.Btn_List.append(self.BT13)

        #! Player 1 Starts
        
        self.LastPlayer = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BT4.setText(_translate("MainWindow", "4"))
        self.BT6.setText(_translate("MainWindow", "6"))
        self.Player2Turn_2.setText(_translate("MainWindow", "Player 2 Turn"))
        self.BT11.setText(_translate("MainWindow", "11"))
        self.SecCounterLabel.setText(_translate("MainWindow", "1 Seconds Left !! "))
        self.BT9.setText(_translate("MainWindow", "9"))
        self.BT12.setText(_translate("MainWindow", "12"))
        self.BT10.setText(_translate("MainWindow", "10"))
        self.BT2.setText(_translate("MainWindow", "2"))
        self.BT8.setText(_translate("MainWindow", "8"))
        self.BT13.setText(_translate("MainWindow", "13"))
        self.BT1.setText(_translate("MainWindow", "1"))
        self.BT0.setText(_translate("MainWindow", "0"))
        self.BT5.setText(_translate("MainWindow", "5"))
        self.MancalaLabel.setText(_translate("MainWindow", "Mancala Game "))
        self.BT7.setText(_translate("MainWindow", "7"))
        self.BT3.setText(_translate("MainWindow", "3"))
        self.Player1Turn.setText(_translate("MainWindow", "Player 1 Turn"))
        self.Plus1_P2Label.setText(_translate("MainWindow", "+1"))
        self.Plus1_P1Label.setText(_translate("MainWindow", "+1"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
        self.MancalaLabel_2.setText(_translate("MainWindow", "Mancala Game "))
        self.SinglePlayerBtn.setText(_translate("MainWindow", "Single Player"))
        self.MultiPlayerBtn.setText(_translate("MainWindow", "Multi-Player"))
        self.RadioStealing.setText(_translate("MainWindow", "Stealing"))
        self.RadioNoSteal.setText(_translate("MainWindow", "No Stealing"))
        self.LoadBtn.setText(_translate("MainWindow", "Load Game"))
        self.ExitGameBtn.setText(_translate("MainWindow", "Exit"))
        
        #! 
        self.Plus1_P2Label.setVisible(False)
        self.Plus1_P1Label.setVisible(False)
        #!
        self.BT0.clicked.connect(self.Pile_Pressed)
        self.BT1.clicked.connect(self.Pile_Pressed)
        self.BT2.clicked.connect(self.Pile_Pressed)
        self.BT3.clicked.connect(self.Pile_Pressed)
        self.BT4.clicked.connect(self.Pile_Pressed)
        self.BT5.clicked.connect(self.Pile_Pressed)
        self.BT6.clicked.connect(self.Pile_Pressed)
        self.BT7.clicked.connect(self.Pile_Pressed)
        self.BT8.clicked.connect(self.Pile_Pressed)
        self.BT9.clicked.connect(self.Pile_Pressed)
        self.BT10.clicked.connect(self.Pile_Pressed)
        self.BT11.clicked.connect(self.Pile_Pressed)
        self.BT12.clicked.connect(self.Pile_Pressed)
        self.BT13.clicked.connect(self.Pile_Pressed)
        
        #! 
        
        self.MultiPlayerBtn.clicked.connect(self.StartGame)
        
        #! Save and Load Btns
        self.SaveBtn.clicked.connect(self.saveGame)
        self.LoadBtn.clicked.connect(self.loadGame)
        self.ExitGameBtn.clicked.connect(self.exitGame)
        #! Disable
        self.BT6.setEnabled(False)
        self.BT13.setEnabled(False)
        
        #! creating a timer object
        timer = QTimer(MainWindow)
        self.start = False
        #! 20 Second For time out 
        self.count = 0
        # adding action to timer
        timer.timeout.connect(self.showTime)
        # update the timer every second
        timer.start(100)
    
    def saveGame(self):  
        QSound.play("Click.wav")
        self.BoardObj.saveGame()
    def exitGame(self):  
        sys.exit(app.exec_())
    def loadGame(self):
        self.BoardObj.loadGame()
        self.StartGame()
        
    def StartGame(self):
        if self.RadioStealing.isChecked():
                self.BoardObj.stealing = True
                print("Stealing Activated")
        else : 
                self.BoardObj.stealing = False
                print("No Stealing Activated")
        self.BoardObj.toggleGameStatus(1)
        self.stackedWidget.setCurrentIndex(0) 
        self.Toggle_Btns()   
        self.LastPlayer =1
        self.Update_Board()
        QSound.play("Thba7.wav")
    def showTime(self):
        # checking if flag is true
        if self.start:
                # incrementing the counter
                self.count -= 1

        # timer is completed
        if self.count == 0:
                # making flag false
                self.start = False
                # setting text to the label
                self.SecCounterLabel.setText("Time Outtt!!!")

        if self.start:
                # getting text from count
                text = "Time Remaining:"+str(int(self.count/10 )) + " s"
                # showing text
                self.SecCounterLabel.setText(text)
    #! Function Called when a pile is clicked              
    def Pile_Pressed(self):
        QSound.play("Click.wav")
        sending_button = self.MainWindow.sender()
        if sending_button.text() == '0':
                print("Can't Play 0")
                return 
        
        self.BoardObj.clicked_index = int(sending_button.objectName()[2:])
        self.BoardObj.prepMove()
        if self.BoardObj.wrong_turn == 1 or self.BoardObj.wrong_turn == 2:
                return
        #self.Player2Turn_2.setText('%s Clicked!' % str(sending_button.objectName()))
        #! Add your Function Board Function
        self.Update_Board()
        # Update Board with new Values
        
        self.Reset_Timer()
        self.Toggle_Btns()
        self.LastPlayer = self.BoardObj.player
        if self.BoardObj.winning_player == 1:
                print("Player 1 Win")
        elif self.BoardObj.winning_player == 2:
                print("Player 2 Win")
        elif self.BoardObj.winning_player == 3:
                print("Draw")
                
#! 
    def Update_Board(self):
        count = 0
        for newValue,btn in zip(self.BoardObj.piles, self.Btn_List):
                if newValue == 0:
                        btn.setEnabled(False)
                else:
                        btn.setEnabled(True)
                btn.setText(str(newValue))
        
        self.CheckWinner()
        self.BT6.setEnabled(False)
        self.BT13.setEnabled(False)
   
    def CheckWinner(self):
            if self.BoardObj.winning_player != 0:
                   msg = QtWidgets.QMessageBox()
                   msg.setWindowTitle("We Have a Winner!!")
                   msg.setText("Congrats Player"+str(self.BoardObj.winning_player)+" You are the Winner!!")  
                   msg.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Cancel)
                   msg.clickedButton.connect()
                   x = msg.exec_() 
    #! Function Called when the winner choose retry or cancle            
    def MsgButton(self,i):
            if i.text == "Retry":
                self.BoardObj = Board()
                self.StartGame()
            else : 
                self.exitGame()
            
                    
    def Reset_Timer(self):
        self.count = 20 * 10
        self.start = True

    def Toggle_Btns(self):
                
        if self.BoardObj.player == 1:
                
                self.Plus1_P2Label.setVisible(False)
                if self.LastPlayer == 1:
                        self.Plus1_P1Label.setVisible(True)
                        QSound.play("3ed.wav")
                else: 
                        self.Plus1_P1Label.setVisible(False)
                                
                self.Player2Turn_2.setStyleSheet("background-color: transparent;")
                self.Player1Turn.setStyleSheet("color :  rgb(255, 252, 168);")
                for i in range(7):
                        self.Btn_List[i].setEnabled(True)
                        self.Btn_List[i].setStyleSheet("color :  rgb(255, 252, 168);background-color: transparent; ")
                #! His Turn
                for i in range(7,14):
                        self.Btn_List[i].setEnabled(False)
                        self.Btn_List[i].setStyleSheet("color :  rgb(219, 164, 13);background-color: transparent; ")
        # Player 2 Turn
        else: 
                self.Plus1_P1Label.setVisible(False)
                if self.LastPlayer == 2:
                        self.Plus1_P2Label.setVisible(True)
                        QSound.play("3ed.wav")
                else :
                        self.Plus1_P2Label.setVisible(False)
                self.Player2Turn_2.setStyleSheet(" color :  rgb(255, 252, 168)")
                self.Player1Turn.setStyleSheet("background-color: transparent;")
                for i in range(7):
                        self.Btn_List[i].setEnabled(False)
                        self.Btn_List[i].setStyleSheet("color :  rgb(219, 164, 13);background-color: transparent; ")
                #! His Turn
                for i in range(7,14):
                        self.Btn_List[i].setEnabled(True)
                        self.Btn_List[i].setStyleSheet("color :  rgb(255, 252, 168);background-color: transparent; ")
        
        self.BT6.setEnabled(False)
        self.BT13.setEnabled(False)
                        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
