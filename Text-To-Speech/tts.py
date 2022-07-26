"""
This is Text To Speech version 1.5.
How to use Text To Speech:
Type in your text into the large text box you've been given.
Then, click the save as button.
As of version 1.5 you have a save functionality. YOU NEED TO PUT THE SOUND FILE IN THE SAME DIRECTORY AS THE SCRIPT FOR IT TO PLAY.
IF YOU DON'T NEED IT TO PLAY AUTOMATICALLY, SAVE IT ANYWHERE YOU WANT.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from gtts import gTTS
import sys
import os
import qdarkstyle
import playsound
from time import sleep
class Ui_MainWindow(object):
    def playSoundFile(self):
        speech = os.path.basename(filename)
        playsound.playsound(speech)
    def getSaveFileName(self):
        file_filter = 'Sound File (*.mp3)'
        default = "speech.mp3"
        response = QFileDialog.getSaveFileName(
            caption='Save your generated speech',
            directory= default,
            filter=file_filter,
            initialFilter='Sound File (*.mp3)'
        )
        print(response)
        global filename
        filename = response[0]
        tts.save(filename)
        self.playSoundFile()
    def code(self):
        text = self.textEdit.toPlainText()
        global tts
        tts = gTTS(text=text, lang="en", slow="False")
        sleep(2.5)
        self.getSaveFileName()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 251, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 140, 1221, 511))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 690, 95, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.code)
        self.pushButton.setCursor(Qt.PointingHandCursor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(750, 10, 61, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("my logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text To Speech"))
        self.label.setText(_translate("MainWindow", "Aryaman Software"))
        self.label_2.setText(_translate("MainWindow", "Text To Speech"))
        self.label_3.setText(_translate("MainWindow", "Enter the text to be converted to mp3:"))
        self.pushButton.setText(_translate("MainWindow", "Save as"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    import darkdetect
    if darkdetect.isDark() == True:
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    elif darkdetect.isLight() == True:
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
