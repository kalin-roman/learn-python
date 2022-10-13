    
from tkinter import E


def without():
    f = open('input.txt','r')
    s = f.readline()
    while s != '':
        print(s.rstrip())
        s = f.readline()
    f.close()

def print_file():
    with open('input.txt') as f:
        for s in f:
            print("line: ",s.rstrip(),"")


e = input("Enter the string: ")

with open('input.txt', "a") as f:
    f.write("\n" + e)
print_file()
