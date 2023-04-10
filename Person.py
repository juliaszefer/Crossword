class Person:
    def __init__(self, nick, email, password):
        self.nick = self.encode(nick)
        self.email = self.encode(email)
        self.password = self.encode(password)
        self.key1 = "abcdefghijklmnoprstuvwxyz123456789"
        self.key2 = "0987126543qplaksmznxjdiwuerydtfghu"
        self.key1list = list(self.key1)
        self.key2list = list(self.key2)

    def getnick(self):
        return self.nick

    def __str__(self):
        return f"{self.nick},{self.email},{self.password}"

    def listtostring(self, strr):
        tmp = ""
        for i in strr:
            tmp += i
        return tmp

    def encode(self, word):
        tochange = list(word)
        for i in range(len(self.key1list)):
            for j in range(len(tochange)):
                if self.key1list[i] == tochange[j]:
                    tochange[j] = self.key2list[i]
        word = self.listtostring(tochange)
        return word

    def decode(self, word):
        tochange = list(word)
        for i in range(len(self.key2list)):
            for j in range(len(tochange)):
                if self.key2list[i] == tochange[j]:
                    tochange[j] = self.key1list[i]
        word = self.listtostring(tochange)
        return word


