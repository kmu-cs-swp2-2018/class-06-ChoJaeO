class Guess:
    def __init__(self,word):
        self.guess_list = []
        self.currentStatus = ""
        self.answer = word
        self.numTries = 0
        self.guessedChars = ""
        for i in range(len(word)):
            self.guess_list.append(0)

    def display(self):
        print("Tries : " + str(self.numTries))
        print("You already guessed " + self.guessedChars)
        pass

    def guess(self,character):
        self.guessedChars += character
        for i in range(len(self.answer)):
            if character == self.answer[i]:
                self.guess_list[i] = 1
        print("Current : " , end ='')
        self.currentStatus = ""
        if character not in self.answer:
            self.numTries += 1
        for i in range(len(self.answer)):
            if self.guess_list[i] == 1:
                self.currentStatus += self.answer[i] + " "
                print(self.answer[i], end =' ')
            else:
                self.currentStatus += "_ "
                print("_", end = ' ')
        print()
        if 0 not in self.guess_list:
            return True
        else:
            return False
