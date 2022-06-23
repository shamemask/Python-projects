from random import choice
def citizen(number):

    with open('medival_names.txt',encoding='utf-8') as file:
        medival_names = file.read().split()
        
    with open('medival_sirnames.txt',encoding='utf-8') as file:
        medival_sirnames = file.read().split()
    return [ f"{choice(medival_names)} {choice(medival_sirnames)}" for i in range(number)]


# print(citizen(500)) # test