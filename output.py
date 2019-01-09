from body import KontrolFlow
from head import assign
from tkinter import *

window = Tk()
window.title("Output Console")
window.iconbitmap('config/icon.ico')
window.configure(background = "black")
for i in range(len(KontrolFlow)):
    if KontrolFlow[i][0] == assign["print_call"]:
        Label (window, text="» {}".format(KontrolFlow[i][2]), bg="black", fg="white", font="none 12 bold").grid(row=1+i, column = 0, sticky=W)


window.mainloop()
