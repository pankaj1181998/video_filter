import tensorflow as tf
import pandas as pd
import numpy as np
import cv2
from pandas import ExcelWriter

model = tf.keras.models.load_model('saved_models/nsfw_or_sfw_model1.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
def load_model_and_calculate(file_name :str):
   
   
   # img = cv2.imread('4.jpg')
   # img = cv2.resize(img,(150,150))
   # img1 = (np.expand_dims(img,0))
   # classes = model.predict(img1)
   # print(classes)
   
   data = pd.read_excel('Report_File_Excels/'+file_name,sheet_name='Frames')

   lenn = len(data.name)
   

   for i in range(0,lenn):
      img_name = data.name[i]
      img = cv2.imread(img_name)
      img = cv2.resize(img,(150,150))
      img1 = (np.expand_dims(img,0))
      classes = model.predict(img1)
      if int(classes[0][0]) == 0:
         data.prediction[i]="nsfw"
      else :
         data.prediction[i]="sfw" 
         
   data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True) 
   with ExcelWriter('Report_File_Excels/'+file_name,engine="openpyxl") as writer:
       data.to_excel(writer,sheet_name="Frames")      
   writer.save()   