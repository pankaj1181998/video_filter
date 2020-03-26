# Importing all necessary libraries 
import cv2 
import os

def create_frames(name : str):
	name.replace(".mp4","")
	name.replace(".avi","")
	cam = cv2.VideoCapture("input/"+name)
	try :
	   if not os.path.exists("frames/"+name):
	      os.makedirs("frames/"+ name)
	except OSError :
	   print ('Error: Creating directory of data')

	#frame
	currentframe = 0
	while (True) :
	   ret,frame = cam.read()

	   if ret:
	      name = 'frames/'+name+str(currentframe)+'.jpg'
	      print ('Creating...' + name) 

	      # Creating Images 
	      cv2.imwrite(name,frame)

	      currentframe += 1
	   else:
	      break 
	# Release all space and windows once done
	cam.release()
	cv2.destroyAllWindows()

