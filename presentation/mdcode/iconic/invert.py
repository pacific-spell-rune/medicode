import cv2
import os
import numpy as np

def invert_black_to_white(img_path):
    img = cv2.imread(img_path)
    black_mask = np.all(img == [0, 0, 0], axis=2)
    img[black_mask] = [255, 255, 255]
    cv2.imwrite(f"inverted_{os.path.basename(img_path)}", img)
    
def invert_images_in_dir(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(dir_path, filename)
            invert_black_to_white(img_path)
diry="icons"
invert_images_in_dir(diry)