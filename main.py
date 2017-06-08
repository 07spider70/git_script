from lib import *

path1 = "C:\Users\Janci\Desktop\python\project_1"

data = open_json()


def main():
    #path1=path()
    cd(data)
    print """
            Stlac 1 pre init,
            stlac 2 pre config,
            stlac 3 pre add,
            stlac 4 pre commit,
            stlac 5 pre push,
            stlac 6 pre add, commit, push.
            """
    case = int(input('Cislo: '))
    if case == 1:
        init()
    elif case == 2:
        config(data)
    elif case == 3:
        add()
    elif case == 4:
        mes = mess()
        commit(mes)
    elif case == 5:
        push()
    elif case ==6:
        add()
        mes = mess()
        commit(mes)
        push()

if __name__ == '__main__':
    main()
