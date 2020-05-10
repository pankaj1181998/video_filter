# Importing all necessary libraries 
import cv2 
import os
from moviepy.editor import VideoFileClip


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
   file_name = name.replace(".mp4","")
   file_name = file_name.replace(".avi","")
   cur_frame = 0.5
   frame_num = 1
   while cur_frame<total:
      try:
         cap = cv2.VideoCapture("video_input/"+name)
         # cap.set(cv2.CAP_PROP_POS_MSEC,1000)      # Go to the 1 sec. position
         cap.set(cv2.CAP_PROP_POS_MSEC,cur_frame*1000)      # Go to the 1 sec. position
         ret,frame = cap.read()                   # Retrieves the frame at the specified second
         cv2.imwrite('frames/'+dir_name+'/'+file_name+str(frame_num)+'.jpg', frame)          # Saves the frame as an image 
         print('Creating '+file_name+' '+str(frame_num)+'.jpg' )
         cur_frame+=0.5
         frame_num+=1
      except:
          break
