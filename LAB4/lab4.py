import sys
from communicate import Serial_Talker # custom defined serial communication class

# Libraries necessary for the GUI
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Motor A state variables
motorA_state = 0      # 0 -> off , 1 -> on
motorA_direction = 0  # initially ccw, 0 -> ccw, 1 -> cw  
motorA_dutyCycle = 0  # initially 0, dutyCycle integer [0, 65535]
motorA_pwmFreq = 50   # initially 50, dutyCycle integer [1, 1000]

# Motor B state variables
motorB_state = 0      # 0 -> off , 1 -> on
motorB_direction = -1 # -1 -> not defined, 0 -> ccw, 1 -> cw  
motorB_dutyCycle = 0  # initially 0, dutyCycle integer [0, 65535]
motorB_pwmFreq = 50   # initially 50, dutyCycle integer [1, 1000]

talker = Serial_Talker() # Initialize serial communication with pico

'''
Parameters to be send to pico

motorA_state : 1 or 0
motorA_direction : 1 (cw) or 0(ccw)
motorA_dutyCycle : 0 to 65535
motorA_pwmFreq : 1 Hz to 1kHz

motorB_state : 1 or 0
motorB_direction : 1 (cw) or 0(ccw)
motorB_dutyCycle : 0 to 65535
motorB_pwmFreq : 1 Hz to 1kHz
'''

