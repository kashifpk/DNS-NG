# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DNS-NG-UI.ui'
#
# Created: Sat May 21 18:12:32 2011
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
        dlgDNS.resize(592, 522)
        self.verticalLayoutWidget = QtGui.QWidget(dlgDNS)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 521))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tblRedirects = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.tblRedirects.setMinimumSize(QtCore.QSize(400, 200))
        self.tblRedirects.setObjectName(_fromUtf8("tblRedirects"))
        self.tblRedirects.setColumnCount(6)
        self.tblRedirects.setRowCount(0)
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cmdAddRecord = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdAddRecord.setObjectName(_fromUtf8("cmdAddRecord"))
        self.horizontalLayout_2.addWidget(self.cmdAddRecord)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cmdRefresh = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdRefresh.setObjectName(_fromUtf8("cmdRefresh"))
        self.horizontalLayout_2.addWidget(self.cmdRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.txtDNSRequests = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.txtDNSRequests.setEnabled(True)
        self.txtDNSRequests.setMinimumSize(QtCore.QSize(400, 200))
        self.txtDNSRequests.setObjectName(_fromUtf8("txtDNSRequests"))
        self.verticalLayout.addWidget(self.txtDNSRequests)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rdo_on = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdo_on.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.rdo_on.setChecked(True)
        self.rdo_on.setObjectName(_fromUtf8("rdo_on"))
        self.horizontalLayout.addWidget(self.rdo_on)
        self.rdo_off = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdo_off.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.rdo_off.setObjectName(_fromUtf8("rdo_off"))
        self.horizontalLayout.addWidget(self.rdo_off)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cmdClose = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

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
        self.cmdAddRecord.setToolTip(QtGui.QApplication.translate("dlgDNS", "Add a record", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddRecord.setText(QtGui.QApplication.translate("dlgDNS", "Add Record", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdRefresh.setText(QtGui.QApplication.translate("dlgDNS", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDNSRequests.setHtml(QtGui.QApplication.translate("dlgDNS", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_on.setToolTip(QtGui.QApplication.translate("dlgDNS", "Display incoming DNS requests", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_on.setText(QtGui.QApplication.translate("dlgDNS", "On", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_off.setToolTip(QtGui.QApplication.translate("dlgDNS", "Turn off incoming DNS requests display", None, QtGui.QApplication.UnicodeUTF8))
        self.rdo_off.setText(QtGui.QApplication.translate("dlgDNS", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("dlgDNS", "Close", None, QtGui.QApplication.UnicodeUTF8))

