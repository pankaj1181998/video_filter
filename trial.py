from moviepy.editor import VideoFileClip
import cv2
name='all_over.mp4'
clip = VideoFileClip("video_input/"+name)
print( clip.duration )
total = clip.duration

i = 0.5
while i<total:
   cap = cv2.VideoCapture("video_input/"+name)
   # cap.set(cv2.CAP_PROP_POS_MSEC,1000)      # Go to the 1 sec. position
   cap.set(cv2.CAP_PROP_POS_MSEC,i*1000)      # Go to the 1 sec. position
   ret,frame = cap.read()                   # Retrieves the frame at the specified second
   cv2.imwrite("image"+str(i)+".jpg", frame)          # Saves the frame as an image
   # cv2.imshow("Frame Name",frame)           # Displays the frame on screen
   # cv2.waitKey() 
   i+=0.5