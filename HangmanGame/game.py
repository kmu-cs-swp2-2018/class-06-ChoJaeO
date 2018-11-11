from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    #단어들을 받아온다.
    word = Word()
    guess = Guess(word.readFromDB())

    #생명 갯수를 정해준다.
    hangman = Hangman()
    maxTries = hangman.getLife()

    try_cnt = 0

    while guess.numTries < maxTries:
        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()
        guessedChar = input("Select a letter : ")
        print("-------------------------------")
        if len(guessedChar) != 1:
            # 두개 이상의 알파벳을 입력했을 때
            print("One character at a time!")
            continue
        if guessedChar in guess.guessedChars:
            # 알파벳이 이미 추측한 것일 때
            print("You already guessed " + guessedChar)
            continue
        # guess.guess를 통해 최종 성공 여부를 반환
        finished = guess.guess(guessedChar)
        try_cnt += 1
        print("Tries : " + str(guess.numTries))
        if finished == True:
            break

    print("-------------------------------")
    if maxTries > guess.numTries:
        print("Success")

    else:
        # 루프가 다 돌고 완전히 실패했을 경우
        print(hangman.get(0))
        print("Word is "+guess.answer)
        print("Guess : " + guess.currentStatus)
        print("Fail")

if __name__ == '__main__':
    gameMain()