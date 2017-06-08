#from subprocess import call
import os
import json

def open_json(data_f='conf.json'): #open json config file
    with open(data_f) as data_file:
        data = json.load(data_file)
    return(data)

def cd(data):   #change directory according to config file
    #call(['cd',path])
    path = data['config']['patch']
    os.system('cd '+ path)
    return()

def mess(): #set message for commit
    message = (str(input('Zadaj text: ')))
    return message

def init(): #inicialize git folder
    #call(['git','init'])
    os.system('git init')
    return()

def add():  #add all from folder to git
    #call(['git','add','.'])
    os.system('git add .')
    return()

def config(data):   #config for git according to config file
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

def commit(message):    #commit folder to git
    #cal(['git','commit','-m',message])
    os.system('git commit -m '+ '"' + str(message) + '"')
    return()

def push(): #upload folder to git repository
    os.system('git push')
    return()
