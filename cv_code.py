import cv2
import numpy as np

def get_colored_image(r, g, b, switch):
    img = np.zeros((300, 512, 3), np.uint8)
    if switch == 1:
        img[:] = [r, g, b]
    return img
