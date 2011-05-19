# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DNS-NG-UI.ui'
#
# Created: Sat May 14 18:16:53 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dlgDNS(object):
    def setupUi(self, dlgDNS):
        dlgDNS.setObjectName(_fromUtf8("dlgDNS"))
        dlgDNS.resize(543, 487)
        self.verticalLayoutWidget = QtGui.QWidget(dlgDNS)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 541, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.tblRedirects = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.tblRedirects.setMinimumSize(QtCore.QSize(400, 200))
        self.tblRedirects.setObjectName(_fromUtf8("tblRedirects"))
        self.tblRedirects.setColumnCount(6)
        self.tblRedirects.setRowCount(0)
        self.tblRedirects.setToolTip('Current redirect rules in the DNS database')
        item = QtGui.QTableWidgetItem()
        self.tblRedirects.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblRedirects.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblRedirects.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblRedirects.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblRedirects.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblRedirects.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tblRedirects)
        
        self.horizontalLayout_0 = QtGui.QHBoxLayout()
        self.horizontalLayout_0.setObjectName(_fromUtf8("horizontalLayout_0"))
        spacerItem_0 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_0.addItem(spacerItem_0)
        self.cmdRefresh = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdRefresh.setObjectName(_fromUtf8("cmdRefresh"))
        self.horizontalLayout_0.addWidget(self.cmdRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout_0)
        
        self.txtDNSRequests = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.txtDNSRequests.setEnabled(True)
        self.txtDNSRequests.setMinimumSize(QtCore.QSize(400, 200))
        self.txtDNSRequests.setObjectName(_fromUtf8("txtDNSRequests"))
        self.txtDNSRequests.setToolTip('DNS Log')
        self.verticalLayout.addWidget(self.txtDNSRequests)
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdClose = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.setLayout(self.verticalLayout)
        
        self.retranslateUi(dlgDNS)
        QtCore.QMetaObject.connectSlotsByName(dlgDNS)

    def retranslateUi(self, dlgDNS):
        dlgDNS.setWindowTitle(QtGui.QApplication.translate("dlgDNS", "DNS-NG", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("dlgDNS", "Rule ID", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("dlgDNS", "Redirect IP", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("dlgDNS", "Client Specs RE", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("dlgDNS", "Query Domain RE", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("dlgDNS", "Query Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("dlgDNS", "Enabled?", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDNSRequests.setHtml(QtGui.QApplication.translate("dlgDNS", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("dlgDNS", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdRefresh.setText(QtGui.QApplication.translate("dlgDNS", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        
        #Signal handler connections
        self.connect(self.cmdClose, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        
    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, "Really Quit?", "Are you sure you want to quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    
    



    
    
