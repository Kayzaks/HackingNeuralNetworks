''' 
Please read the README.md for Exercise instructions!
'''

# THIS IS THE CLIENT
# ------------------

from server import serverCheckInput
from skimage import io
import numpy as np

tests = 50
successes = 0

for i in range(tests):
    img = np.random.random((2,2))
    checked = serverCheckInput(img)
    if (checked[0]) == 1:
        successes = successes + 1

print('\n' + str(successes) + '/'+ str(tests) + ' succeeded\n' )
