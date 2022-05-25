from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
player = "player1"
player1 = "X"
player2 = "O"
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
class Ui_MainWindow(object):
    def code(self):
        firebaseConfig = {
            'apiKey': "AIzaSyCmddj80nuQKHN1kMprSNhkfkMFCjO-5gM",
            'authDomain': "tictactoepython-97cdc.firebaseapp.com",
            'databaseURL': "https://tictactoepython-97cdc-default-rtdb.firebaseio.com/",
            'projectId': "tictactoepython-97cdc",
            'storageBucket': "tictactoepython-97cdc.appspot.com",
            'messagingSenderId': "767593943919",
            'appId': "1:767593943919:web:0b9f9e74d1eb4263a4ce9a"
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()
        won = False
        player = "player1"
        player1 = "X"
        player2 = "O"
        data = {
            "one": one,
            "two": two,
            "three": three,
            "four": four,
            "five": five,
            "six": six,
            "seven": seven,
            "eight": eight,
            "nine": nine,
            "player": player,
            "player1": player1,
            "player2": player2
        }
        db.child("test").push(data)
    def nineclicked(self):
        if player == "player1":
            self.nine.setText("X")
            nine = "X"
            player == "player2"
        if player == "player2":
            self.nine.setText("O")
            player == "player1"
            nine = "X"
    def oneclicked(self):
        if player == "player1":
            self.one.setText("X")
            player == "player2"
            one = "X"
        if player == "player2":
            self.one.setText("O")
            player == "player1"
            one = "O"
    def twoclicked(self):
        if player == "player1":
            self.two.setText("X")
            player == "player2"
            two = "X"
        if player == "player2":
            self.two.setText("O")
            player == "player1"
            two = "O"
    def threeclicked(self):
        if player == "player1":
            self.three.setText("X")
            player == "player2"
            three = "X"
        if player == "player2":
            self.three.setText("O")
            player == "player1"
            three = "O"
    def fourclicked(self):
        if player == "player1":
            self.four.setText("X")
            player == "player2"
            four = "X"
        if player == "player2":
            self.four.setText("O")
            player == "player1" 
            four = "O"
    def fiveclicked(self):
        if player == "player1":
            self.five.setText("X")
            player == "player2"
            five = "X"
        if player == "player2":
            self.five.setText("O")
            player == "player1"
            five = "O"
    def sixclicked(self):
        if player == "player1":
            self.six.setText("X")
            player == "player2"
            six = "X"
        if player == "player2":
            self.six.setText("O")
            player == "player1"
            six = "O"
    def sevenclicked(self):
        if player == "player1":
            self.seven.setText("X")
            player == "player2"
            seven = "X"
        if player == "player2":
            self.seven.setText("O")
            player == "player1"
            seven = "O"
    def eightclicked(self):
        if player == "player1":
            self.eight.setText("X")
            player == "player2"
            eight = "X"
        if player == "player2":
            self.eight.setText("O")
            player == "player1"
            eight = "O"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(180, 90, 121, 101))
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(340, 90, 111, 101))
        self.two.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(480, 90, 111, 101))
        self.three.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three.setObjectName("three")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(180, 220, 121, 101))
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(340, 220, 121, 101))
        self.five.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(480, 220, 121, 101))
        self.six.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.six.setObjectName("six")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(180, 340, 121, 101))
        self.seven.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(340, 340, 121, 101))
        self.eight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(480, 340, 121, 101))
        self.nine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nine.setObjectName("nine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 30, 71, 21))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.one.clicked.connect(self.oneclicked)
        self.two.clicked.connect(self.twoclicked)
        self.three.clicked.connect(self.threeclicked)
        self.four.clicked.connect(self.fourclicked)
        self.five.clicked.connect(self.fiveclicked)
        self.six.clicked.connect(self.sixclicked)
        self.seven.clicked.connect(self.sevenclicked)
        self.eight.clicked.connect(self.eightclicked)
        self.nine.clicked.connect(self.nineclicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.label.setText(_translate("MainWindow", "TicTacToe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
