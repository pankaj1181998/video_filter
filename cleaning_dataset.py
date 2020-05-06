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

for filename in listdir(sfw_dir):
  if filename.endswith('.jpg'):
    try:
      img = io.imread(sfw_dir +'/'+ filename) # open the image file
      print('Reading '+filename)
        # verify that it is, in fact an image
    except (IOError) as e:
      print('Bad file:', filename) 
      # os.remove(sfw_dir + filename)
