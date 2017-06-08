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
    message = (str(input('Zadaj text: ')))
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
    os.system('git commit -m '+ '"' + str(message) + '"')
    return()

def push():
    os.system('git push')
    return()
