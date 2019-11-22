''' 
Please read the README.md for Exercise instructions!
'''

import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
from pycuda.compiler import SourceModule
from skimage import io


# Load the Image File with skimage.
# ('imread' was deprecated in SciPy 1.0.0, and will be removed in 1.2.0.)
image = io.imread('./testimage.png')

# Feel free to edit above this line, so you don't need to
# draw everything in Photoshop or Paint... But nothing
# below!
#########################################################

width, height = image.shape

maxWidth = 4

if width != height:
    print("Image must be square in size and a maximum of 4x4!")
    exit()
    
linearizedImage = np.zeros(width * height, dtype=np.float32)
for i in range(width):
    for j in range(height):
        linearizedImage[i * height + j] = image[i][j] / 255.0


processedImage = np.zeros(maxWidth * maxWidth, dtype=np.float32)

# Allocate Memory for the Images on the GPU
gpuImgSize = np.int32(width)
gpuImage = cuda.mem_alloc(linearizedImage.nbytes)
gpuProcessedImage = cuda.mem_alloc(processedImage.nbytes)

weights = np.random.random(size=(32)).astype(np.float32) * 0.1
biases = np.array([1.0, 0.0], dtype=np.float32)
results = np.array([0.0, 0.0], dtype=np.float32)

# Allocate Memory for the Neural Network on the GPU
gpuWeights = cuda.mem_alloc(weights.nbytes)
gpuBiases = cuda.mem_alloc(biases.nbytes)
gpuResults = cuda.mem_alloc(results.nbytes)

# Copy over all the Data to the GPU
cuda.memcpy_htod(gpuImage, linearizedImage)
cuda.memcpy_htod(gpuWeights, weights)
cuda.memcpy_htod(gpuBiases, biases)
cuda.memcpy_htod(gpuResults, results)

# CUDA Source Code for the Preprocessor and Classifier
mod = SourceModule("""
    __global__ void preprocess
      ( int imgSize, float *newImg, float *prcImg )
    {
        int row = threadIdx.x * imgSize;

        // Lighten the image a bit...
        for(int i=0; i<(imgSize); i++)
        {
           prcImg[row + i] = newImg[row + i] + 0.1;
        }
    }
    
    __global__ void classify
      ( float *prcImg, float *weights, float *biases, float *results )
    {
        // "Fake" Classification using two Neurons

        // Neuron 1 and 2
        float result1 = 0.0;
        float result2 = 0.0;

        for(int i=0; i<16; i++)
        {
            result1 = result1 + prcImg[i] * weights[i];
            result2 = result2 + prcImg[i] * weights[i + 16];
        }

        // ReLu
        results[0] = max(result1 + biases[0], 0.0);
        results[1] = max(result2 + biases[1], 0.0);
    }    
     """)

preproc = mod.get_function("preprocess")
classify = mod.get_function("classify")

# Run the Preprocessor for each Line in the Image
preproc(gpuImgSize, gpuImage, gpuProcessedImage,  
     block=(width, 1, 1))
     
# Run the Classifier once
classify(gpuProcessedImage, gpuWeights, gpuBiases, gpuResults,
     block=(1, 1, 1))

# Copy the results from the GPU to the HOST
cuda.memcpy_dtoh(results, gpuResults)

# Check Access
access = np.argmax(results)

if access == 0:
    print("\nAccess DENIED!\n")
else:
    print("\nAccess GRANTED!\n")




cuda.memcpy_dtoh(weights, gpuWeights)
cuda.memcpy_dtoh(biases, gpuBiases)

print(weights)
print(biases)