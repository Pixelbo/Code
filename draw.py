from Xlib.display import Display
from Xlib import X
from Xlib import protocol

display = Display(':0')
root = display.screen().root
gc = root.create_gc()
root.fill_rectangle(gc, 100, 100, 500, 500)