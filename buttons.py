import ujson
import os

def get_index(big_list, value):
    keys = [sublist[0] for sublist in big_list]
    if value in keys:
        return keys.index(value)
    else:
        return -1

def get_remotes():
    remotes=[]
    if 'remotes.p' in os.listdir():
        with open('remotes.p', 'r') as rf:
            remotes=ujson.load(rf)
    return remotes

def new_remote(name):
    remotes=[]
    if 'remotes.p' in os.listdir():
        with open('remotes.p', 'r') as rf:
            remotes=ujson.load(rf)
    if name in remotes:
        return(-1)
    remotes.append(name)
    with open('remotes.p', 'w') as rf:
        ujson.dump(remotes, rf)
    with open(f'{name}.p', 'w') as rf:
        ujson.dump([], rf)
    return(1)

def remove_remote(name):
    remotes=[]
    if 'remotes.p' in os.listdir():
        with open('remotes.p', 'r') as rf:
            remotes=ujson.load(rf)
    if name in remotes:
        remotes.remove(name)
    with open('remotes.p', 'w') as rf:
        ujson.dump(remotes, rf)
    os.remove(f'{name}.p')
    return(1)

def get_buttons(name):
    buttons=[]
    if f'{name}.p' in os.listdir():
        with open(f'{name}.p', 'r') as rf:
            buttons=ujson.load(rf)
    return buttons

def get_button(remote,button):
    buttons=[]
    if f'{remote}.p' in os.listdir():
        with open(f'{remote}.p', 'r') as rf:
            buttons=ujson.load(rf)
    index = get_index(buttons,button)
    if(index==-1):
        return -1
    print(buttons[index][1])
    return buttons[index][1]

def edit_button(r_name,b_name,b_vals):
    buttons=[]
    if f'{r_name}.p' in os.listdir():
        with open(f'{r_name}.p', 'r') as rf:
            buttons=ujson.load(rf)
    index=get_index(buttons,b_name)
    if(index==-1):
        buttons.append([b_name,b_vals])
    else:
        buttons[index][1]=b_vals
    with open(f'{r_name}.p', 'w') as rf:
        ujson.dump(buttons, rf)

def remove_button(r_name,b_name):
    buttons=[]
    if f'{r_name}.p' in os.listdir():
        with open(f'{r_name}.p', 'r') as rf:
            buttons=ujson.load(rf)
    index=get_index(buttons,b_name)
    if(index!=-1):
        del buttons[index]
    with open(f'{r_name}.p', 'w') as rf:
        ujson.dump(buttons, rf)