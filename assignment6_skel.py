import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit, QGridLayout)
import pickle

dbfilename = 'test3_4.dat'

class AssLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.NameLabel = QLabel('Name : ', self)
        self.NameText = QLineEdit()
        self.AgeLabel = QLabel('Age:',self)
        self.AgeText = QLineEdit()
        self.ScoreLabel = QLabel('Score: ', self)
        self.ScoreText = QLineEdit()
        self.AmountLabel = QLabel('Amount: ',self)
        self.AmountText = QLineEdit()
        self.KeyLabel = QLabel('Key : ',self)
        self.KeyBox = QComboBox()
        AddButton = QPushButton("Add",self)
        DelButton = QPushButton("Del",self)
        FindButton = QPushButton("Find",self)
        IncButton = QPushButton("Inc",self)
        ShowButton = QPushButton("Show",self)
        self.ResultLabel = QLabel("Result")
        self.ResultText = QTextEdit()
        self.ResultMsg = QLabel()
        self.KeyBox.addItems(['Name','Age','Score'])
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QGridLayout.SetFixedSize)
        self.ResultText.setReadOnly(True)

        mainLayout.addWidget(self.NameLabel, 0, 0, 1, 1)
        mainLayout.addWidget(self.NameText, 0, 1, 1, 1)
        mainLayout.addWidget(self.AgeLabel, 0, 2, 1, 1)
        mainLayout.addWidget(self.AgeText, 0, 3, 1, 1)
        mainLayout.addWidget(self.ScoreLabel, 0, 4, 1, 1)
        mainLayout.addWidget(self.ScoreText, 0, 5, 1, 1)
        mainLayout.addWidget(self.AmountLabel, 0, 6, 1, 1)
        mainLayout.addWidget(self.AmountText, 0, 7, 1, 1)
        mainLayout.addWidget(self.KeyLabel, 1, 6, 1, 1)
        mainLayout.addWidget(self.KeyBox, 1, 7, 1, 1)

        ButtonLayout = QGridLayout()
        ButtonLayout.addWidget(AddButton,0,0,1,1)
        ButtonLayout.addWidget(DelButton,0,1,1,1)
        ButtonLayout.addWidget(FindButton,0,2,1,1)
        ButtonLayout.addWidget(IncButton,0,3,1,1)
        ButtonLayout.addWidget(ShowButton,0,4,1,1)

        mainLayout.addLayout(ButtonLayout,2,0,1,8)

        ResultLayout = QVBoxLayout()
        ResultLayout.addWidget(self.ResultLabel)
        ResultLayout.addWidget(self.ResultMsg)
        ResultLayout.addWidget(self.ResultText)


        mainLayout.addLayout(ResultLayout,3,0,1,8)
        self.setLayout(mainLayout)
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Assignment6')

        AddButton.clicked.connect(self.buttonClicked)
        DelButton.clicked.connect(self.buttonClicked)
        FindButton.clicked.connect(self.buttonClicked)
        IncButton.clicked.connect(self.buttonClicked)
        ShowButton.clicked.connect(self.buttonClicked)


    def buttonClicked(self):
        button = self.sender()
        inputstr = button.text()
        scdb = scoredb
        name = self.NameText.text()
        age = self.AgeText.text()
        score = self.ScoreText.text()
        amount = self.AmountText.text()
        print( name, age, score)
        self.ResultText.setText("")
        self.ResultMsg.setText("")
        if inputstr == 'Add':
            try:
                record = {'Name': name, 'Age': int(age), 'Score': int(score)}
                scdb += [record]
                self.ResultMsg.setText("Add Complete")
                sortKey = self.KeyBox.currentText()
                self.showScoreDB(scdb, sortKey)
            except IndexError:
                self.ResultMsg.setText("Error : You should input three parses")
            except ValueError:
                self.ResultMsg.setText("Error : Check the Value")
            except:
                self.ResultMsg.setText("Unknown Error")
        elif inputstr == 'Find':
            find_person = []
            try:
                for p in scdb:
                    if p['Name'] == name:
                        find_person += [p]
                    self.ResultText.setText(len(find_person))
                if len(find_person) == 0:
                    self.ResultMsg.setText(name + " is not in this list")
                else:
                    self.showScoreDB(find_person, self.KeyBox.currentText())

            except IndexError:
                self.ResultMsg.setText("Error : You should input one parse")
            except ValueError:
                self.ResultMsg.setText("Error : Check the Value")
            except:
                self.ResultMsg.setText("Unknown Error")
        elif inputstr == 'Inc':
            inc_num = 0
            try:
                for p in scdb:
                    if p['Name'] == name:
                        p['Score'] = str(int(p['Score']) + int(amount))
                        inc_num += 1
                if inc_num == 0:
                    self.ResultMsg.setText(str(name) + " is not in this list")
                else:
                    self.ResultMsg.setText("Increase " + str(inc_num) + "student(s)("+str(name)+") score")
                sortKey = self.KeyBox.currentText()
                self.showScoreDB(scdb, sortKey)
            except IndexError:
                self.ResultMsg.setText("Error : You should input two parses")
            except ValueError:
                self.ResultMsg.setText("Error : Check the Value")
            except:
                self.ResultMsg.setText("Unknown Error")
        elif inputstr == 'Del':
            try:
                del_num = 0
                for p in scdb:
                    if p['Name'] == name:
                        scdb.remove(p)
                        del_num += 1
                if del_num == 0:
                    self.ResultMsg.setText(str(name) + " is not in this list")
                else:
                    self.ResultMsg.setText("Delete " + str(del_num) + "student(s)")
                sortKey = self.KeyBox.currentText()
                self.showScoreDB(scdb, sortKey)

            except IndexError:
                self.ResultMsg.setText("Error : You should input two parse")
            except ValueError:
                self.ResultMsg.setText("Error : Check the Value")
            except:
                self.ResultMsg.setText("Unknown Error")
        elif inputstr == 'Show':
            try:
               sortKey = self.KeyBox.currentText()
               self.showScoreDB(scdb, sortKey)
            except IndexError:
                self.ResultMsg.setText("Error : You don't need more parse")
            except ValueError:
                self.ResultMsg.setText("Error : Check the Value")
            except:
                self.ResultMsg.setText("Unknown Error")
        else:
            self.ResultMsg.setText("Invalid command: " + inputstr)

        self.NameText.setText("")
        self.AgeText.setText("")
        self.ScoreText.setText("")
        self.AmountText.setText("")

    def showScoreDB(self, scdb, keyname):
        result_show = ""
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                result_show += str(attr) + " = " + str(p[attr]) + " \t"
            result_show += " \n"
        self.ResultText.setText(result_show)

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb

# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

if __name__ == '__main__':
    scoredb = readScoreDB()
    writeScoreDB(scoredb)
    app = QApplication(sys.argv)
    ex = AssLayout()
    ex.show()
    sys.exit(app.exec_())