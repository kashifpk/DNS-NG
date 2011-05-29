# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DNS-NG-UI.ui'
#
# Created: Sun May 29 06:26:14 2011
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
        dlgDNS.resize(663, 641)
        self.verticalLayoutWidget = QtGui.QWidget(dlgDNS)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 641))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("font-weight: bold; font-size: 12pt;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.lblServerStatus = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblServerStatus.setStyleSheet(_fromUtf8("color: rgb(0, 192, 0);\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
""))
        self.lblServerStatus.setObjectName(_fromUtf8("lblServerStatus"))
        self.horizontalLayout_4.addWidget(self.lblServerStatus)
        self.lblServerPID = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblServerPID.setText(_fromUtf8(""))
        self.lblServerPID.setObjectName(_fromUtf8("lblServerPID"))
        self.horizontalLayout_4.addWidget(self.lblServerPID)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.cmdToggleServer = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdToggleServer.setObjectName(_fromUtf8("cmdToggleServer"))
        self.horizontalLayout_4.addWidget(self.cmdToggleServer)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
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
        self.cmdAdd = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdAdd.setObjectName(_fromUtf8("cmdAdd"))
        self.horizontalLayout_2.addWidget(self.cmdAdd)
        self.cmdSave = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout_2.addWidget(self.cmdSave)
        self.cmdDelete = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdDelete.setObjectName(_fromUtf8("cmdDelete"))
        self.horizontalLayout_2.addWidget(self.cmdDelete)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
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
        self.rdoOn = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoOn.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);"))
        self.rdoOn.setChecked(True)
        self.rdoOn.setObjectName(_fromUtf8("rdoOn"))
        self.horizontalLayout.addWidget(self.rdoOn)
        self.rdoOff = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoOff.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.rdoOff.setObjectName(_fromUtf8("rdoOff"))
        self.horizontalLayout.addWidget(self.rdoOff)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.cmdClose = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.horizontalLayout.addWidget(self.cmdClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dlgDNS)
        QtCore.QMetaObject.connectSlotsByName(dlgDNS)

    def retranslateUi(self, dlgDNS):
        dlgDNS.setWindowTitle(QtGui.QApplication.translate("dlgDNS", "DNS-NG", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgDNS", "DNS Server Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblServerStatus.setText(QtGui.QApplication.translate("dlgDNS", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdToggleServer.setText(QtGui.QApplication.translate("dlgDNS", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("dlgDNS", "Rule ID", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("dlgDNS", "Redirect IP", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("dlgDNS", "Client Specs RE", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("dlgDNS", "Query Domain RE", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("dlgDNS", "Query Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tblRedirects.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("dlgDNS", "Enabled?", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAdd.setToolTip(QtGui.QApplication.translate("dlgDNS", "Add a record", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAdd.setText(QtGui.QApplication.translate("dlgDNS", "Add Record", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setToolTip(QtGui.QApplication.translate("dlgDNS", "Save all changed and added records", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("dlgDNS", "Save All", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setToolTip(QtGui.QApplication.translate("dlgDNS", "Delete currently selected row", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDelete.setText(QtGui.QApplication.translate("dlgDNS", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdRefresh.setText(QtGui.QApplication.translate("dlgDNS", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDNSRequests.setHtml(QtGui.QApplication.translate("dlgDNS", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rdoOn.setToolTip(QtGui.QApplication.translate("dlgDNS", "Display incoming DNS requests", None, QtGui.QApplication.UnicodeUTF8))
        self.rdoOn.setText(QtGui.QApplication.translate("dlgDNS", "On", None, QtGui.QApplication.UnicodeUTF8))
        self.rdoOff.setToolTip(QtGui.QApplication.translate("dlgDNS", "Turn off incoming DNS requests display", None, QtGui.QApplication.UnicodeUTF8))
        self.rdoOff.setText(QtGui.QApplication.translate("dlgDNS", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("dlgDNS", "Close", None, QtGui.QApplication.UnicodeUTF8))

