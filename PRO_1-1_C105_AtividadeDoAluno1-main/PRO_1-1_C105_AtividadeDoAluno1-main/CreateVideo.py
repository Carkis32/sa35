import os
import cv2


path = "Image"

image = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        image.append(file_name)
        
print(len(image))
count = len(image)
