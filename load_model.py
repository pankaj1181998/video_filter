import tensorflow as tf
import numpy as np
import cv2


model = tf.keras.models.load_model('saved_models/nsfw_or_sfw_model1.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

img = cv2.imread('testns1.jpg')
img = cv2.resize(img,(150,150))
img1 = (np.expand_dims(img,0))
# print( img )
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

classes = model.predict(img1)
print(classes)