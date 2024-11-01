import cv2
import numpy as np
import os

def c(img_p, t_color, n_color):
    img = cv2.imread(img_p)
    if img is None:
        return None
    
    lb = np.array([t_color[0] - 10, t_color[1] - 10, t_color[2] - 10])
    ub = np.array([t_color[0] + 10, t_color[1] + 10, t_color[2] + 10])
    msk = cv2.inRange(img, lb, ub)
    img[msk > 0] = n_color
    
    return img

d_p = 'icons'
o_p = 'modified_icons'
os.makedirs(o_p, exist_ok=True)

t_color = (255, 0, 0)
n_color = (161, 201, 179)
cnt = 1

for f in os.listdir(d_p):
    if f.endswith('.png'):
        img_p = os.path.join(d_p, f)
        mod_img = c(img_p, t_color, n_color)
        
        if mod_img is not None:
            out_p = os.path.join(o_p, f"{cnt}.jpg")
            cv2.imwrite(out_p, mod_img)
            cnt += 1
