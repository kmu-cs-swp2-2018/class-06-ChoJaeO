from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
import sys
import keypad
import calcfunction

class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        backspace = Button("지우기")
        backspace.clicked.connect(self.buttonClicked)

        #Error Label
        self.errorlabel = QLabel()

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(len(self.digitButton)):
            self.digitButton[i] = Button(str(i))
        # . and = Buttons
        self.decButton = Button('.')
        self.eqButton = Button('=')

        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        self.buttonGroups = {
            'op' : {'buttons' : keypad.operatorList, 'layout' : opLayout, 'columns' : 2},
            'constants' : {'buttons' : keypad.constantList[0], 'layout' : constLayout, 'columns' : 1},
            'functions' : {'buttons' : keypad.functionList, 'layout' : funcLayout, 'columns' : 1},
        }


        print(keypad.operatorList)
        for label in self.buttonGroups.keys():
            r = 0
            c = 0
            buttonInfo = self.buttonGroups[label]
            for btnText in buttonInfo['buttons']:
                button = Button(btnText)
                buttonInfo['layout'].addWidget(button,r,c)
                print(buttonInfo['buttons'])
                button.clicked.connect(self.buttonClicked)
                c += 1
                if c >= buttonInfo['columns']:
                    c = 0
                    r += 1
        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 1)
        mainLayout.addWidget(backspace,0,1,1,1)
        mainLayout.addWidget(self.errorlabel,1,0)

        numLayout = QGridLayout()
        cnt = 0
        for i in range(4):
            if i == 0:
                numLayout.addWidget(self.digitButton[0], 3, 0)
                continue
            n = 3-i
            for j in range(3):
                numLayout.addWidget(self.digitButton[(i-1)*3 + j + 1], n, j)
                cnt += 1

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 2, 0)
        mainLayout.addLayout(opLayout, 2, 1)
        mainLayout.addLayout(constLayout, 3, 0)
        mainLayout.addLayout(funcLayout,3,1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")

        for i in self.digitButton:
            i.clicked.connect(self.buttonClicked)
        self.decButton.clicked.connect(self.buttonClicked)
        self.eqButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        button = self.sender()
        inputstr = button.text()
        self.errorlabel.setText("")
        if self.display.text() == 'Error':
            self.display.setText('')
        if inputstr == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except ZeroDivisionError:
                self.errorlabel.setText("0으로 해당숫자를 나눌 수 없습니다.")
            except:
                self.errorlabel.setText("Error")
        elif inputstr == "지우기":
            text_display = str(self.display.text())
            text_display = text_display[0:len(text_display)-1]
            self.display.setText(text_display)
        elif inputstr == 'C':
            self.display.clear()
        elif inputstr in keypad.constantList[0]:
            index_key = keypad.constantList[0].index(inputstr)
            text_display = str(self.display.text()) + keypad.constantList[1][index_key]
            self.display.setText(text_display)
        elif inputstr == keypad.functionList[0]:
            func_result = calcfunction.factorial_function(int(self.display.text()))
            self.display.setText(func_result)
        elif inputstr == keypad.functionList[1]:
            func_result = calcfunction.binary_function(int(self.display.text()))
            self.display.setText(func_result)
        elif inputstr == keypad.functionList[2]:
            func_result = calcfunction.dec_function(int(self.display.text()))
            self.display.setText(func_result)
        elif inputstr == keypad.functionList[3]:
            func_result = calcfunction.roman(int(self.display.text()))
            self.display.setText(func_result)
        elif inputstr == keypad.functionList[4]:
            func_result = calcfunction.romantodec(self.display.text())
            if func_result == "Error":
                self.errorlabel.setText("로마 숫자를 입력해야 합니다.")
            else:
                self.display.setText(str(func_result))
        else:
            text_display = str(self.display.text()) + inputstr
            self.display.setText(text_display)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

