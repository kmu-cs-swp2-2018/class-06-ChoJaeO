import random

class Word:
    def __init__(self,minlength):
        self.word_list = []
        self.count = 0
        # 파일 입력
        f = open("words.txt")
        words = f.readlines()
        f.close()
        for word in words:
            # 빈칸 제거 작업
            word_one = word.rstrip()
            if len(word_one) >= minlength:
                self.word_list.append(word_one)
                self.count += 1

    def readFromDB(self):
        # 단어 하나 난수생성을 통해 선택
        r = random.randrange(len(self.word_list))
        # 단어 리턴
        return self.word_list[r]