class Ui_MainWindow(object):

    def send_message_A(self):
        global motorA_state, motorA_direction, motorA_dutyCycle, motorA_pwmFreq
        talker.send(f'0 {motorA_state} {motorA_direction} {motorA_dutyCycle} {motorA_pwmFreq}')
    
    ### FIX THIS KLATER
    def send_message_B(self):
        global motorB_state, motorB_direction, motorB_dutyCycle, motorB_pwmFreq
        talker.send(f'1 {motorB_state} {motorB_direction} {motorB_dutyCycle} {motorB_pwmFreq}')

    #### FUNCTIONS MOTOR A
    def startA_routine(self):
        global motorA_state, motorA_direction, motorA_dutyCycle, motorA_pwmFreq
        motorA_state = 1
        self.textBrowser_2.append(f'motorA_state : {motorA_state}')

        self.send_message_A()

    def stopA_routine(self):
        global motorA_state, motorA_direction, motorA_dutyCycle, motorA_pwmFreq
        motorA_state = 0
        self.textBrowser_2.append(f'motorA_state : {motorA_state}')

        self.send_message_A()

    def motorA_direction_routine(self):
        global motorA_state, motorA_direction, motorA_dutyCycle, motorA_pwmFreq
        if self.radioButton_28.isChecked():
            motorA_direction = 0 #ccw
        elif self.radioButton_27.isChecked():
            motorA_direction = 1 #cw

        self.textBrowser_2.append(f'motorA_direction : {motorA_direction}\n')

        self.send_message_A()
    
    def motorA_dutyCycle_routine(self):
        global motorA_state, motorA_direction, motorA_dutyCycle, motorA_pwmFreq
        motorA_dutyCycle = int(self.horizontalScrollBar_3.value()*65535/100)
        self.lcdNumber_2.display(int(motorA_dutyCycle/65535*100))

        self.textBrowser_2.append(f'motorA_dutyCycle : {motorA_dutyCycle}\n')

        self.send_message_A()
    
    def motorA_presetDutyCycle_routine(self):
        global motorA_state, motorA_direction, motorA_dutyCycle, motorA_pwmFreq
        if not motorA_state: 
            if self.radioButton_22.isChecked():
                motorA_dutyCycle = 0
            elif self.radioButton_23.isChecked():
                motorA_dutyCycle = int(25*65535/100)
            elif self.radioButton_24.isChecked():
                motorA_dutyCycle = int(50*65535/100)
            elif self.radioButton_25.isChecked():
                motorA_dutyCycle = int(75*65535/100)
            elif self.radioButton_26.isChecked():
                motorA_dutyCycle = 65535 
            self.textBrowser_2.append(f'motorA_dutyCycle : {motorA_dutyCycle}\n')

            self.send_message_A()

    def motorA_pwmFreq_routine(self):
        global motorA_state, motorA_direction, motorA_dutyCycle, motorA_pwmFreq
        motorA_pwmFreq = int(self.horizontalScrollBar_4.value()*10)  #SET RANGE PROPERLY pwm() is btw 1 Hz AND 1kHz

        self.textBrowser_2.append(f'motorA_pwmFreq : {motorA_pwmFreq}\n')

        message = f'A{motorA_state}{motorA_direction}D{motorA_dutyCycle}F{motorA_pwmFreq}'
        talker.send(message)
    
    #### FUNCTIONS MOTOR B
        
    def startB_routine(self):
        global motorB_state, motorB_direction, motorB_dutyCycle, motorB_pwmFreq 
        motorB_state = 1
        self.textBrowser.append(f'motorB_state : {motorB_state}')

        self.send_message_B()

    def stopB_routine(self):
        global motorB_state, motorB_direction, motorB_dutyCycle, motorB_pwmFreq 
        motorB_state = 0
        self.textBrowser.append(f'motorB_state : {motorB_state}')
        
        self.send_message_B()

    def motorB_direction_routine(self):
        global motorB_state, motorB_direction, motorB_dutyCycle, motorB_pwmFreq 
        if self.radioButton_16.isChecked():
            motorB_direction = 0 #ccw
        elif self.radioButton_15.isChecked():
            motorB_direction = 1 #cw

        self.textBrowser.append(f'motorB_direction : {motorB_direction}\n')

        self.send_message_B()
    
    def motorB_dutyCycle_routine(self):
        global motorB_state, motorB_direction, motorB_dutyCycle, motorB_pwmFreq 
        motorB_dutyCycle = int(self.horizontalScrollBar.value()*65535/100)
        self.lcdNumber.display(int(motorB_dutyCycle/65535*100))

        self.textBrowser.append(f'motorB_dutyCycle : {motorB_dutyCycle}\n')

        self.send_message_B()

    def motorB_presetDutyCycle_routine(self):
        global motorB_state, motorB_direction, motorB_dutyCycle, motorB_pwmFreq 
        if self.radioButton_17.isChecked():
            motorB_dutyCycle = 0
        elif self.radioButton_18.isChecked():
            motorB_dutyCycle = int(25*65535/100)
        elif self.radioButton_19.isChecked():
            motorB_dutyCycle = int(50*65535/100)
        elif self.radioButton_20.isChecked():
            motorB_dutyCycle = int(75*65535/100)
        elif self.radioButton_21.isChecked():
            motorB_dutyCycle = 65535 
        self.textBrowser.append(f'motorB_dutyCycle : {motorB_dutyCycle}\n')

        self.send_message_B()

    def motorB_pwmFreq_routine(self):
        global motorB_state, motorB_direction, motorB_dutyCycle, motorB_pwmFreq 
        motorB_pwmFreq = self.horizontalScrollBar_2.value()   #SET RANGE PROPERLY

        self.textBrowser.append(f'motorB_pwmFreq : {motorB_pwmFreq}\n')

        self.send_message_B()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 665)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-10, 0, 901, 711))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        ########## BUTTONS
        ##### MOTOR A START
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 40, 141, 61))
        font = QFont()
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(self.startA_routine)

        ##### MOTOR A START END

        ##### MOTOR A STOP
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 400, 691, 61))
        palette2 = QPalette()
        brush1 = QBrush(QColor(237, 51, 59, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.pushButton_4.setPalette(palette2)
        self.pushButton_4.setFont(font)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 190, 131, 17))
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 290, 131, 17))
        self.pushButton_4.clicked.connect(self.stopA_routine)
        ##### MOTOR A STOP END
        ########## END BUTTONS

        ##### MOTOR A CW-CCW 
        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(40, 20, 241, 81))
        self.radioButton_27 = QRadioButton(self.groupBox_4)
        self.radioButton_27.setObjectName(u"radioButton_27")
        self.radioButton_27.setGeometry(QRect(10, 40, 112, 23))
        self.radioButton_28 = QRadioButton(self.groupBox_4)
        self.radioButton_28.setObjectName(u"radioButton_28")
        self.radioButton_28.setGeometry(QRect(130, 40, 112, 23))
        self.radioButton_28.clicked.connect(self.motorA_direction_routine)
        self.radioButton_27.clicked.connect(self.motorA_direction_routine)
        ##### MOTOR A CW-CCW END

        ##### MOTOR A DUTY CYCLE PRESET
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(310, 20, 281, 80))
        self.radioButton_22 = QRadioButton(self.groupBox_3)
        self.radioButton_22.setObjectName(u"radioButton_22")
        self.radioButton_22.setGeometry(QRect(20, 40, 112, 23))
        self.radioButton_23 = QRadioButton(self.groupBox_3)
        self.radioButton_23.setObjectName(u"radioButton_23")
        self.radioButton_23.setGeometry(QRect(60, 40, 112, 23))
        self.radioButton_24 = QRadioButton(self.groupBox_3)
        self.radioButton_24.setObjectName(u"radioButton_24")
        self.radioButton_24.setGeometry(QRect(110, 40, 112, 23))
        self.radioButton_25 = QRadioButton(self.groupBox_3)
        self.radioButton_25.setObjectName(u"radioButton_25")
        self.radioButton_25.setGeometry(QRect(160, 40, 112, 23))
        self.radioButton_26 = QRadioButton(self.groupBox_3)
        self.radioButton_26.setObjectName(u"radioButton_26")
        self.radioButton_26.setGeometry(QRect(220, 40, 112, 23))
        

        self.radioButton_22.clicked.connect(self.motorA_presetDutyCycle_routine)
        self.radioButton_23.clicked.connect(self.motorA_presetDutyCycle_routine)
        self.radioButton_24.clicked.connect(self.motorA_presetDutyCycle_routine)
        self.radioButton_25.clicked.connect(self.motorA_presetDutyCycle_routine)
        self.radioButton_26.clicked.connect(self.motorA_presetDutyCycle_routine)

        ##### MOTOR A DUTY CYCLE PRESET END

        ##### MOTOR A DUTY CYCLE SET
        self.horizontalScrollBar_3 = QScrollBar(self.tab)
        self.horizontalScrollBar_3.setObjectName(u"horizontalScrollBar_3")
        self.horizontalScrollBar_3.setGeometry(QRect(50, 220, 691, 61))
        palette = QPalette()
        brush = QBrush(QColor(98, 160, 234, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.horizontalScrollBar_3.setPalette(palette)
        self.horizontalScrollBar_3.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar_3.setMaximum(100)
        self.horizontalScrollBar_3.setMinimum(0)
        self.horizontalScrollBar_3.valueChanged.connect(self.motorA_dutyCycle_routine)
        
        ##### MOTOR A DUTY CYCLE SET END

        ##### MOTOR A PWM FREQUENCY
        self.horizontalScrollBar_4 = QScrollBar(self.tab)
        self.horizontalScrollBar_4.setObjectName(u"horizontalScrollBar_4")
        self.horizontalScrollBar_4.setGeometry(QRect(50, 320, 691, 61))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.horizontalScrollBar_4.setPalette(palette1)
        self.horizontalScrollBar_4.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar_4.valueChanged.connect(self.motorA_pwmFreq_routine)
        ##### MOTOR A PWM FREQUENCY END

        ##### MOTOR A FEEDBACK
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(50, 490, 691, 81))


        ##### MOTOR A FEEDBACK END

        ##### MOTOR A LCD
        self.lcdNumber_2 = QLCDNumber(self.tab)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(420, 120, 51, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.lcdNumber_2.setFont(font1)
        ##### MOTOR A LCD END

        ##### TAB 2
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 30, 241, 81))

        ########## BUTTONS
        
        ##### MOTOR B CW-CCW
        self.radioButton_15 = QRadioButton(self.groupBox)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setGeometry(QRect(10, 40, 112, 23))
        self.radioButton_16 = QRadioButton(self.groupBox)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setGeometry(QRect(130, 40, 112, 23))
        self.radioButton_15.clicked.connect(self.motorB_direction_routine)
        self.radioButton_16.clicked.connect(self.motorB_direction_routine)

        ##### MOTOR B START
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 410, 691, 61))

        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.pushButton_2.setPalette(palette3)
        self.pushButton_2.setFont(font)
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(640, 50, 141, 61))
        self.pushButton.setFont(font)
        self.pushButton_2.clicked.connect(self.stopB_routine)
        self.pushButton.clicked.connect(self.startB_routine)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(320, 30, 281, 80))
        self.radioButton_17 = QRadioButton(self.groupBox_2)
        self.radioButton_17.setObjectName(u"radioButton_17")
        self.radioButton_17.setGeometry(QRect(20, 40, 112, 23))
        self.radioButton_18 = QRadioButton(self.groupBox_2)
        self.radioButton_18.setObjectName(u"radioButton_18")
        self.radioButton_18.setGeometry(QRect(60, 40, 112, 23))
        self.radioButton_19 = QRadioButton(self.groupBox_2)
        self.radioButton_19.setObjectName(u"radioButton_19")
        self.radioButton_19.setGeometry(QRect(110, 40, 112, 23))
        self.radioButton_20 = QRadioButton(self.groupBox_2)
        self.radioButton_20.setObjectName(u"radioButton_20")
        self.radioButton_20.setGeometry(QRect(160, 40, 112, 23))
        self.radioButton_21 = QRadioButton(self.groupBox_2)
        self.radioButton_21.setObjectName(u"radioButton_21")
        self.radioButton_21.setGeometry(QRect(220, 40, 112, 23))

        self.radioButton_17.clicked.connect(self.motorB_presetDutyCycle_routine)
        self.radioButton_18.clicked.connect(self.motorB_presetDutyCycle_routine)
        self.radioButton_19.clicked.connect(self.motorB_presetDutyCycle_routine)
        self.radioButton_20.clicked.connect(self.motorB_presetDutyCycle_routine)
        self.radioButton_21.clicked.connect(self.motorB_presetDutyCycle_routine)

        

        self.horizontalScrollBar = QScrollBar(self.tab_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(60, 230, 691, 61))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.horizontalScrollBar.setPalette(palette4)
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar.valueChanged.connect(self.motorB_dutyCycle_routine)

        self.horizontalScrollBar_2 = QScrollBar(self.tab_2)
        self.horizontalScrollBar_2.setObjectName(u"horizontalScrollBar_2")
        self.horizontalScrollBar_2.setGeometry(QRect(60, 330, 691, 61))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.horizontalScrollBar_2.setPalette(palette5)
        self.horizontalScrollBar_2.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar_2.valueChanged.connect(self.motorB_pwmFreq_routine)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 200, 131, 17))

        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(60, 500, 691, 81))

        self.lcdNumber = QLCDNumber(self.tab_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(430, 130, 51, 41))
        self.lcdNumber.setFont(font1)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 300, 131, 17))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DC Motor Controller", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Preset Duty Cycle Values", None))
        self.radioButton_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.radioButton_23.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.radioButton_24.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.radioButton_25.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.radioButton_26.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Motor Direction", None))
        self.radioButton_27.setText(QCoreApplication.translate("MainWindow", u"CW", None))
        self.radioButton_28.setText(QCoreApplication.translate("MainWindow", u"CCW", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Duty Cycle", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PWM Frequency", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Motor A", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Motor Direction", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"CW", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"CCW", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Preset Duty Cycle Values", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Duty Cycle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PWM Frequency", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Motor B", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    gui = Ui_MainWindow()
    gui.setupUi(window)


    window.show()
  
    sys.exit(app.exec_())

    
