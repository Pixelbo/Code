from pynput.mouse import Controller, Button
import time



mouse = Controller()
mouse.position = (908, 489)
time.sleep(1)
mouse.position = (906, 596)





#print(mouse.position)
#mouse.click(Button.left, 2)
#mouse.press(Button.left)
#mouse.release(Button.left)
#mouse.scroll(10 ,10)