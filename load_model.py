# import os
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras import Model

# from keras.models import load_model
# import cv2
# import numpy as np

import tensorflow as tf

import numpy as np
import cv2


# model = tf.saved_model.load('saved_models/nsfw_model.h5')
model = tf.keras.models.load_model('saved_models/nsfw_model.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

img = cv2.imread('test2.jpg')
img = cv2.resize(img,(150,150))
img1 = (np.expand_dims(img,0))
# print( img )
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

classes = model.predict(img1)
print(classes)