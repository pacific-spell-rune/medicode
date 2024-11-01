import cv2
import numpy as np
import os

def c(i, tc, fc):
    img = cv2.imread(i)
    h, w = img.shape[:2]
    for x in range(w):
        for y in range(h):
            if tuple(img[y, x]) == tc: 
                img[y, x] = fc
    return img

d = 'icons'
c_folder = 'colored'
os.makedirs(os.path.join(d, c_folder), exist_ok=True)

tc = (0, 0, 0)  # Target Color (R, G, B)
fc = (0, 255, 0)  # Final Color (R, G, B)

for f in os.listdir(d):
    if f.endswith('.png'):
        i_path = os.path.join(d, f)
        o_path = os.path.join(d, c_folder, f)
        cv2.imwrite(o_path, c(i_path, tc, fc))
        