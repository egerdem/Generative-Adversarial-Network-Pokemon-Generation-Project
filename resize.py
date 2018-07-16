# resize pokeGAN.py
import os
import cv2
from PIL import Image

src = "./data" #pokeRGB_black
dst = "./resizeddate_ege" # resized

os.mkdir(dst)

for each in os.listdir(src):
    imga = Image.open(os.path.join(src,each))
    new = imga.resize(img,(256,256))
    new.save(os.path.join(dst,each))
dst = "./resized_black_ege/"
os.mkdir(dst)

for each in os.listdir(src)
    png = Image.open(os.path.join(src,each))
    #print each
    
    Image.open(os.path.join(src,each)).convert('RGB').save(os.path.join(dst,each.split('.')[0]+ '.jpg'), 'JPEG')
    
