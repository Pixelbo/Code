from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()

window.title("A Thing")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)


#def clicked():
#    lbl.configure(text="Button was clicked !!")

def clicked():
    res = "Welcome to " + txt.get()

    lbl.configure(text=res)

    print(combo.get())



btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

window.geometry('500x500')

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")

combo.current(1)  # set the selected item

combo.grid(column=0, row=1)

#chk_state = BooleanVar()
#chk_state.set(True)  # set check state
#or:
#chk_state = IntVar()
#chk_state.set(0)  # uncheck
#chk_state.set(1)  # check
#chk = Checkbutton(window, text='Choose', var=chk_state)
#chk.grid(column=0, row=2)

selected = IntVar()

rad1 = Radiobutton(window, text='First', value=1, variable=selected)

rad2 = Radiobutton(window, text='Second', value=2, variable=selected)

rad3 = Radiobutton(window, text='Third', value=3, variable=selected)


def clickedd():
    print(selected.get())


btnn = Button(window, text="Click Me", command=clickedd)

rad1.grid(column=0, row=3)

rad2.grid(column=1, row=3)

rad3.grid(column=2, row=3)

btnn.grid(column=3, row=0)

spin = Spinbox(window, from_=1, to=100, width=5)

spin.grid(column=0, row=4)

bar = Progressbar(window, length=200)

bar['value'] = 70

bar.grid(column=0, row=5)

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

new_item.add_separator()

new_item.add_command(label='Edit')

menu.add_cascade(label='File', menu=new_item)

new_item.add_command(label='New', command=clickedd)

window.config(menu=menu)

window.mainloop()