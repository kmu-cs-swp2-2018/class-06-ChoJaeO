class Guess:
    def __init__(self,word):
        self.guess_list = []
        self.answer = word
        self.numTries = 0
        self.guessedChars = ""
        for i in range(len(word)):
            self.guess_list.append(0)

    def display(self):

        pass

    def guess(self,character):
        self.guessedChars += character
        for i in range(len(self.answer)):
            if character == self.answer[i]:
                self.guess_list[i] = 1
        print("Current : " , end ='')
        for i in range(len(self.answer)):
            if self.guess_list[i] == 1:
                print(self.answer[i], end ='')
            else:
                print("_", end = '')
        print()

        if 0 not in self.guess_list:
            return True
        else:
            return False
