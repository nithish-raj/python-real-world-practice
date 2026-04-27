import os
import shutil
source = r"C:\Users\thang\Downloads"
for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(source+"/"+file,"Images/"+file)