# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skyquery.ui'
#
# Created: Fri Feb  1 10:09:35 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(728, 627)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("SkyQuery.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.frame_4 = QtGui.QFrame(self.tab)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame_8 = QtGui.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_5 = QtGui.QGroupBox(self.frame_8)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_9 = QtGui.QFrame(self.groupBox_5)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.frame_9)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.horizontalLayout_4.addWidget(self.groupBox_6)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox = QtGui.QGroupBox(self.frame_8)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame_10 = QtGui.QFrame(self.groupBox)
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.frame_10)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label_6 = QtGui.QLabel(self.frame_10)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_10)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_11 = QtGui.QFrame(self.groupBox)
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.frame_11)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_11)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.label_4 = QtGui.QLabel(self.frame_11)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_11)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_4.setInputMask(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.label_5 = QtGui.QLabel(self.frame_11)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_11)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.verticalLayout_15.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.frame_5 = QtGui.QFrame(self.tab_3)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame_5)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout_6.addWidget(self.plainTextEdit)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.frame_3 = QtGui.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.frame_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.frame_7 = QtGui.QFrame(self.tab_4)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.frame_12 = QtGui.QFrame(self.frame_7)
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.textEdit = QtGui.QTextEdit(self.frame_12)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_10.addWidget(self.textEdit)
        self.verticalLayout_9.addWidget(self.frame_12)
        self.frame_13 = QtGui.QFrame(self.frame_7)
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName(_fromUtf8("frame_13"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_11.addWidget(self.pushButton_3)
        self.verticalLayout_9.addWidget(self.frame_13)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.scrollArea = QtGui.QScrollArea(self.tab_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 686, 534))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.listWidget = QtGui.QListWidget(self.groupBox_4)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_14.addWidget(self.listWidget)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_14.addWidget(self.pushButton_5)
        self.horizontalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_13.addWidget(self.textEdit_2)
        self.frame_14 = QtGui.QFrame(self.groupBox_3)
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName(_fromUtf8("frame_14"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_14)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        self.pushButton_6 = QtGui.QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.verticalLayout_13.addWidget(self.frame_14)
        self.horizontalLayout_7.addWidget(self.groupBox_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_12.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SkyQuery", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Data Base", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "SQLite", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Another type of Data Base like mysql</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Save data in a csv file</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "csv", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "User Data Base:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "DB Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>The Name of Data Base where the data will be saved</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Data Base:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>The Data Base Name used: </p><p align=\"center\">MySQL : mysql</p><p align=\"center\">PostgresSQL: postgres</p><p align=\"center\">MSSQL: mssql</p><p align=\"center\">FireBird: firebird</p><p align=\"center\">Oracle: oracle</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setText(QtGui.QApplication.translate("MainWindow", "postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Table Name : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "User : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Password : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Host : ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setText(QtGui.QApplication.translate("MainWindow", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Local DataBase", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("MainWindow","", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Save Query", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Save Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Data Recived", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Queries", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Selected Query", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Submit Query", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Delete Query From DB", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "My Queries", None, QtGui.QApplication.UnicodeUTF8))

