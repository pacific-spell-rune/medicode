import os
from PIL import Image
import numpy as np

def get_colors(img_path):
    i = Image.open(img_path)
    i = i.convert('RGB')
    img = np.array(i)
    return np.unique(img.reshape(-1, 3), axis=0)

def list_img_colors(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(dir_path, filename)
            colors = get_colors(img_path)
            print(f"{filename}:")
            print(colors)
            print()

list_img_colors('icons')