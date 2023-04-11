class Person:
    def __init__(self, nick, email, password):
        self.nick = nick
        self.email = email
        self.password = password

    def getnick(self):
        return self.nick

    def __str__(self):
        return f"{self.nick},{self.email},{self.password}"
