from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    #단어들을 받아온다.
    word = Word()
    guess = Guess(word.randFromDB())

    #생명 갯수를 정해준다.
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:
        display = hangman.get(maxTries - guess.numTries)
        guess.display()

        guessedChar = input("Select a letter : ")
        if len(guessedChar) != 1:
            # 두개 이상의 알파벳을 입력했을 때
            print("One character at a time!")
            continue
        if guessedChar in guess.guessedChars:
            # 알파벳 하나 추측을 성공했을 때
            print("You already guessed " + guessedChar)
            continue
        # guess.guess를 통해 최종 성공 여부를 반환
        finished = guess.guess(guessedChar)

        if finished == True:
            print("Success")
            break

    else:
        # 루프가 다 돌고 완전히 실패했을 경우
        print(hangman.get(0))
        print("Word is "+guess.secretWord)
        print("Guess" + guess.currentStatus)
        print("Fail")

if __name__ == '__main__':
    gameMain()