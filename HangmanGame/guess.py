class Guess:
    def __init__(self,word):
        self.guess_list = []
        self.currentStatus = ""
        self.answer = word
        self.numTries = 0
        self.guessedChars = ""
        for i in word:
            self.guess_list.append(0)

    def display(self):
        print("Tries : " + str(self.numTries))
        print("You already guessed " + self.guessedChars)
        pass

    def guess(self,character):

        self.guessedChars += character
        if character not in self.answer:
            self.numTries += 1
        else:
            print("Current : " , end ='')
            self.currentStatus = ""
            for i in range(len(self.answer)):
                if character == self.answer[i]:
                    self.guess_list[i] = 1
                self.currentStatus = self.answer[i] if self.guess_list[i] == 1 else "_"
            print (self.currentStatus)
        return self.guess_list

    def getnumTries(self):
        return self.numTries

    def getcurrentStatus(self):
        return self.currentStatus

    def getguessedChars(self):
        return self.guessedChars

    def getanswer(self):
        return answer
