import random

def wake():
    wake = random.randint(1,2)
    if wake == 1:
        return "Hummm, no"
    else:
        return "Pffff, yes"

def sleep():
    print("ZZZZZzzzzz")
    print("wake up!!")
    print(wake())



sleep()
    
