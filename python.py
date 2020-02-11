from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox


def Add():
    Name = Entry(window)
    ID   = Entry(window)

    Size = Entry(window)

    if Name == "" or ID == "" or Size == "":
        MessageBox.showerror ("Error!", "Fill up all the forms.")
    else:
        MessageBox.showerror ("Error", "BOBO!")





window = Tk()
window.title("BoJack Clothing Line") # Title of the Window
window.geometry("800x500+450+100")   # Size of the window
window.resizable(0,0)                # Use this to stop the window from being resizeable when you run the program
# Main Window



productInfo  = Label(window, text = "Product Information ") .grid(row = 1, column = 0, padx = 15,   pady = 10,          sticky=W)
productID    = Label(window, text = "Product ID ")          .grid(row = 2, column = 0, padx = 15, pady = 10, sticky=W)
productDesc  = Label(window, text = "Product Description ") .grid(row = 3, column = 0, padx = 15, pady = 10, sticky=W)
productSize  = Label(window, text = "Product Size ")        .grid(row = 4, column = 0, padx = 15, pady = 10, sticky=W)
productPrice = Label(window, text = "Product Price ")       .grid(row = 5, column = 0, padx = 15, pady = 10, sticky=W)
# Labels


Name        = Text (window,height = 1, width = 50)  .grid(row = 2, column = 1, columnspan =2)
Description = Text (window,height = 1, width = 50)  .grid(row = 3, column = 1, columnspan =2)
ID          = Text (window,height = 1, width = 50)  .grid(row = 4, column = 1, columnspan =2)
Size        = Text (window,height = 1, width = 50)  .grid(row = 5, column = 1, columnspan =2)
# Textboxes


add     = Button(window, text = 'Add Product', fg = 'brown', height = 1, width = 15, command = Add) .place(x=435, y=205)
#read   = Button(window, text = 'Read'  , fg = 'brown', height = 1, width = 6).place(x=90, y= 175)
update  = Button(window, text = 'Update Product', fg = 'brown', height = 1, width = 15)             .place(x=145, y=205)
#delete = Button(window, text = 'Delete', fg = 'brown', height = 1, width = 6).place(x=210, y=175)                                                                                   
# Buttons



listView()
# List View






mainloop()
# End of Code







# import time
# variable name = time.strtime('%I:%m:%p')


