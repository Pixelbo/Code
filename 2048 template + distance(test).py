import pyscreenshot as ImageGrab
import cv2
import numpy as np
import time

numbers = [r"D:\2048-2.png", r"D:\2048-4.png", r"D:\2048-8.png", r"D:\2048-16.png"]
colors = [(255,0,0), (0,255,0), (0,0,255), (255,0,255)]
x =[]
y = []
centerx = []
centery = []
name = []
names = []
test = []
line = []

##suprime les doublons##
def doublons(inn, out):
    for i in inn:
        if i not in out:
            out.append(i)
            time.sleep(0.1)
##########################


##main sript##
if __name__ == "__main__":
    #prends un screenshot et le sauvgarde
    im=ImageGrab.grab()
    im.save(r'D:\2048bot.png')

    #matching templates avec rectangles
    global color
    color = 0
    for img in numbers:

        img_rgb = cv2.imread(r'D:\2048bot.png')
        gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img ,0)

        res = cv2.matchTemplate(gray, template, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        min_thresh = (min_val + 1e-6) * 1.5
        match_locations = np.where(res <= min_thresh)

        w, h = template.shape[::-1]
        for (xpt, ypt) in zip(match_locations[1], match_locations[0]):
            x.append(xpt)
            y.append(ypt)
            name.append(numbers[color])
            cv2.rectangle(img_rgb, (xpt, ypt), (xpt + w, ypt + h), colors[color], 1)
            test.append((xpt + w, ypt + h))
        cv2.imwrite(r'D:\2048bot.png',img_rgb)
        color += 1

        # triage des positions x et y n°2 et marque cercle au centre puis rajoute la valeur du centre dans une liste
    yyyy = 0
    for xxxx in x:
        w2 = np.round(w / 2)
        h2 = np.round(h / 2)
        img = cv2.circle(img_rgb, (xxxx + int(w2), y[yyyy] + int(h2)), 5, (255, 0, 255), -1)

        centerx.append(xxxx + int(w2))
        centery.append(x[yyyy] + int(h2))
        yyyy += 1

    cv2.imwrite(r'D:\2048bot.png', img_rgb)

        # triage des positions des plaques
    j = 0
    p=14
    o = 0

    time.sleep(1)

    for i in range(10000):
        try:
            names.append(name[j])
            j += p
            p += o
            o += 2
        except:
            pass

for name1 in name:
    name2 = name.index(name1)
    if not name2 == len(name)-1:
        if name[name2] == name[name2+1]:
            x1 = x[name2]
            y1 = y[name2]
            x2 = x[name2+1]
            y2 = y[name2+1]
            cv2.line(img_rgb, (x1 + int(w2), y1 + int(h2)), (x2 + int(w2), y2 + int(h2)), 5)
            cv2.imwrite(r'D:\2048bot.png', img_rgb)
            line.append((x1 + int(w2), y1 + int(h2)))
            line.append((x2 + int(w2), y2 + int(h2)))
        else:
            print("hum")

