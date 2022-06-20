import os
import numpy as np
from PIL import Image
base = os.path.dirname(os.path.abspath(__file__))
imag_dir = os.path.join(base,"image_data")

y_labels = []
x_train = []


for root,dirs,files in os.walk(imag_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(" ","-").lower()

            print(label,path)

            pil_image=Image.open(path).convert("L") #grayscale
            img_array= np.array(pil_image,"uint8")
            print(img_array)
            
