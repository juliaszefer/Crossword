from Crossword.Player import Player
from Person import Person
from Word import Word
from Set import Set
import random

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

        person = Person(encode(nickname), encode(email), encode(password))
        savechanges(path, person.__str__())
        print("account created successfully")
    else:
        for p in users:
            if encode(nickname) == p.nick and encode(email) == p.email and encode(password) == p.password:
                person = Person(decode(nickname), email, password)
                print(f"\nWelcome {nickname}!\n")
                return person
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
    info = v_line.replace("\n", "").split(",")
    a, b, c = info[0], info[1], info[2]
    person1 = Person(a, b, c)
    return person1


def listtostring(strr):
    tmp = ""
    for i in strr:
        tmp += i
    return tmp


def encode(word):
    key1 = "abcdefghijklmnoprstuvwxyz123456789"
    key2 = "0987126543qplaksmznxjdiwuerydtfghu"
    key1list = list(key1)
    key2list = list(key2)
    tochange = list(word)
    for i in range(len(key1list)):
        for j in range(len(tochange)):
            if key1list[i] == tochange[j]:
                tochange[j] = key2list[i]
    word = listtostring(tochange)
    return word


def decode(word):
    key2 = "abcdefghijklmnoprstuvwxyz123456789"
    key1 = "0987126543qplaksmznxjdiwuerydtfghu"
    key1list = list(key1)
    key2list = list(key2)
    tochange = list(word)
    for i in range(len(key1list)):
        for j in range(len(tochange)):
            if key1list[i] == tochange[j]:
                tochange[j] = key2list[i]
    word = listtostring(tochange)
    return word


def savechanges(pathh, persona):
    ffile = open(pathh, 'a')
    ffile.write(f'{persona}\n')


def changeletter(word):
    lista = list(word)
    newlista = list()
    for i in lista:
        newlista.append('_')
    return newlista


def game(player1, player2, odp, sets):
    rand = random.randint(0, 2)
    currset = sets[rand]
    print(f'Your set: {currset.name}\nHave fun :)')
    hiddenlist = list()
    for i in currset.lista:
        hiddenpassword = list()
        tmp = list(i.word)
        for j in tmp:
            hiddenpassword.append(changeletter(j))
        hiddenlist.append(hiddenpassword)
    print("Your crossword: ")
    for i in range(len(hiddenlist)):
        print(f'{i+1}. ', end="")
        for j in range(len(hiddenlist[i])):
            print(f'{hiddenlist[i][j]} ', end="")
        print('')
    print('')
    for i in range(len(currset.lista)):
        print(f'{i+1}. {currset.lista[i].text}, key: {currset.lista[i].key+1}')

    if odp == 1:
        # multiplayer
        print('multi')
    else:
        # singleplayer
        print('single')


szkola1 = Word('plastyka', 3, 'przedmiot artysyczny w szkole')
szkola2 = Word('przerwa', 2, 'inaczej czas wolny miedzy lekcjami')
szkola3 = Word('dziennik', 7, 'nauczyciel zapisuje tam oceny')
szkola4 = Word('dzwonek', 3, 'dzwiek mowiacy o zakonczeniu lekcji')
szkola5 = Word('zeszyt', 1, 'sluzy do zapisywania notatek')
szkola6 = Word('tablica', 6, 'nauczyciel pisze po niej podczas zajec')

set1 = Set('szkola', (szkola1, szkola2, szkola3, szkola4, szkola5, szkola6))

wiosna1 = Word('motyl', 1, 'owad z kolorowymi skrzydlami')
wiosna2 = Word('gesi', 0, 'dzikie ptaki, ktore lataja kluczem')
wiosna3 = Word('ropucha', 0, 'wieksza od zaby')
wiosna4 = Word('bobr', 1, 'buduje tamy na rzekach')
wiosna5 = Word('drzewa', 0 , 'na zime zrzucily liscie, na wiosne znowu zielone')

set2 = Set('wiosna', (wiosna1, wiosna2, wiosna3, wiosna4, wiosna5))

jesien1 = Word('jarzebina', 0, 'czerwone kulki na jesiennych drzewach')
jesien2 = Word('jez', 1, 'ma kolce na grzbiecie')
jesien3 = Word('kasztany', 2, 'brazowe, w kolczastej skorupie, rosna na drzewach')
jesien4 = Word('bocian', 3 , 'dlugonogi ptak, odlatujacy jesienia do cieplych krajow')
jesien5 = Word('liscie', 5, 'zmieniaja kolor na pomaranczowy')
jesien6 = Word('wrzesien', 7, 'miesiac rozpoczecia kalendarzowej jesieni')

set3 = Set('jesien', (jesien1, jesien2, jesien3, jesien4, jesien5, jesien6))

sets = (set1, set2, set3)


persongame = login()
player1 = Player(persongame.nick)
answer = input("Do you want to play...\n1. Single player mode\n2. Multiplayer mode\n")
if answer == 1:
    nick = input("Enter your nickname: ")
    player2 = Player(nick)
    game(player1, player2, 1, sets)
else:
    game(player1, "", 2, sets)
