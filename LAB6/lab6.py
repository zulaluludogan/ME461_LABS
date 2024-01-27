from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

from communicate import Serial_Talker # custom defined serial communication class

'''
5 parameters to be send to pico

single_step : 4bit 
delay : float
act_sequence : actuation sequence list
run_mode : 1-> single 0-> continuous
stop_mode : 1 or 0

'''

i = 0
run_mode = 0
stop_mode = 0

talker = Serial_Talker() # Initialize serial communication with pico

class Ui_MainWindow(object):
    ### GUI FUNCTIONS

    def send_message(self):
        global i, run_mode, stop_mode, delay, act_sequence
        talker.send(f'{i} {run_mode} {stop_mode} {delay} {act_sequence}')

    def apply_singleStep(self):
        global i, run_mode, stop_mode, delay, act_sequence

        act_sequence = self.plainTextEdit.toPlainText().splitlines()
        if i < len(act_sequence):
            single_step = act_sequence[i]
            self.textBrowser.clear()
            self.textBrowser.append(f'{single_step}')
            i += 1
        else:
            i = 0
            single_step = act_sequence[i]
            self.textBrowser.clear()
            self.textBrowser.append(f'{single_step}')
            i += 1
        
        self.send_message()

    def run_continuousMode(self):
        global i, run_mode, stop_mode, delay, act_sequence
        try:
            delay = float(self.textEdit.toPlainText())
        except:
            delay = self.textEdit.toPlainText()
            print("Delay should be a float!!!")

        if isinstance(delay, float) and delay < 3000:
            act_sequence = self.plainTextEdit.toPlainText().splitlines()
            run_mode = 1
            print(delay)
            print(act_sequence)
        
        self.send_message()

    def stopAction(self):
        global i, run_mode, stop_mode, delay, act_sequence
        stop_mode = 1

        self.send_message()

    #### SET UP
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(431, 507)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 30, 201, 421))

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 240, 161, 51))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 210, 121, 17))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 300, 175, 17))

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 390, 161, 51))

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(250, 46, 161, 58))

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 110, 161, 51))

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(250, 330, 161, 51))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 431, 22))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.apply_singleStep)
        self.pushButton_2.clicked.connect(self.run_continuousMode)
        self.pushButton_3.clicked.connect(self.stopAction)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stepper Controller", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Continuous Mode", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Delay between steps (ms)", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply Single Step", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    gui = Ui_MainWindow()
    gui.setupUi(window)
    window.show()

    sys.exit(app.exec_())
    