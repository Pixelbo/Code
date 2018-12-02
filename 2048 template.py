import pyscreenshot as ImageGrab
import cv2
import numpy as np

numbers = [r"D:\2048-2.png", r"D:\2048-4.png", r"D:\2048-8.png", r"D:\2048-16.png"]
colors = [(255,0,0), (0,255,0), (0,0,255)]

if __name__ == "__main__":
    # fullscreen
    im=ImageGrab.grab()
    im.save(r'D:\2048bot.png')

    global color
    color = 0
    for img in numbers:
        img_rgb = cv2.imread(r'D:\2048bot.png')
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img ,0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), colors[color], 2)

        cv2.imwrite(r'D:\2048bot.png',img_rgb)

        color += 1
