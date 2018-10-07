import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit, QGridLayout)
import pickle

dbfilename = 'test3_4.dat'


class AssLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #UI 설정 -- Dictionary로 간단하게 해결해보기.....
        NameLabel = QLabel('Name : ', self)
        NameText = QLineEdit()
        AgeLabel = QLabel('Age:',self)
        AgeText = QLineEdit()
        ScoreLabel = QLabel('Score: ', self)
        ScoreText = QLineEdit()
        AmountLabel = QLabel('Amount: ',self)
        AmountText = QLineEdit()
        KeyLabel = QLabel('Key : ',self)
        KeyBox = QComboBox()
        AddButton = QPushButton("Add")
        DelButton = QPushButton("Del")
        FindButton = QPushButton("Find")
        IncButton = QPushButton("Inc")
        ShowButton = QPushButton("Show")
        ResultLabel = QLabel("Result")
        ResultText = QTextEdit()
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QGridLayout.SetFixedSize)

        # 다른 레이아웃 사용
        mainLayout.addWidget(NameLabel, 0, 0, 1, 1)
        mainLayout.addWidget(NameText, 0, 1, 1, 1)
        mainLayout.addWidget(AgeLabel, 0, 2, 1, 1)
        mainLayout.addWidget(AgeText, 0, 3, 1, 1)
        mainLayout.addWidget(ScoreLabel, 0, 4, 1, 1)
        mainLayout.addWidget(ScoreText, 0, 5, 1, 1)
        mainLayout.addWidget(AmountLabel, 0, 6, 1, 1)
        mainLayout.addWidget(AmountText, 0, 7, 1, 1)
        mainLayout.addWidget(KeyLabel, 1, 6, 1, 1)
        mainLayout.addWidget(KeyBox, 1, 7, 1, 1)

        # 버튼 배치 -- 인적사항과 분리해서 레이아웃 사용
        mainLayout.addWidget(AddButton,2,3,1,1)
        mainLayout.addWidget(DelButton,2,4,1,1)
        mainLayout.addWidget(FindButton,2,5,1,1)
        mainLayout.addWidget(IncButton,2,6,1,1)
        mainLayout.addWidget(ShowButton,2,7,1,1)

        # 결과 화면
        ResultLayout = QVBoxLayout()
        ResultLayout.addWidget(ResultLabel)
        ResultLayout.addWidget(ResultText)

        mainLayout.addLayout(ResultLayout,3,0,1,8)
        self.setLayout(mainLayout)
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Assignment6')



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


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]
                print("Add Complete")
            except IndexError:
                print("Error : You should input three parses")
            except ValueError:
                print("Error : Check the Value")
            except:
                print("Unknown Error")
                continue
        elif parse[0] == 'find':
            find_person = []
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        find_person += [p]
                if len(find_person) == 0:
                    print(parse[1] + " is not in this list")
                else:
                    showScoreDB(find_person, 'Name')
            except IndexError:
                print("Error : You should input one parse")
            except ValueError:
                print("Error : Check the Value")
            except:
                print("Unknown Error")
                continue
        elif parse[0] == 'inc':
            inc_num = 0
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score']) + int(parse[2]))
                        inc_num += 1
                if inc_num == 0:
                    print(str(parse[1]) + " is not in this list")
                else:
                    print("Increase " + str(inc_num) + "student(s) score")
            except IndexError:
                print("Error : You should input two parses")
            except ValueError:
                print("Error : Check the Value")
            except:
                print("Unknown Error")
                continue
        elif parse[0] == 'del':
            try:
                del_num = 0
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                        del_num += 1
                if del_num == 0:
                    print(str(parse[1]) + " is not in this list")
                else:
                    print("Delete " + str(del_num) + "student(s)")
            except IndexError:
                print("Error : You should input two parse")
            except ValueError:
                print("Error : Check the Value")
            except:
                print("Unknown Error")
                continue
        elif parse[0] == 'show':
            try:
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except IndexError:
                print("Error : You don't need more parse")
            except ValueError:
                print("Error : Check the Value")
            except:
                print("Unknown Error")
                continue
        elif parse[0] == 'quit':
            try:
                break
            except IndexError:
                print("Error : You don't need more parse")
            except ValueError:
                print("Error : Check the Value")
            except:
                print("Unknown Error")
                continue
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

if __name__ == '__main__':
    scoredb = readScoreDB()
    doScoreDB(scoredb)
    writeScoreDB(scoredb)
    app = QApplication(sys.argv)
    ex = AssLayout()
    ex.show()
    sys.exit(app.exec_())
