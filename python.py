from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox


def Add():
    Name = eName.get()
    ID   = eID.get()
    Size = eSize.get()
    if Name == "" or ID == "" or Size == "":
        MessageBox.showerror ("Error!", "Fill up all the forms.")
    else:
        MessageBox.showerror ("Error!", "BOBO!.")
    

window = Tk().geometry("800x500+450+100")
# Main Window


productInfo  = Label(window, text = "Product Information ").grid(row = 0, column = 0, padx = 30,sticky=W)
productID    = Label(window, text = "Product ID ").grid(row = 1, column = 0, padx = 30, pady = 15, sticky=W)
productPrice = Label(window, text = "Product Price ").grid(row = 2, column = 0, padx = 30, pady = 15, sticky=W)
productSize  = Label(window, text = "Product Size ").grid(row = 3, column = 0, padx = 30, pady = 15, sticky=W)
# Labels


Name = Text (window,height = 1, width = 10).grid(row = 1, column = 1, columnspan =2)
ID   = Text (window,height = 1, width = 10).grid(row = 2, column = 1, columnspan =2)
Size = Text (window,height = 1, width = 10).grid(row = 3, column = 1, columnspan =2)
# Textboxes


create = Button(window, text = 'Create', fg = 'brown', height = 1, width = 6, command = Add).place(x=30, y=175)
read   = Button(window, text = 'Read'  , fg = 'brown', height = 1, width = 6).place(x=90, y= 175)
update = Button(window, text = 'Update', fg = 'brown', height = 1, width = 6).place(x=150, y=175)
delete = Button(window, text = 'Delete', fg = 'brown', height = 1, width = 6).place(x=210, y=175)                                                                                   
# Buttons

mainloop()
# End of Code

