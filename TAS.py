from pynput.keyboard import Key, Listener, Controller
import time
import ast

fichier = open("D:\data.txt", "a")
fichier.write('"[')

keyboardd  = Controller()



def on_press(key):
    global start
    global fichier



    if key == Key.f2:
        start = True
        time.sleep(1)
        fichier = open("D:\data.txt", "a")
    if key == Key.f3:
        start = False

    if start:
        fichier.write(str(key)+", ")
    else:
        fichier.close()

    if key == Key.f4:
        fichier = open("D:\data.txt", "a")
        fichier.write(']"')
        fichier.close()

        fichierr = open("D:\data.txt", "r")
        read = ast.literal_eval(fichierr.read())
        for char in read:
            keyboardd.press(char)
            keyboardd.release(char)
            time.sleep(1)
        fichier.close()

with Listener(on_press=on_press) as listener:
    listener.join()
