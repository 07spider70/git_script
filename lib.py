#from subprocess import call
import os
import json

def open_json(data_f='conf.json'):
    with open(data_f) as data_file:
        data = json.load(data_file)
    return(data)

def cd(data):
    #call(['cd',path])
    path = data['config']['patch']
    os.system('cd '+ path)
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

def config(data):
    #data = open_json()
    name = "'"+ data['config']['name'] +"'"
    email = data['config']['email']
    #call(['git','config','--local','config.name',name])
    #call(['git','config','--local','config.email',email])
    os.system('git config --local config.name '+name)
    os.system('git config --local config.email '+email)
    print('Added ' + name)
    print('Added ' + email)
    return()

def commit(message):
    #cal(['git','commit','-m',message])
    os.system('git commit -m '+ '"' + str(message) + '"')
    return()

def push():
    os.system('git push')
    return()
