# Importing all necessary libraries 
import cv2 
import os
from moviepy.editor import VideoFileClip
import cv2

def create_frames(name : str):
   dir_name = name.replace(".mp4","")
   dir_name = name.replace(".avi","")
   cam = cv2.VideoCapture("video_input/"+name)
   try :
      if not os.path.exists("frames/"+dir_name):
         os.makedirs("frames/"+ dir_name)
   except OSError :
      print ('Error: Creating directory of data')
   clip = VideoFileClip("video_input/"+name)
   
   total = clip.duration

   cur_frame = 0.5
   frame_num = 1
   while cur_frame<total:
      cap = cv2.VideoCapture("video_input/"+name)
      # cap.set(cv2.CAP_PROP_POS_MSEC,1000)      # Go to the 1 sec. position
      cap.set(cv2.CAP_PROP_POS_MSEC,cur_frame*1000)      # Go to the 1 sec. position
      ret,frame = cap.read()                   # Retrieves the frame at the specified second
      cv2.imwrite('frames/'+dir_name+'/'+name+str(frame_num)+'.jpg', frame)          # Saves the frame as an image 
      cur_frame+=0.5
      frame_num+=1
      
################################################################################
# 	#frame
# 	currentframe = 0
# 	while (True) :
# 	   ret,frame = cam.read()

# 	   if ret:
# 	      name = 'frames/'+dir_name+'/frame'+str(currentframe)+'.jpg'
# 	      print ('Creating...' + name) 

# 	      # Creating Images 
# 	      cv2.imwrite(name,frame)

# 	      currentframe += 1
# 	   else:
# 	      break 
# 	# Release all space and windows once done
# 	cam.release()
# 	cv2.destroyAllWindows()

