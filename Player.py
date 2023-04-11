from datetime import date


class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.score = 0
        self.today = date.today()

    def setscore(self, newscore):
        self.score = newscore

    def __str__(self):
        return f"{self.today}\t{self.nickname}: {self.score} points"
