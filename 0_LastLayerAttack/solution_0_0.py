''' 
Solution to Exercise:

1. Get some Software that can view and edit .h5 data. For example the official 
   HDFView - https://www.hdfgroup.org/downloads/hdfview/
2. Open the model.h5 file. 
3. Explore the file and check the Neural Network Model layout by navigating to 
   the /model_weights/ node and double clicking on layer_names:

   ->  Conv -- Conv -- MaxPool -- Dense -- Dense

   (We ignore the Dropout and Flatten. Some consider them layers, some don't.)

4. We navigate to the root node and double click training_config to find the 
   training parameters and see that the model was trained with

   -> Adadelta

5. Generally, the layers found in the model *could* be used for most of the
   models listed in the exercise, but this setup works best for image 
   classification. However, here are some pointers:

   a. training_config tells us it was trained with a categorical_crossentropy
      loss function. A good hint that we are dealing with some sort of
      classification.
   b. model_config tells us that conv2d_1 takes as input 
      "batch_input_shape": [null, 28, 28, 1] which hints at an image of size
      28 x 28.
   c. model_config also tells us that the last layer, dense_2, uses an 
      "activation": "softmax" which is a good hint that we are doing 
      classification.
   d. We can attempt to look for papers that have a similar architecture
      and see what they are doing. This is quite difficult, as there are so
      many papers published each week. As an example, it seems like we are
      dealing with a modified LeNet (Figure 2): 
      http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf
      Which does image classification 

   -> Image Classification
   


'''