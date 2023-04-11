from Player import Player
from Person import Person
from Word import Word
from Set import Set
import random
import os

path = "data/logins.txt"
leaderboard = "Leaderboards/"


def addtoleaderboard(players):
    if not os.path.exists(os.path.join(leaderboard, f'{players[0].nickname}.txt')):
        with open(os.path.join(leaderboard, f'{players[0].nickname}.txt'), 'w') as f:
            for i in range(len(players)):
                f.write(f'{players[i].__str__()}\t')
            f.write('\n')
    else:
        stringpath = leaderboard+players[0].nickname+'.txt'
        ffile = open(stringpath, 'a')
        for i in range(len(players)):
            ffile.write(f'{players[i].__str__()}\t')
        ffile.write('\n')


def login():
    odp = input("Do you want to...\n1. sign in\n2. log in\n")
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


def play(player, hiddenlist, currlist, currset):
    print(f'\nnow playing {player.nickname}...\n')
    odp = input("Which password would you like to guess? (number of the chosen one)")
    for i in range(len(currlist)):
        if int(odp)-1 == i:
            password = input("Enter your guess: ")
            if password == currlist[i].word:
                tmp = list(currlist[i].word)
                hiddenlist[i] = tmp
                player.setscore(player.score+len(tmp))
                print(f"Congrats! You've earned {len(tmp)} points!")
                anws = input("Would you like to guess the main password? (y/n)")
                if anws == 'y':
                    check = input("Enter your guess: ")
                    if check == currset.password:
                        counter = 0
                        for j in range(len(currlist)):
                            temp = list(currlist[j].word)
                            if temp != hiddenlist[j]:
                                counter += 1
                        player.setscore(player.score*counter)
                        print(f"\nplayer {player.nickname} won with: {player.score} points.\n")
                        return 'exit'
                    else:
                        print("wrong guess :(")
            else:
                tmp = list(currlist[i].word)
                player.setscore(player.score-len(tmp))
                print(f"What a shame! You've just lost {len(tmp)} points!")

    return hiddenlist


def writespace(howmany):
    for i in range(howmany):
        print('  ', end="")


def write(player1, player2, hiddenlist, currset, odp):
    print(f'\nplayer1: {player1.nickname}, points: {player1.score}')
    if odp == 1:
        print(f'player2: {player2.nickname}, points: {player2.score}\n')

    for i in range(len(hiddenlist)):
        print(f'{i+1}. ', end="")
        writespace(8-currset.lista[i].key+1)
        for j in range(len(hiddenlist[i])):
            if currset.lista[i].key == j:
                print(f'[{hiddenlist[i][j]}] ', end="")
            else:
                print(f'{hiddenlist[i][j]} ', end="")
        print('')
    print('')
    for i in range(len(currset.lista)):
        print(f'{i+1}. {currset.lista[i].text}')


def game(player1, player2, odp, sets):
    rand = random.randint(0, 2)
    currset = sets[rand]
    print(f'Your set: {currset.name}\nHave fun :)\n')
    hiddenlist = list()
    for i in currset.lista:
        hiddenpassword = list()
        tmp = list(i.word)
        for j in range(len(tmp)):
            hiddenpassword.append("_")
        hiddenlist.append(hiddenpassword)
    print("Your crossword: \n")
    currlist = currset.lista
    if odp == 1:
        decision = random.randint(0, 1)
        while hiddenlist != 'exit':
            write(player1, player2, hiddenlist, currset, odp)
            if decision % 2 == 0:
                hiddenlist = play(player1, hiddenlist, currlist, currset)
            else:
                hiddenlist = play(player2, hiddenlist, currlist, currset)
            decision += 1
        players = list()
        players.append(player1)
        players.append(player2)
        addtoleaderboard(players)
    else:
        while hiddenlist != 'exit':
            write(player1, player2, hiddenlist, currset, odp)
            hiddenlist = play(player1, hiddenlist, currlist, currset)
        players = list()
        players.append(player1)
        addtoleaderboard(players)


szkola1 = Word('plastyka', 3, 'przedmiot artysyczny w szkole')
szkola2 = Word('przerwa', 2, 'inaczej czas wolny miedzy lekcjami')
szkola3 = Word('dziennik', 7, 'nauczyciel zapisuje tam oceny')
szkola4 = Word('dzwonek', 3, 'dzwiek mowiacy o zakonczeniu lekcji')
szkola5 = Word('olowek', 1, 'sluzy do zapisywania notatek')
szkola6 = Word('tablica', 6, 'nauczyciel pisze po niej podczas zajec')

set1 = Set('szkola', (szkola1, szkola2, szkola3, szkola4, szkola5, szkola6), 'szkola')

wiosna1 = Word('motyl', 1, 'owad z kolorowymi skrzydlami')
wiosna2 = Word('gesi', 0, 'dzikie ptaki, ktore lataja kluczem')
wiosna3 = Word('ropucha', 0, 'wieksza od zaby')
wiosna4 = Word('bobr', 1, 'buduje tamy na rzekach')
wiosna5 = Word('drzewa', 0, 'na zime zrzucily liscie, na wiosne znowu zielone')

set2 = Set('wiosna', (wiosna1, wiosna2, wiosna3, wiosna4, wiosna5), 'ogrod')

jesien1 = Word('jarzebina', 0, 'czerwone kulki na jesiennych drzewach')
jesien2 = Word('jez', 1, 'ma kolce na grzbiecie')
jesien3 = Word('kasztany', 2, 'brazowe, w kolczastej skorupie, rosna na drzewach')
jesien4 = Word('bocian', 3, 'dlugonogi ptak, odlatujacy jesienia do cieplych krajow')
jesien5 = Word('liscie', 5, 'zmieniaja kolor na pomaranczowy')
jesien6 = Word('wrzesien', 7, 'miesiac rozpoczecia kalendarzowej jesieni')

set3 = Set('jesien', (jesien1, jesien2, jesien3, jesien4, jesien5, jesien6), 'jesien')

sets = (set1, set2, set3)

# main code
persongame = login()
player1 = Player(persongame.nick)
czyKoniec = True
while czyKoniec:
    answer = input("Do you want to play...\n1. Single player mode\n2. Multiplayer mode\n")
    if int(answer) == 2:
        nick = input("Enter your nickname: ")
        player2 = Player(nick)
        game(player1, player2, 1, sets)
    else:
        game(player1, "", 2, sets)
    odpow = input("Would you like to play again? (y/n)")
    if odpow == 'n':
        czyKoniec = False
print("\nThank you for playing!")
