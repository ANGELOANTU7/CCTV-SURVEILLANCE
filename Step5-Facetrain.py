import os
base = os.path.dirname(os.path.abspath(__file__))
print("base is:" ,base)

imag_dir = os.path.join(base,"image_data")

for root,dirs,files in os.walk(imag_dir):
    for file in files:
       
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path=os.path.join(root,file)
            print(path)

