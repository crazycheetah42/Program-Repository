from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from googletrans import Translator
from gtts import gTTS
import qdarkstyle
import os
import sys
import playsound

class Ui_MainWindow(object):
    def playSoundFile(self):
        speech = os.path.basename(filename)
        playsound.playsound(f"{speech}")
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
    def text_to_speech(self):
        text = self.textBrowser.toPlainText()
        global tts
        tts = gTTS(text=text, lang=lang, slow="False")
        self.getSaveFileName()
    def code(self):
        try:
            translator_variable = Translator()
            text = self.textEdit.toPlainText()
            global lang
            lang = self.textEdit_2.toPlainText()
            out = translator_variable.translate(text, dest=lang)
            self.textBrowser.setText(out.text)
        except ValueError: 
            self.label_8.setText("Please specify a language to translate to.")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 842)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 20, 246, 65))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 30, 61, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 80, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 251, 41))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 200, 501, 571))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 150, 251, 41))
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(610, 300, 91, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 190, 101, 41))
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(790, 200, 541, 501))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(790, 150, 251, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1020, 740, 121, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.text_to_speech)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(590, 400, 121, 22))
        self.pushButton_2.clicked.connect(self.code)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        self.label.setText(_translate("MainWindow", "Aryaman Software"))
        self.label_2.setText(_translate("MainWindow", "Translator"))
        self.label_3.setText(_translate("MainWindow", "Enter the text to translate:"))
        self.label_5.setText(_translate("MainWindow", "Language to translate to:"))
        self.label_6.setText(_translate("MainWindow", "(en for English)"))
        self.label_7.setText(_translate("MainWindow", "Here\'s your text:"))
        self.pushButton.setText(_translate("MainWindow", "Save as speech"))
        self.pushButton_2.setText(QtCore.QCoreApplication.translate("MainWindow", u"Translate!", None))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    import darkdetect
    while True:
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