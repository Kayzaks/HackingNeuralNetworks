from server import serverCheckInput
from skimage import io
import numpy as np

# For completeness, here is an image that would have given access:
img = np.zeros((2, 2))

img[0][0] = 0.392
img[0][1] = 0.784
img[1][0] = 0.784
img[1][1] = 0.392

print(serverCheckInput(img)) 

# And here is one possible overflow of one of the pixels.

img[0][0] = 0.0
img[0][1] = 0.0
img[1][0] = 50000.0
img[1][1] = 0.0

print(serverCheckInput(img)) 