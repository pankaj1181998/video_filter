# from moviepy.editor import VideoFileClip
# import cv2

import os
import pandas as pd
import numpy as np
from pandas import ExcelWriter
# name='all_over.mp4'
# clip = VideoFileClip("video_input/"+name)
# print( clip.duration )
# total = clip.duration
import tensorflow as tf
import pandas as pd
import numpy as np
import cv2
from pandas import ExcelWriter
import time
# i = 0.5
# while i<total:
#    cap = cv2.VideoCapture("video_input/"+name)
#    # cap.set(cv2.CAP_PROP_POS_MSEC,1000)      # Go to the 1 sec. position
#    cap.set(cv2.CAP_PROP_POS_MSEC,i*1000)      # Go to the 1 sec. position
#    ret,frame = cap.read()                   # Retrieves the frame at the specified second
#    cv2.imwrite("image"+str(i)+".jpg", frame)          # Saves the frame as an image
#    # cv2.imshow("Frame Name",frame)           # Displays the frame on screen
#    # cv2.waitKey() 
#    i+=0.5


# print(pd.read_excel('Report_File_Excels/all_over.xlsx',sheet_name='Frames'))
# data = pd.read_excel('Report_File_Excels/countdown.xlsx',sheet_name='Sheet1')

# print(len(data.name))
# lenn = len(data.name)
# data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
# # data.reset_index(inplace=True)

# for i in range(0,lenn):
#     data.prediction[i]="sfw"
# with ExcelWriter('Report_File_Excels/countdown.xlsx'
#   ,engine="openpyxl") as writer:
#     data.to_excel(writer,sheet_name="Frames")   

# print(data)    

model = tf.keras.models.load_model('saved_models/nsfw_or_sfw_model1.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
img = cv2.imread('1.jpg')
img = cv2.resize(img,(150,150))
img1 = (np.expand_dims(img,0))
classes = model.predict(img1)
print(int(classes[0][0]))