''' 
Solution to Exercise 3:

The idea is to add some noise to our best-guess fake-ID.
'''


import keras
import numpy as np
from skimage import io

# Load the Model 
model = keras.models.load_model('./model.h5')

runs = 1000
max_intensity = 10

print('Running pure Random Test')
successes = 0
for i in range(runs):
    # Creating a pure Random Image
    processedImage = np.random.random([1, 28, 28, 1])

    # Run the Model and check what Digit was shown
    shownDigit = np.argmax(model.predict(processedImage))

    # Only Digit 4 grants access!
    if shownDigit == 4:
        successes = successes + 1

print('Pure Random had a ' + str(successes) + ' / ' + str(runs) + ' success rate')

# Best-Guess Fake ID
image = io.imread('./fake_id.png')
originalImage = np.zeros([1, 28, 28, 1])
for yy in range(28):
    for xx in range(28):
        originalImage[0][xx][yy][0] = float(image[xx][yy]) / 255


print('Running Best Guess + Random Test')

min_intensity = 40 # / 100
max_intensity = 50 # / 100

for intensity in range(min_intensity, max_intensity):
    successes = 0
    for i in range(runs):
        # Adding some Random noise to the image
        noise = np.random.random([1, 28, 28, 1]) * float(intensity) * 0.01

        processedImage = originalImage + noise

        # Run the Model and check what Digit was shown
        shownDigit = np.argmax(model.predict(processedImage))

        # Only Digit 4 grants access!
        if shownDigit == 4:
            successes = successes + 1

    print('Rand-Intensity ' + str(intensity) + ' had a ' + str(successes) + ' / ' + str(runs) + ' success rate')



print('Running Best Guess + Normal Distributed Noise Test')

min_intensity = 25 # / 100
max_intensity = 35 # / 100

for mu in range(min_intensity, max_intensity):
    successes = 0
    for i in range(runs):
        # Adding some Normal distributed Noise to the image
        noise = np.random.normal(float(mu) * 0.01, 0.05, [1, 28, 28, 1]) 

        processedImage = originalImage + noise

        # Run the Model and check what Digit was shown
        shownDigit = np.argmax(model.predict(processedImage))

        # Only Digit 4 grants access!
        if shownDigit == 4:
            successes = successes + 1

    print('Mu-intensity ' + str(mu) + ' had a ' + str(successes) + ' / ' + str(runs) + ' success rate')
