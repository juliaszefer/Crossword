import datetime


class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.score = 0
        self.date = datetime.date

    def setscore(self, newscore):
        self.score = newscore

    def __str__(self):
        return f"{self.date}\t{self.nickname}: {self.score} points"