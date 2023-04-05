from Person import Person


def login():
    odp = input("Do you want to\n1. sign in\n2. log in")
    if int(odp) == 1:
        nickname, email, password = input("Enter your nickname: "), input("Enter your e-mail: "),\
                                    input("Enter your password: ")


def readfile(path):
    arr = list()
    ffile = open(path, 'r')
    for line in ffile:
        arr.append(sortline(line))
    return arr


def sortline(v_line):
    info = v_line.split(",")
    a, b, c = info[0], info[1], info[2]
    person1 = Person(a, b, c)
    return person1

def savechanges(path, persona):
    ffile = open(path, 'w')
    ffile.append(persona)
