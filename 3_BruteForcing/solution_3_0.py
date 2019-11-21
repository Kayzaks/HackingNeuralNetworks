''' 
Solution to Exercise:

The idea is to add some noise to our best-guess fake-ID.
'''



import keras
import numpy as np
from skimage import io

# Load the Model 
model = keras.models.load_model('./model.h5')

runs = 1000
max_intensity = 10

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

print('Pure Noise had a ' + str(successes) + ' / ' + str(runs) + ' success rate')


print('Running Best Guess + Noise Test')

# Best-Guess Fake ID
image = io.imread('./fake_id.png')
originalImage = np.zeros([1, 28, 28, 1])
for yy in range(28):
    for xx in range(28):
        originalImage[0][xx][yy][0] = float(image[xx][yy]) / 255

max_intensity = 10
successes = 0

for intensity in range(max_intensity):
    for i in range(runs):
        # Adding some Noise to the image
        noise = np.random.random([1, 28, 28, 1]) * float(intensity) * 0.1

        processedImage = originalImage + noise

        # Run the Model and check what Digit was shown
        shownDigit = np.argmax(model.predict(processedImage))

        # Only Digit 4 grants access!
        if shownDigit == 4:
            successes = successes + 1

    print('Intensity ' + str(intensity) + ' had a ' + str(successes) + ' / ' + str(runs) + ' success rate')
