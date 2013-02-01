#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from __future__ import with_statement

import sys, os
from PyQt4 import QtCore
from PyQt4 import QtGui

from skyqueryUI import Ui_MainWindow

from skyQuery import *
from gluon import *
from string import replace
import datetime

class DesignerMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(DesignerMainWindow,self).__init__(parent)
        self.setupUi(self)
        

        QtCore.QObject.connect(self.listWidget,\
                                                QtCore.SIGNAL("clicked(QModelIndex)"), \
                                                self.listQueryClicked)

        QtCore.QObject.connect(self.pushButton,\
                               QtCore.SIGNAL("clicked()"),\
                               self.querySDSS)                               
        QtCore.QObject.connect(self.pushButton_2, \
                               QtCore.SIGNAL("clicked()"), \
                               self.saveQuery)
        QtCore.QObject.connect(self.pushButton_3, 
                               QtCore.SIGNAL("clicked()"), \
                               self.saveData)
        QtCore.QObject.connect(self.pushButton_4, \
                               QtCore.SIGNAL("clicked()"), \
                               self.queryfromExistentQuery)
        QtCore.QObject.connect(self.pushButton_5, \
                               QtCore.SIGNAL("clicked()"), \
                               self.loadQueries)
        QtCore.QObject.connect(self.pushButton_6, \
                               QtCore.SIGNAL("clicked()"), \
                               self.deleteQuery)
        
        
        QtCore.QObject.connect(self.radioButton, 
                               QtCore.SIGNAL('clicked(bool)'), 
                               self.radioButton_clicked)
        QtCore.QObject.connect(self.radioButton_2, 
                               QtCore.SIGNAL('clicked(bool)'), 
                               self.radioButton_clicked)
        QtCore.QObject.connect(self.radioButton_3, 
                               QtCore.SIGNAL('clicked(bool)'), 
                               self.radioButton_clicked)
                               
        self.myData = None
        self.squery = skyQuery()
        self.db = None
        self.dbOption = 'Other'
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        try:
            os.mkdir('./skyQuery_cache')
        except:
            print 'Cache Folder exist'
            
        os.chdir('./skyQuery_cache/')
            
    def __querySDSS(self, myquery):
        tables = self.squery.dataQuery(myquery)
        self.textEdit.setHtml('')
        self.myData = None
        if(tables[0] == None):
            print tables[1]
            QtGui.QMessageBox.information(self, 'Data Problem', tables[1])
        else:
            html2 = '''<html><head>
        <title>SDSS Query Results</title>
        </head><body bgcolor=white>
        <div align=\'center\'>
        %s
        </div>
        </BODY></HTML>
        ''' %tables[0]
            self.textEdit.setHtml(html2)
            QtGui.QMessageBox.information(self, 'Data O.K.', 'Data recived see tab Data recived')
            self.myData = tables

                               
    def querySDSS(self):
        'Submite The Query for Sky Server'
        myquery =  unicode(self.plainTextEdit.toPlainText())
        self.__querySDSS(myquery)
        
    def queryfromExistentQuery(self):
        if(unicode(self.textEdit_2.toPlainText()) != ''):            
            self.__querySDSS(unicode(self.textEdit_2.toPlainText()) )
            
            
    def saveCVS(self, myListData):
        nameLoc = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.cvs', self.tr('cvs (*.cvs)'))
        arq = open(unicode(nameLoc), 'w')
        
        for dado in myListData:
            tmp = ''            
            for valor in dado:
                tmp+=str(valor)+';' 
            tmp = tmp[:-1]+'\n'
            arq.write(tmp)
        arq.close()

    def saveData(self):
        if(self.myData != None):
            myListData = self.squery.dataExtraction(self.myData)
            if(self.dbOption == 'cvs'):
                self.saveCVS(myListData)
            else:
                self.tableModel(myListData)
        else:
             QtGui.QMessageBox.information(self, 'Data.', 'No data recived')
             
    def __tableModel(self, myListData):
        fields = myListData[0]
        if(self.dbOption == 'Other'):
            tmpDB = unicode(self.lineEdit_6.text())+'://'+\
                            unicode(self.lineEdit_3.text())+':'+\
                            unicode(self.lineEdit_4.text())+'@'+\
                            unicode(self.lineEdit_5.text())+'/'+\
                            replace(unicode(self.lineEdit_2.text()), ' ', '_')
                            
        elif(self.dbOption == 'SQLite'):
            tmpDB = 'sqlite://'+replace(unicode(self.lineEdit_2.text()), ' ', '_')
            
        tableName = unicode(self.lineEdit.text())
        tableName = replace(tableName, ' ', '_')
        defineTableFields = '\''+unicode(self.lineEdit.text())+'\''
        defineTableCode = """#!/usr/bin/env python
#*-* Coding : UTF-8 *-*
\'\'\' This Code was authomatic generated by SkyQuery program\'\'\'
from gluon import *
db =  DAL(\'%s\')
def tableDB(db):        
        """ %tmpDB
        
        for data in fields:
            defineTableFields +=',Field(\''+data+'\',type=\'double\')'
        
        tableModel = """
    db.define_table(%s)
        
        """ %defineTableFields
        
        defineTableCode = defineTableCode+tableModel+"""
def insertDataTable(db):
        """
                   
    
        
        for row in myListData[1:]:
            defineInsertFields = ''
            for i in range(len(row)):
                defineInsertFields += fields[i]+'='+str(row[i])+','
            insertDataTable = """
    db.%s.insert(%s)
    db.commit()
            
            """ %(tableName, defineInsertFields[:-1])
            defineTableCode = defineTableCode+insertDataTable
            
        endProg = """
tableDB(db)
insertDataTable(db)
        """
        defineTableCode = defineTableCode+endProg
        #print defineTableCode 
        exec(defineTableCode)
        
            
    def tableModel(self, myListData):       
        self.dataEntryValidator(self.__tableModel, myListData)
            
    def dataEntryValidator(self, func, *args):       
        if(unicode(self.lineEdit.text()) != ''):
            if(unicode(self.lineEdit_2.text()) != ''):
                if(self.dbOption == 'Other'):
                    if(unicode(self.lineEdit_3.text()) == ''):
                        QtGui.QMessageBox.information(self, 'Table Name.', 'It is necessary the user name of DB')
                    elif(unicode(self.lineEdit_4.text()) == ''):
                        QtGui.QMessageBox.information(self, 'Table Name.', 'It is necessary the password name of DB')
                    else:
                        func(*args)
                else:
                    func(*args)
                
            else:
                QtGui.QMessageBox.information(self, 'Table Name.', 'It is necessary define a name for the database')
        else:
            QtGui.QMessageBox.information(self, 'Table Name.', 'It is necessary define a name for the database table')
    
    def __searchQuery(self, myquery):
        
        if(self.dbOption == 'Other'):
            tmpDB = unicode(self.lineEdit_6.text())+'://'+\
                            unicode(self.lineEdit_3.text())+':'+\
                            unicode(self.lineEdit_4.text())+'@'+\
                            unicode(self.lineEdit_5.text())+'/'+\
                            replace(unicode(self.lineEdit_2.text()), ' ', '_')
                            
        elif(self.dbOption == 'SQLite'):
            tmpDB = 'sqlite://'+replace(unicode(self.lineEdit_2.text()), ' ', '_')
            

        defineTableCode = """
try:
    self.db =  DAL(\'%s\')
except:
    self.db = None        
        """ %(tmpDB)
        exec(defineTableCode)
        if(self.db != None):
            self.db.define_table('skyQueryQueries',Field('query','text',  requires = IS_NOT_IN_DB(self.db,'skyQueryQueries.query')))
            myselection = self.db(self.db.skyQueryQueries.query == myquery ).select()[0]
            self.db(self.db.skyQueryQueries.id == myselection['id']).delete()
            self.db.commit()
            
    def searchQuery(self, myquery):
        self.__searchQuery(myquery)
        
    def deleteQuery(self):
        if(unicode(self.textEdit_2.toPlainText()) != ''):
            query = unicode(self.textEdit_2.toPlainText())
            self.searchQuery(query)
            self.item = self.listWidget.takeItem(self.listWidget.currentRow())
            self.item = None
            self.textEdit_2.setText('')
    
    def listOfQueries(self, dados):

        for dado in dados:
            item = QtGui.QListWidgetItem(dado)
            self.listWidget.addItem(item)
                
                
    def radioButton_clicked(self):
        radiobutton = self.sender()
        self.dbOption = radiobutton.text()
        
    def listQueryClicked(self, qmodelindex ):
        self.item = qmodelindex.data(QtCore.Qt.DisplayRole).toString()
        self.textEdit_2.setText(self.item)
        
    def __saveQuery(self, query):
        if(self.dbOption == 'Other'):
            tmpDB = unicode(self.lineEdit_6.text())+'://'+\
                            unicode(self.lineEdit_3.text())+':'+\
                            unicode(self.lineEdit_4.text())+'@'+\
                            unicode(self.lineEdit_5.text())+'/'+\
                            replace(unicode(self.lineEdit_2.text()), ' ', '_')
                            
        elif(self.dbOption == 'SQLite'):
            tmpDB = 'sqlite://'+replace(unicode(self.lineEdit_2.text()), ' ', '_')
            
        tableName = unicode(self.lineEdit.text())
        tableName = replace(tableName, ' ', '_')
        defineTableFields = '\''+unicode(self.lineEdit.text())+'\''
        defineTableCode = """
try:
    self.db =  DAL(\'%s\')
except:
    self.db = None        
        """ %(tmpDB)
        exec(defineTableCode)
        if(self.db != None):
            self.db.define_table('skyQueryQueries',Field('query','text',  requires = IS_NOT_IN_DB(self.db,'skyQueryQueries.query')))
            
            validator = self.db.skyQueryQueries.query.validate(query)
            if(validator[1] == 'value already in database or empty'):
                QtGui.QMessageBox.information(self, 'Save Query.', 'Query already in the database')
            else:
                self.db.skyQueryQueries.insert(query= query)
                self.db.commit()
        
    def saveQuery(self):
        myquery =  unicode(self.plainTextEdit.toPlainText())
        self.dataEntryValidator(self.__saveQuery, myquery)
            
    
    def __loadQueries(self):
        if(self.dbOption == 'Other'):
            tmpDB = unicode(self.lineEdit_6.text())+'://'+\
                            unicode(self.lineEdit_3.text())+':'+\
                            unicode(self.lineEdit_4.text())+'@'+\
                            unicode(self.lineEdit_5.text())+'/'+\
                            replace(unicode(self.lineEdit_2.text()), ' ', '_')
                            
        elif(self.dbOption == 'SQLite'):
            tmpDB = 'sqlite://'+replace(unicode(self.lineEdit_2.text()), ' ', '_')
            
        tableName = unicode(self.lineEdit.text())
        tableName = replace(tableName, ' ', '_')
        defineTableFields = '\''+unicode(self.lineEdit.text())+'\''
        defineTableCode = """
try:
    self.db =  DAL(\'%s\')
except:
    self.db = None        
        """ %(tmpDB)
        exec(defineTableCode)
        if(self.db != None):
            self.db.define_table('skyQueryQueries',Field('query','text',  requires = IS_NOT_IN_DB(self.db,'skyQueryQueries.query')))
            
            selectQueries = self.db().select(self.db.skyQueryQueries.ALL, orderby=self.db.skyQueryQueries.id)
            
            dados = [row['query'] for row in  selectQueries]
            self.listOfQueries(dados)
            
            
            
        
    def loadQueries(self):
        self.dataEntryValidator(self.__loadQueries)

        
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dmw = DesignerMainWindow()
    dmw.show()
    sys.exit(app.exec_())
