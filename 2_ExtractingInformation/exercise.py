''' 
Please read the README.md for Exercise instructions!


This code is a modified version of 
https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.py
If you want to train the model yourself, just head there and run
the example. Don't forget to save the model using model.save('model.h5')
'''

import keras
import numpy as np
from skimage import io

# Load the Image File with skimage.
# ('imread' was deprecated in SciPy 1.0.0, and will be removed in 1.2.0.)
image = io.imread('./fake_id.png')
processedImage = np.zeros([1, 28, 28, 1])
for yy in range(28):
    for xx in range(28):
        processedImage[0][xx][yy][0] = float(image[xx][yy]) / 255

# Load the Model 
model = keras.models.load_model('./model.h5')

# Run the Model and check what Digit was shown
shownDigit = np.argmax(model.predict(processedImage))

# Only Digit 4 grants access!
if shownDigit == 4:
    print("Access Granted")
else:
    print("Access Denied")