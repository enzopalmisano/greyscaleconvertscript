import cv2
from os import listdir,makedirs
from os.path import isfile,join
import os

path = 'insert source path' # Source Folder
dstpath = 'insert destination path' # Destination Folder

while True:
    input_dir = input("select directory: ")
    input_dir = input_dir+"/"
    if input_dir == "exit":
        break
    try:
        makedirs(dstpath+input_dir)
    except:
        print ("Directory already exist, images will be written in asme folder")

        # Folder won't used
    files = [f for f in listdir(path+input_dir) if isfile(join(path+input_dir,f))]

    for image in files:
        img = cv2.imread(os.path.join(path+input_dir,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath+input_dir,image)
        cv2.imwrite(dstPath,gray)
