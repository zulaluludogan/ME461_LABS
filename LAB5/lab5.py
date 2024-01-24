from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

'''
2 parameters to be send to pico

servo_position: 0-65536 input to analog pin 
release_motor: 0 or 1 motor to be released
'''
class Ui_MainWindow(object):
    def preset_servoPosition(self):
        global servo_position
        if self.radioButton.isChecked():
            servo_position = 0 
        elif self.radioButton_2.isChecked():
            servo_position = int(45*65536/180)
        elif self.radioButton_3.isChecked():
            servo_position = int(90*65536/180)
        elif self.radioButton_4.isChecked():
            servo_position = int(135*65536/180)
        elif self.radioButton_5.isChecked():
            servo_position = int(180*65536/180)
        print(servo_position)

    def releaseMotor(self):
        global release_motor
        release_motor = 1
        print(release_motor)
    
    def set_servoPosition(self):
        global servo_position
        servo_position = int(self.horizontalSlider.value()*65536/100)
        self.lcdNumber.display(int(servo_position/65536*180))
        print(servo_position)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"RC Servo Controller")
        MainWindow.resize(427, 202)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 20, 131, 31))

        self.pushButton.clicked.connect(self.releaseMotor)
       
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(30, 100, 361, 41))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalSlider.valueChanged.connect(self.set_servoPosition)

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(180, 70, 64, 23))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 246, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.widget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.widget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.radioButton.clicked.connect(self.preset_servoPosition)
        self.radioButton_2.clicked.connect(self.preset_servoPosition)
        self.radioButton_3.clicked.connect(self.preset_servoPosition)
        self.radioButton_4.clicked.connect(self.preset_servoPosition)
        self.radioButton_5.clicked.connect(self.preset_servoPosition)


        self.horizontalLayout.addWidget(self.radioButton_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 427, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("RC Servo Controller", u"RC Servo Controller", None))
        self.pushButton.setText(QCoreApplication.translate("RC Servo Controller", u"Release Motor", None))
        self.radioButton.setText(QCoreApplication.translate("RC Servo Controller", u"0", None))
        self.radioButton_2.setText(QCoreApplication.translate("RC Servo Controller", u"45", None))
        self.radioButton_3.setText(QCoreApplication.translate("RC Servo Controller", u"90", None))
        self.radioButton_4.setText(QCoreApplication.translate("RC Servo Controller", u"135", None))
        self.radioButton_5.setText(QCoreApplication.translate("RC Servo Controller", u"180", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    gui = Ui_MainWindow()
    gui.setupUi(window)

    window.show()

    sys.exit(app.exec_())