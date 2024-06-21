import os
import cv2
path="Images/Images"
images=[]
for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        filename=path+"/"+file
        images.append(filename)
count=len(images)
frame=cv2.imread(images[0])
height,width,channel=frame.shape
size=(width,height)
out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size) 
for i in range(0,count):
    frames=cv2.imread(images[i])
    out.write(frames)
out.release()
print("Done")            