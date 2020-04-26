# Importing all necessary libraries 
import cv2 
import os
import time 

def create_frames(name : str):
	dir_name = name.replace(".mp4","")
	dir_name = name.replace(".avi","")
	cam = cv2.VideoCapture("video_input/"+name)
	try :
	   if not os.path.exists("frames/"+dir_name):
	      os.makedirs("frames/"+ dir_name)
	except OSError :
	   print ('Error: Creating directory of data')

	#frame
	currentframe = 0
	while (True) :
	   time.sleep(5)
	   ret,frame = cam.read()

	   if ret:
	      name = 'frames/'+dir_name+'/frame'+str(currentframe)+'.jpg'
	      print ('Creating...' + name) 

	      # Creating Images 
	      cv2.imwrite(name,frame)

	      currentframe += 1
	   else:
	      break 
	# Release all space and windows once done
	cam.release()
	cv2.destroyAllWindows()

