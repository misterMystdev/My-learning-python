from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x300")


def showChoice():
    choice1 = language1.get()
    choice2 = language2.get()
    choice3 = language3.get()
    choice4 = language4.get()

    if choice1 == 1:
        Label(text="คุณได้เลือก Python").pack(anchor=W)
    if choice2 == 1:
        Label(text="คุณได้เลือก Javascript").pack(anchor=W)
    if choice3 == 1:
        Label(text="คุณได้เลือก PHP").pack(anchor=W)
    if choice4 == 1:
        Label(text="คุณได้เลือก C#").pack(anchor=W)

language1 = IntVar()
Checkbutton(text="Python",variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="Javascript",variable=language2).pack(anchor=W)
language3 = IntVar()
Checkbutton(text="PHP",variable=language3).pack(anchor=W)
language4 = IntVar()
Checkbutton(text="C#",variable=language4).pack(anchor=W)

Button(text="แสดงตัวเลือก",command=showChoice).pack(anchor=W)

root.mainloop()