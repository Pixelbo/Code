import pyscreenshot as ImageGrab
import cv2
import numpy as np
import time

numbers = [r"D:\2048-2.png", r"D:\2048-4.png", r"D:\2048-8.png", r"D:\2048-16.png"]
colors = [(255,0,0), (0,255,0), (0,0,255), (255,0,255)]
x =[]
xx =[]
xxx =[]
y = []
yy = []
yyy = []
centerx = []
centery = []
centerx2 = []
centery2 = []
name = []
names = []
test = []

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
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img ,0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            x.append(pt[0])
            y.append(pt[1])
            name.append(numbers[color])
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), colors[color], 1)
            test.append((pt[0] + w, pt[1] + h))
        cv2.imwrite(r'D:\2048bot.png',img_rgb)
        color += 1

        #triage des positions x et y n°1
        j = 0
        for i in range(16):
            try:
                xx.append(x[j])
                yy.append(y[j])
                j += 14
            except:
                print("")

        # suprime les donblons depuis le triage n°1
        doublons(xx, xxx)
        doublons(yy, yyy)
        # triage des positions x et y n°2 et marque cercle au centre puis rajoute la valeur du centre dans une liste
        yyyy = 0
        for xxxx in xxx:
            w2 = np.round(w/2)
            h2 = np.round(h/2)
            img = cv2.circle(img_rgb, (xxxx+int(w2), yyy[yyyy]+int(h2)), 5, (255, 0, 255), -1)

            centerx.append(xxxx+int(w2))
            centery.append(yyy[yyyy]+int(h2))
            yyyy += 1

        cv2.imwrite(r'D:\2048bot.png',img_rgb)

        # suprime les donblons depuis le triage n°2
        doublons(centerx, centerx2)
        doublons(centery, centery2)

        # triage des positions des plaques
        j = 0
        p=14
        o = 0

        time.sleep(1)

    for i in range(99999):
        try:
            names.append(name[j])
            print(j)
            j += p
            p += o
            o += 2
        except:
            print("")