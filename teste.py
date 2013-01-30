import sys

# import PyQt:
from PyQt4 import QtCore, QtGui, QtWebKit

# import web2py libraries
sys.path.append(r"/home/gianni/web2py")
from gluon.dal import DAL, Field
from gluon.sqlhtml import SQLFORM
from gluon.html import INPUT, FORM, TABLE, TR, TD
from gluon.validators import IS_NOT_EMPTY, IS_EXPR, IS_NOT_IN_DB, IS_IN_SET
from gluon.storage import Storage

    
def main():
    # create DAL connection (and create DB if not exists)
    db=DAL('sqlite://guitest.sqlite',folder=None)

    # define a table 'person' (create/aster as necessary)
    person = db.define_table('person',
        Field('name','string', length=100),
        Field('sex','string', length=1),
        Field('active','boolean', comment="check!"),
        Field('bio','text', comment="resume (CV)"),
        )

    # set sample validator (do not allow empty nor duplicate names)
    db.person.name.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'person.name')]
    db.person.sex.requires = IS_IN_SET({'M': 'Male', 'F': 'Female'})

    #>> create the PyQt GUI application instance:
    app = QtGui.QApplication(sys.argv)

    #>> create a testing view (Qt):
    webView = QtWebKit.QWebView(title="web2py/pyqt sample app")
    # webView.page() gives you the page
    # webView.page().mainFrame() gives you the frame

    # create the web2py FORM based on person table
    form = SQLFORM(db.person)

    # convert the web2py FORM to XML and display it
    webView.setHtml(form.xml())
    
    # some form-submit handler here
    def on_form_submit(evt):
	    # where evt is supposed to carry the needed form's information
	    print "HERE WE ARE!"

    # HERE IS THE MISSING POINT:
    # how to "connect the FORM submit event with the HTML browser" now ???
    # In the wxPython case it's solved by: html.Bind(EVT_FORM_SUBMIT, on_form_submit)

    # show the main window
    window = QtGui.QMainWindow()
    window.setCentralWidget(webView)
    window.show()
    
    # start the Qt loop to interact with the user
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()
