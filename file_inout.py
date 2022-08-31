from tkinter import N


def space():
    return '\n'

f = open("새파일.txt", 'a')
for line in range(5):
    text=input()
    f.write(text)
    f.write(space())
       


f.close()


