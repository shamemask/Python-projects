import os

path = os.getcwd() 
print('Enter path and file:')
while True:
    try:
        line = input()
    except EOFError:
        break
    print("mkdir \""+path+"\\".join(line.split("/")[:-1])+"\"")
    os.system("mkdir \""+path+"\\".join(line.split("/")[:-1])+"\"")
    print("echo > \""+path+"\\".join(line.split("/")))
    os.system("echo  > \""+path+"\\".join(line.split("/"))+"\"")