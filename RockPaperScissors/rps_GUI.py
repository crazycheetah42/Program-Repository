from PyQt5 import QtCore, QtGui, QtWidgets
import random
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(140, 0, 491, 31))
        self.welcome.setObjectName("welcome")
        self.lbl_option_prompt = QtWidgets.QLabel(self.centralwidget)
        self.lbl_option_prompt.setGeometry(QtCore.QRect(40, 50, 431, 31))
        self.lbl_option_prompt.setObjectName("lbl_option_prompt")
        self.wintie = QtWidgets.QLabel(self.centralwidget)
        self.wintie.setGeometry(QtCore.QRect(150, 300, 491, 121))
        self.wintie.setText("")
        self.wintie.setObjectName("wintie")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(270, 120, 261, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 130, 99, 30))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        def rps_code(MainWindow):
            bot_rps_options = ["Rock", "Paper", "Scissors"]
            bot_rps = random.choice(bot_rps_options)
            if self.pushButton.clicked:
                if self.plainTextEdit.toPlainText() == "Rock":
                    player_rps = "Rock"
                    if player_rps == "Rock":
                        if bot_rps == "Paper":
                            self.wintie.setText("Paper beats rock, Bot wins!")
                        elif bot_rps == "Rock":
                            self.wintie.setText("Tie!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Rock crushes Scissors, Player wins!")
                    if player_rps == "Paper":
                        if bot_rps == "Rock":
                            self.wintie.setText("Paper beats Rock, Player wins!")
                        elif bot_rps == "Paper":
                            self.wintie.setText("Tie!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Scissors cut paper, Bot wins!")
                    if player_rps == "Scissors":
                        if bot_rps == "Rock":
                            self.wintie.setText("Rock crushes scissors, Bot wins!")
                        elif bot_rps == "Paper":
                            self.wintie.setText("Scissors cut paper, Player wins!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Tie!")

                if self.plainTextEdit.toPlainText() == "Paper":
                    player_rps = "Paper"
                    if player_rps == "Rock":
                        if bot_rps == "Paper":
                            self.wintie.setText("Paper beats rock, Bot wins!")
                        elif bot_rps == "Rock":
                            self.wintie.setText("Tie!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Rock crushes Scissors, Player wins!")
                    if player_rps == "Paper":
                        if bot_rps == "Rock":
                            self.wintie.setText("Paper beats Rock, Player wins!")
                        elif bot_rps == "Paper":
                            self.wintie.setText("Tie!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Scissors cut paper, Bot wins!")
                    if player_rps == "Scissors":
                        if bot_rps == "Rock":
                            self.wintie.setText("Rock crushes scissors, Bot wins!")
                        elif bot_rps == "Paper":
                            self.wintie.setText("Scissors cut paper, Player wins!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Tie!")

                if self.plainTextEdit.toPlainText() == "Scissors":
                    player_rps = "Scissors"
                    if player_rps == "Rock":
                        if bot_rps == "Paper":
                            self.wintie.setText("Paper beats rock, Bot wins!")
                        elif bot_rps == "Rock":
                            self.wintie.setText("Tie!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Rock crushes Scissors, Player wins!")
                    if player_rps == "Paper":
                        if bot_rps == "Rock":
                            self.wintie.setText("Paper beats Rock, Player wins!")
                        elif bot_rps == "Paper":
                            self.wintie.setText("Tie!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Scissors cut paper, Bot wins!")
                    if player_rps == "Scissors":
                        if bot_rps == "Rock":
                            self.wintie.setText("Rock crushes scissors, Bot wins!")
                        elif bot_rps == "Paper":
                            self.wintie.setText("Scissors cut paper, Player wins!")
                        elif bot_rps == "Scissors":
                            self.wintie.setText("Tie!")
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(rps_code)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Welcome to Rock Paper Scissors, Python Edition!"))
        self.lbl_option_prompt.setText(_translate("MainWindow", "Player, please choose your option. Rock, Paper, or Scissors?"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Replace this text with your choice\n"
""))
        self.pushButton.setText(_translate("MainWindow", "Done!"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

