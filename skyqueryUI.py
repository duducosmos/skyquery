# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skyquery.ui'
#
# Created: Wed Jan 30 12:36:19 2013
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
        MainWindow.resize(593, 633)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_4 = QtGui.QFrame(self.frame)
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
        self.groupBox = QtGui.QGroupBox(self.frame_8)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame_9 = QtGui.QFrame(self.groupBox)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton = QtGui.QRadioButton(self.frame_9)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.frame_9)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.verticalLayout_5.addWidget(self.frame_9)
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
        self.frame_6 = QtGui.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame_6)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
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
        self.webView = QtWebKit.QWebView(self.tab_5)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_12.addWidget(self.webView)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SkyQuery", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "User Data Base:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "SQLite", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "DB Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>The Name of Data Base where the data will be saved</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Data Base:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>The Data Base Name used: </p><p align=\"center\">MySQL : mysql</p><p align=\"center\">PostgresSQL: postgres</p><p align=\"center\">MSSQL: mssql</p><p align=\"center\">FireBird: firebird</p><p align=\"center\">Oracle: oracle</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setText(QtGui.QApplication.translate("MainWindow", "postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "User : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Password : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Host : ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setText(QtGui.QApplication.translate("MainWindow", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Table Name : ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("MainWindow", "SELECT  TOP 5 t.SpecObjID, t.ra, t.dec, mjd,plate,\n"
"fiberID,z,zErr,zConf,specClass\n"
"FROM Target as t\n"
"--Match to the tables with geometry and version information\n"
"inner JOIN Region as r on t.regionid = r.regionid\n"
"inner JOIN TargetInfo as ti on t.targetId = ti.targetid\n"
"-- Extract the TARGET photometry\n"
"inner JOIN TARGDR7..PhotoTag as p on ti.targetObjId = p.objID\n"
"-- Match to objetcs with spectroscopy\n"
"LEFT OUTER JOIN specObj as s on s.targetid = t.targetId\n"
"WHERE(\n"
"-- Restrict sample to target selection version v3_1_0\n"
"     r.regionid in (\n"
"         SELECT b.boxid FROM region2box as b, tilinggeometry as g\n"
"         WHERE b.boxtype = \'SECTOR\'\n"
"         AND b.regiontype = \'TIPRIMARY\' \n"
"         AND b.id = g.tilinggeometryid \n"
"         GROUP BY b.boxid\n"
"         HAVING MIN(g.targetversion) >= \'v3_1_0\'\n"
"     )\n"
"     AND\n"
"     -- Include only primary objects\n"
"         ((p.mode =1) AND (p.status & 0x10) > 0) AND ((p.status & 0x2000) > 0) \n"
"     AND\n"
"     -- Include only explicit quasar targets\n"
"         ((p.primTarget & 0x0000001f) >0)\n"
"     AND \n"
"     -- Include only quasar confirmed by spectral analisys\n"
"         (s.SpecClass > 2)\n"
"    AND\n"
"         (s.SpecClass < 5)\n"
"     AND\n"
"         (s.zConf > 0.3)\n"
"    AND\n"
"        (s.z > 0.0)\n"
")\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Save Query", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Save Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Data Recived", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "My Queries", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
