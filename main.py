from subprocess import call
import os

def path():
    path = str(input('Zadajte cestu k suboru: '))
    return(path)

def cd(path):
    #call(['cd',path])
    os.system('cd '+path)
    return()

def mess():
    message = str(input('Zadaj text. '))
    return message

def init():
    #call(['git','init'])
    os.system('git init')
    return()

def add():
    #call(['git','add','.'])
    os.system('git add .')
    return()

def config(name,email):
    name = "'"+str(name)+"'"
    email = str(email)
    #call(['git','config','--local','config.name',name])
    #call(['git','config','--local','config.email',email])
    os.system('git config --local config.name '+name)
    os.system('git config --local config.email '+email)
    return()

def commit(message):
    #cal(['git','commit','-m',message])
    os.system('git commit -m '+ message)
    return()

def main():
    path1=path()
    cd(path1)
    print """
            Stlac 1 pre init,
            stlac 2 pre config,
            stlac 3 pre add,
            stlac 4 pre commit,
            stlac 5 pre add,commit.
            """
    case = int(input('Cislo: '))
    if case == 1:
        init()
    elif case == 2:
        name = str(input('Meno: '))
        email = str(input('Email: '))
        config(name,email)
    elif case == 3:
        add()
    elif case == 4:
        mes = mess()
        commit(mes)
    elif case ==5:
        add()
        mes = mess()
        commit(mes)

if __name__ == '__main__':
    main()
