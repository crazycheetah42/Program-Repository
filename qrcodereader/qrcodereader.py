from PyQt5 import QtCore, QtGui, QtWidgets
import qrtools
class Ui_Form(object):
    def code(self):
        qr = qrtools.QR()
        filename = self.textEdit.toPlainText()
        qr.decode(filename)
        self.textBrowser.setText(qr.data)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(939, 801)
        font = QtGui.QFont()
        font.setPointSize(20)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 0, 211, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(240, 100, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 160, 95, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(110, 210, 721, 471))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton.clicked.connect(self.code)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QRCode Reader"))
        self.label.setText(_translate("Form", "QRCode Reader"))
        self.label_2.setText(_translate("Form", "By Aryaman Sriram"))
        self.textEdit.setPlaceholderText(_translate("Form", "Enter the filename or the whole path here:"))
        self.pushButton.setText(_translate("Form", "Decode"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
