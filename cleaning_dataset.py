import os
import cv2
from os import listdir
from PIL import Image
from skimage import io
   
base_dir = 'D:/Video_filtering/data'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Directory with our training pictures nsfw
nsfw_dir = os.path.join(train_dir, 'nsfw')
    
# Directory with our training dog pictures
sfw_dir = os.path.join(train_dir, 'sfw')
   
# Remoing from train/sfw
print('train/sfw-----------------------')
print()
for filename in listdir(sfw_dir+'/'):
  if filename.endswith('.jpg'):
    try:
      img = Image.open(sfw_dir+'/'+filename) # open the image file
      img.verify() # verify that it is, in fact an image
      print('Verified Image '+filename)
    except (IOError, SyntaxError) as e:
      print('*********Bad file***********:', filename) # print out the names of corrupt files
      os.remove(sfw_dir +'/'+ filename)
 
# Remoing from train/nsfw     
print('train/nsfw')
print()
for filename in listdir(nsfw_dir+'/'):
  if filename.endswith('.jpg'):
    try:
      img = Image.open(nsfw_dir+'/'+filename) # open the image file
      img.verify() # verify that it is, in fact an image
      print('Verified Image '+filename)
    except (IOError, SyntaxError) as e:
      print('Bad file:', filename) # print out the names of corrupt files
      os.remove(nsfw_dir +'/'+ filename)