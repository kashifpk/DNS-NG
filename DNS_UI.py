from PyQt4 import QtCore, QtGui
from DNSNG_UI import Ui_dlgDNS
from db_model import Redirect, ClientHost, DNSRequest
from db_code import get_db_session

import sys

class DnsUI(QtGui.QDialog, Ui_dlgDNS):
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.connect(self.cmdRefresh, QtCore.SIGNAL("clicked()"), self.reloadRedirects)
        
        self.objDB = get_db_session()
        self.reloadRedirects()
    
    
    def reloadRedirects(self):
        redirects = self.objDB.query(Redirect)
        
        self.tblRedirects.setRowCount(redirects.count())
        
        for r_num, R in enumerate(redirects):
            self.tblRedirects.setItem(r_num, 0, QtGui.QTableWidgetItem(str(R.rule_id)))
            self.tblRedirects.setItem(r_num, 1, QtGui.QTableWidgetItem(R.redirect_ip))
            self.tblRedirects.setItem(r_num, 2, QtGui.QTableWidgetItem(R.client_host_specs))
            self.tblRedirects.setItem(r_num, 3, QtGui.QTableWidgetItem(R.query_domain))
            self.tblRedirects.setItem(r_num, 4, QtGui.QTableWidgetItem(R.query_type))
            self.tblRedirects.setItem(r_num, 5, QtGui.QTableWidgetItem(str(R.enabled)))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    run = DnsUI()
    run.show()
    sys.exit(app.exec_())
