from Crossword.Player import Player
from Person import Person

path = "data/logins.txt"


def login():
    odp = input("Do you want to\n1. sign in\n2. log in")
    users = readfile(path)
    person = ""
    nickname, email, password = input("Enter your nickname: "), input("Enter your e-mail: "), \
        input("Enter your password: ")
    if int(odp) == 1:
        for p in users:
            czygit = True
            while czygit:
                if nickname == p.nick:
                    print("Nickname already exists, try again.")
                    nickname = input("Enter your nickname: ")
                else:
                    czygit = False
            czygit = True
            while czygit:
                if email == p.email:
                    print("Email already exists, try again.")
                    email = input("Enter your e-mail: ")
                else:
                    czygit = False

        person = Person(nickname, email, password)
        savechanges(path, person)
        print("account created successfully")
    else:
        for p in users:
            if nickname == p.decode(p.nick) and email == p.decode(p.email) and password == p.decode(p.password):
                person = Person(nickname, email, password)
                print(f"Welcome {nickname}!")
            else:
                print("Wrong login or password")
                login()
    return person


def readfile(pathh):
    arr = list()
    ffile = open(pathh, 'r')
    for line in ffile:
        arr.append(sortline(line))
    return arr


def sortline(v_line):
    info = v_line.split(",")
    a, b, c = info[0], info[1], info[2]
    person1 = Person(a, b, c)
    return person1


def savechanges(pathh, persona):
    ffile = open(pathh, 'a')
    ffile.write(persona)


def game(player1, player2, odp):
    print("gra")


persongame = login()
player1 = Player(persongame.getnick())
answer = input("Do you want to play...\n1.Single player mode\n2.Multiplayer mode")
if answer == 1:
    nick = input("Enter your nickname: ")
    player2 = Player(nick)
    game(player1, player2, True)
else:
    game(player1, "", False)
