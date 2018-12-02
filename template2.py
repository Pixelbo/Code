from PIL import ImageGrab
import numpy as np
pil_img = ImageGrab.grab()
opencv_img = np.array(pil_img)