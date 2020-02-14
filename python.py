
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
window.geometry("790x250+450+100")   # Size of the window
window.resizable(0,0)                # Use this to stop the window from being resizeable when you run the program
# Main Window




table = Frame(window)
table.place(x = 310, y = 7)

tbl = ttk.Treeview(table,  columns = (1,2,3,4,5), selectmode = "extended",height = "10", show = "headings")
tbl.pack(expand= YES, fill = BOTH)

tbl.heading(1, text = "ID")
tbl.column(1, minwidth = 0,width = 40, stretch = NO, anchor = 'center')
tbl.heading(2, text = "Name")
tbl.column(2, minwidth = 0,width = 120, stretch = NO, anchor = 'center')
tbl.heading(3, text = "Description")
tbl.column(3, minwidth = 0,width = 150, stretch = NO, anchor = 'center')
tbl.heading(4, text = "Size")
tbl.column(4, minwidth = 0,width = 80, stretch = NO, anchor = 'center')
tbl.heading(5, text = "Price")
tbl.column(5, minwidth = 0,width = 80, stretch = NO, anchor = 'center')
# Table



productInfo  = Label(window, text = "Product Information ") .grid(row = 1, column = 0, padx = 15, pady = 10, sticky=W)
productID    = Label(window, text = "Product Name ")        .grid(row = 2, column = 0, padx = 15, pady = 10, sticky=W)
productDesc  = Label(window, text = "Product Description ") .grid(row = 3, column = 0, padx = 15, pady = 10, sticky=W)
productSize  = Label(window, text = "Product Size ")        .grid(row = 4, column = 0, padx = 15, pady = 10, sticky=W)
productPrice = Label(window, text = "Product Price ")       .grid(row = 5, column = 0, padx = 15, pady = 10, sticky=W)
# Labels


Name        = Text (window,height = 1, width = 18)  .grid(row = 2, column = 1, columnspan =2)
Description = Text (window,height = 1, width = 18)  .grid(row = 3, column = 1, columnspan =2)
ID          = Text (window,height = 1, width = 18)  .grid(row = 4, column = 1, columnspan =2)
Size        = Text (window,height = 1, width = 18)  .grid(row = 5, column = 1, columnspan =2)
# Textboxes


add     = Button(window, text = 'Add Product', fg = 'brown', height = 1, width = 12, command = Add) .place(x=17, y=207)
#read   = Button(window, text = 'Read'  , fg = 'brown', height = 1, width = 6).place(x=90, y= 175)
update  = Button(window, text = 'Update Product', fg = 'brown', height = 1, width = 12)             .place(x= 114, y=207)
delete = Button(window, text = 'Delete Product', fg = 'brown', height = 1, width = 12).place(x=210, y=207)                                                                                   
# Buttons





mainloop()
# End of Code







# import time
# variable name = time.strtime('%I:%m:%p')


