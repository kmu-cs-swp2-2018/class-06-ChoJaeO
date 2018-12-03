from hangman import Hangman
from guess import Guess
from word import Word

from PyQt5.QtWidgets import (QApplication, QWidget, QLayout, QGridLayout, QTextEdit, QLineEdit, QToolButton)
import sys

class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.word = Word()

        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        #self.hangmanWindow.setAlignment(Qt.AlignLeft)

        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        statusWindow = QGridLayout()

        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        font = self.currentWord.font()
        font.setPointSize((font.pointSize() + 8))
        self.currentWord.setFont(font)
        statusWindow.addWidget(self.currentWord, 0, 0, 1, 2)

        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        #self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)      # 알파벳 갯수가 26개이므로
        statusWindow.addWidget(self.guessedChars, 1, 0, 1, 2)

        self.status_message = QLineEdit()
        self.status_message.setReadOnly(True)
        #self.status_message.setAlignment(Qt.AlignLeft)
        self.status_message.setMaxLength(52)
        statusWindow.addWidget(self.status_message, 2, 0, 1, 2)

        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusWindow.addWidget(self.charInput,  3, 0)

        self.guessButton = QToolButton()
        self.guessButton.setText('Guess')
        self.guessButton.clicked.connect(self.gameMain)
        statusWindow.addWidget(self.guessButton, 3, 1)

        self.newgameButton = QToolButton()
        self.newgameButton.setText("new Game")
        self.newgameButton.clicked.connect(self.RestartGame)
        statusWindow.addWidget(self.newgameButton, 4, 0)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout,0 ,0)
        mainLayout.addLayout(statusWindow,0 , 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hangman")

        self.RestartGame()

    def RestartGame(self):
        self.hangman = Hangman()
        self.answer = "core"
        self.guess = Guess("core") #self.word.readFromDB()
        self.currentWord.setText("_ " * len(self.answer))
        self.status_message.setText("Game Start!")
        self.hangmanWindow.setText(self.hangman.get(0))
        self.guessedChars.clear()
        self.charInput.clear()
        self.guess = Guess(self.answer)
        self.guessButton.setEnabled(True)
        self.newgameButton.setEnabled(False)

    def gameMain(self):

        guessedChar = self.charInput.text()
        self.status_message.clear()
        self.guessedChars.clear()
        self.charInput.clear()

        guess = Guess(word.readFromDB())

        #생명 갯수를 정해준다.
        hangman = Hangman()
        maxTries = hangman.getLife()
        print("Current : " + "_ "*len(guess))
        self.currentWord.setText("_"*len(guess))

        display = hangman.get(maxTries - self.guess.getnumTries())
        print(display)
        self.hangmanWindow.setText(display)
        self.guess.display()

        #guessedChar = input("Select a letter : ")
        guessedChar = guessedChar.lower()
        print("-------------------------------")
        self.guessedChars.setText(self.guess.getguessedChars())
        if guessedChar in self.guess.getguessedChars():
            # 알파벳이 이미 추측한 것일 때
            self.status_message.setText("You already guessed " + guessedChar)
            print("You already guessed " + guessedChar)
            # guess.guess를 통해 최종 성공 여부를 반환
        finished = self.guess.guess(guessedChar)
        guessingword = self.answer[i] if self.guess_list[i] == 1 else "_"
        self.currentWord.setText(guessingword)
        if maxTries > self.guess.getnumTries() and 0 not in finished:
            print("Success")
            self.status_message.setText("Success")
            self.guessButton.setEnabled(False)
            self.newgameButton.setEnabled(True)
        elif maxTries < self.guess.getnumTries() and 0 in finished:
            # 루프가 다 돌고 완전히 실패했을 경우
            print(hangman.get(0))
            print("Word is "+self.guess.getanswer())
            self.status_message.setText("Word is "+self.guess.getanswer())
            print("Guess : " + self.guess.getcurrentStatus())
            print("Fail")
            self.guessButton.setEnabled(False)
            self.newgameButton.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())
