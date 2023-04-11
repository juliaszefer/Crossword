class Person:
    def __init__(self, nick, email, password):
        self.nick = self.encode(nick)
        self.email = self.encode(email)
        self.password = self.encode(password)

    def getnick(self):
        return self.nick

    def __str__(self):
        return f"{self.nick},{self.email},{self.password}"

    @staticmethod
    def listtostring(strr):
        tmp = ""
        for i in strr:
            tmp += i
        return tmp

    def encode(self, word):
        key1 = "abcdefghijklmnoprstuvwxyz123456789"
        key2 = "0987126543qplaksmznxjdiwuerydtfghu"
        key1list = list(key1)
        key2list = list(key2)
        tochange = list(word)
        for i in range(len(key1list)):
            for j in range(len(tochange)):
                if key1list[i] == tochange[j]:
                    tochange[j] = key2list[i]
        word = self.listtostring(tochange)
        return word

    def decode(self, word):
        key1 = "abcdefghijklmnoprstuvwxyz123456789"
        key2 = "0987126543qplaksmznxjdiwuerydtfghu"
        key1list = list(key1)
        key2list = list(key2)
        tochange = list(word)
        for i in range(len(key2list)):
            for j in range(len(tochange)):
                if key2list[i] == tochange[j]:
                    tochange[j] = key1list[i]
        word = self.listtostring(tochange)
        return word
