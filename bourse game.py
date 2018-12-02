from iexfinance.stocks import Stock
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *
import time
from tkinter import messagebox
from tkinter import Menu

pricetable = []
timetable = []
opentable = []
money = float(1000)
companies = ["TSLA", "AAPL", "GOOGL", "MSFT", "INTC", "AMZN", "FB", "BABA", "ATVI", "ADBE"]
stocks = Stock(companies)
selllist = []

def actualisemoney():
    trs = "Money: " + str(round(money))
    moneylbl.configure(text=trs)

def actualiseactions():
    trs = "Actions: " + str(selllist)
    actionlbl.configure(text=trs)

def actualisestocks():
    opentable, timetable, pricetable = get()

    pricestocks = str(pricetable[-1])
    pricestocks2 = pricestocks.replace("{", " ")
    pricestocks3 = pricestocks2.replace("}", " ")
    srt = "The price is at " + pricestocks3 + "for the time " + str(timetable[-1])
    lbl.configure(text=srt)


def buy():
    global money
    were = combobuy.get()
    werestock = Stock([were])
    costprice = werestock.get_price()
    much = spinbuy.get()
    cost = costprice * float(much)
    if cost > money:
        messagebox.showinfo('!!!!!!!!!!!!!!', "You can't affrod this!!!!")
    else:
        selllist.append(were)
        selllist.append(much)
        selllist.append(" actions")
        money = money - cost
        actualisemoney()
        actualiseactions()
        actualisestocks()
    return money

def sell():
    global money
    actualiseactions()
    whatsell = combosell.get()
    wheresell = Stock([whatsell])

    werestocklist = selllist.index(whatsell)
    moneyy = wheresell.get_price() * float(selllist[werestocklist + 1])
    money = money + moneyy
    selllist.pop(werestocklist + 2)
    selllist.pop(werestocklist + 1)
    selllist.pop(werestocklist)
    actualiseactions()
    actualisemoney()
    actualisestocks()
    return money


window = Tk()
window.title("Stock Game")
window.geometry('1600x900')

lbl = Label(window, text="a", font=("Arial Bold", 10))
lbl.grid(column=1, row=0)

moneylbl = Label(window, text="a", font=("Arial Bold", 15))
moneylbl.grid(column=1, row=5)

actionlbl = Label(window, text="a", font=("Arial Bold", 10))
actionlbl.grid(column=1, row=7)

btnbuy = Button(window, text="Buy", command=buy)
btnbuy.grid(column=0, row=1)
btnsell = Button(window, text="sell", command=sell)
btnsell.grid(column=0, row=6)

combobuy = Combobox(window)
combobuy['values'] = companies
combobuy.current(1)  # set the selected item
combobuy.grid(column=0, row=2)

combosell = Combobox(window)
combosell['values'] = companies
combosell.current(1)  # set the selected item
combosell.grid(column=0, row=7)

spinbuy = Spinbox(window, from_=1, to=100, width=5)
spinbuy.grid(column=0, row=3)




def get():
    open = stocks.get_open()
    price = stocks.get_price()
    times = time.strftime("%H:%M:%S")
    opentable.append(open)
    timetable.append(times)
    pricetable.append(price)

    return opentable, timetable, pricetable


while True:

    actualisestocks()
    actualisemoney()
    actualiseactions()
    window.mainloop()