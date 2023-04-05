from Person import Person

path = "data/logins.txt"


def login():
    odp = input("Do you want to\n1. sign in\n2. log in")
    users = readfile(path)
    if int(odp) == 1:
        nickname, email, password = input("Enter your nickname: "), input("Enter your e-mail: "),\
                                    input("Enter your password: ")
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
