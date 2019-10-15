''' 
Please read the README.md for Exercise instructions!


This code is a modified version of 
https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.py
If you want to train the model yourself, just head there and run
the example. Don't forget to save the model using model.save('model.h5')
'''


import keras
import numpy as np
from scipy import misc

# Load the Image File
image = misc.imread('0_LastLayerAttack/fake_id.png')
processedImage = np.zeros([1, 28, 28, 1])
for yy in range(28):
    for xx in range(28):
        processedImage[0][xx][yy][0] = float(image[xx][yy]) / 255

# Load the Model 
model = keras.models.load_model('0_LastLayerAttack/model.h5')

# Run the Model and check what Digit was shown
shownDigit = np.argmax(model.predict(processedImage))

print(model.predict(processedImage))

# Only Digit 4 grants access!
if shownDigit == 4:
    print("Access Granted")
else:
    print("Access Denied")
