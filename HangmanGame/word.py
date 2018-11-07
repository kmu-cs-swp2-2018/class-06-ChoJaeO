import random

class Word:
    def __init__(self):
        self.word_list = []
        # 파일 입력
        f = open("words.txt")
        words = f.readlines()
        f.close()
        for word in words:
            # 빈칸 제거 작업
            self.word_list.append(word.rstrip())

    def readFromDB(self):
        # 단어 하나 난수생성을 통해 선택
        r = random.randrange(len(self.word_list))
        # 단어 리턴
        return self.word_list[r]
