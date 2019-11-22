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

# Load the Model 
model = keras.models.load_model('./model.h5')

runs = 1000

print('Running pure Noise Test')
successes = 0
for i in range(runs):
    # Creating a pure Noise Image
    processedImage = np.random.random([1, 28, 28, 1])

    # Run the Model and check what Digit was shown
    shownDigit = np.argmax(model.predict(processedImage))

    # Only Digit 4 grants access!
    if shownDigit == 4:
        successes = successes + 1

print('Had a ' + str(successes) + ' / ' + str(runs) + ' success rate')

