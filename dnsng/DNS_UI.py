from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from DNSNG_UI import Ui_dlgDNS
from db_model import Redirect, ClientHost, DNSRequest
from db_code import get_db_session

from subprocess import check_output, call, CalledProcessError

import sys
import time

class DnsUI(QtGui.QDialog, Ui_dlgDNS):
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.setLayout(self.verticalLayout)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        
        #Signal handler connections
        self.connect(self.cmdClose, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        
        self.connect(self.cmdRefresh, QtCore.SIGNAL("clicked()"), self.reloadRedirects)
        self.connect(self.cmdRefresh, QtCore.SIGNAL("clicked()"), self.updateServerStatusUI)
        
        self.connect(self.cmdToggleServer, QtCore.SIGNAL("clicked()"), self.toggleServerStatus)
        
        self.connect(self.rdoOn, QtCore.SIGNAL("clicked()"), self.toggleRequestsView)
        self.connect(self.rdoOff, QtCore.SIGNAL("clicked()"), self.toggleRequestsView)
        
        self.connect(self.cmdAdd, QtCore.SIGNAL("clicked()"), self.addRecord)
        self.connect(self.cmdSave, QtCore.SIGNAL("clicked()"), self.saveRecords)
        self.connect(self.cmdDelete, QtCore.SIGNAL("clicked()"), self.deleteRecord)
        
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.getDNSRequests)
        
        self.objDB = get_db_session()
        
        
        self.txtDNSRequests.setText("Incoming DNS Queries")
        self.lastRequestID = self.getLastRequestID()
        
        # Check server status and update user interface accordingly
        self.updateServerStatusUI()
        
        
        if '' != self.serverPID:
            self.timer.start()
        
        
        self.reloadRedirects()
    
    def getLastRequestID(self):
        "Returns the last req_id from the DNS requests table"
        
        
        q = self.objDB.query(DNSRequest).order_by(DNSRequest.req_id.desc()).first()
        if None != q:
            return q.req_id
        else:
            return None
    
    def getDNSRequests(self):
        "Fetch incoming DNS requests from the DB and display them in txtDNSRequests"
        
        if self.serverPID is None:
            return
        
        q = self.objDB.query(DNSRequest)
        if self.lastRequestID:
            
            q=self.objDB.query(DNSRequest).filter('req_id>%s' % str(self.lastRequestID))
        
        
        
        for R in q:
            s = "[%s] Query %s [%s] from %s" % (str(R.request_time), R.request_query, R.query_type, R.host.host_ip)
            self.txtDNSRequests.append(s)
            self.lastRequestID = R.req_id
    
    def addRecord(self):
        "Add a row to the redirects table so user can enter data into its fields"
        r_num = self.tblRedirects.rowCount()
        self.tblRedirects.insertRow(r_num)
        
        item = QtGui.QTableWidgetItem('')
        item.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        
        self.tblRedirects.setItem(r_num, 0, item)
        self.tblRedirects.setItem(r_num, 1, QtGui.QTableWidgetItem(''))
        self.tblRedirects.setItem(r_num, 2, QtGui.QTableWidgetItem(''))
        self.tblRedirects.setItem(r_num, 3, QtGui.QTableWidgetItem(''))
        self.tblRedirects.setItem(r_num, 4, QtGui.QTableWidgetItem(''))
        self.tblRedirects.setItem(r_num, 5, QtGui.QTableWidgetItem(''))
        
    
    def saveRecords(self):
        "Save records back to the DB"
        
        for r_num in range(0, self.tblRedirects.rowCount()):
            
            rule_id = str(self.tblRedirects.item(r_num, 0).text()).strip()
            
            if '' != rule_id:
                #existing record, update.
                R = self.objDB.query(Redirect).filter_by(rule_id=int(rule_id)).one()
                
            else:
                #new record, add.
                R = Redirect('', '', '', '')
            
            R.redirect_ip = self.tblRedirects.item(r_num, 1).text()
            R.client_host_specs = self.tblRedirects.item(r_num, 2).text()
            R.query_domain = self.tblRedirects.item(r_num, 3).text()
            R.query_type = self.tblRedirects.item(r_num, 4).text()
            if 'true' == str(self.tblRedirects.item(r_num, 5).text()).strip().lower():
                R.enabled = True
            else:
                R.enabled = False
            
            if '' == rule_id:
                print("Adding record %s" % str(R))
                self.objDB.add(R)
                
            
            self.objDB.commit()
        
        
        self.reloadRedirects()
    
    def deleteRecord(self):
        "Delete currently selected record"
        r_num = self.tblRedirects.currentRow()
        if None != r_num:
            rule_id = str(self.tblRedirects.item(r_num, 0).text()).strip()
            if '' != rule_id:
                R = self.objDB.query(Redirect).filter_by(rule_id=int(rule_id)).one()
                self.objDB.delete(R)
                self.objDB.commit()
            
            
            self.tblRedirects.removeRow(r_num)
            
    def updateServerPID(self):
        "Returns server PID or empty string if server is not running"
        server_pid = ""
        
        try:
            server_pid = check_output(["pidof", "DNS_NG"]).strip()
        except CalledProcessError:
            server_pid = ""
        
        self.serverPID = server_pid
    
    def updateServerStatusUI(self):
        "Update controls related to server status"
        
        self.updateServerPID()
        
        if "" != self.serverPID:
            self.lblServerStatus.setText("RUNNING")
            self.lblServerStatus.setStyleSheet("color: green; font-weight: bold; font-size: 14pt;")
            self.lblServerPID.setText("(PID: %s)" % self.serverPID)
            self.cmdToggleServer.setText("Stop Server")
            
        else:
            self.lblServerStatus.setText("NOT RUNNING")
            self.lblServerStatus.setStyleSheet("color: red; font-weight: bold; font-size: 14pt;")
            self.lblServerPID.setText("     ")
            self.cmdToggleServer.setText("Start Server")
    
    
    def toggleServerStatus(self):
        "Start or stop the server"
        
        if "" == self.serverPID:
            # start server
            try:
                ret = call(["python", "DNS_NG.py", "--daemon"])
                self.updateServerStatusUI()
                
            except CalledProcessError:
                QtGui.QMessageBox.critical(self, "Error", "Error starting server")
            
        else:
            #stop server
            try:
                ret = call(["killall", "DNS_NG"])
                time.sleep(1)
                self.updateServerStatusUI()
            except CalledProcessError:
                QtGui.QMessageBox.critical(self, "Error", "Error stoping server")
            
    
    def toggleRequestsView(self):
        "turns DNS requests viewing on or off"
        self.txtDNSRequests.setVisible(self.rdoOn.isChecked())
        
        if self.rdoOn.isChecked():
            self.timer.start()
        else:
            self.timer.stop()
        
    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, "Really Quit?", "Are you sure you want to quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def reloadRedirects(self):
        redirects = self.objDB.query(Redirect)
        
        self.tblRedirects.setRowCount(redirects.count())
        
        for r_num, R in enumerate(redirects):
            item = QtGui.QTableWidgetItem(str(R.rule_id))
            item.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
            
            self.tblRedirects.setItem(r_num, 0, item)
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
