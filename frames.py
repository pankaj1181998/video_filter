# Importing all necessary libraries 
import cv2 
import os

cam = cv2.VideoCapture('input/')
try :
   if not os.path.exists('frames'):
      os.makedirs('frames/')
except OSError :
   print ('Error: Creating directory of data')

#frame
currentframe = 0
while(True):
   ret,frame = cam.read()

   if ret:
      name = 'frames/file_name'+str(currentframe)+'.jpg'
      print ('Creating...' + name) 

      # Creating Images 
      cv2.imwrite(name,frame)

      currentframe += 1
   else:
      break 

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

