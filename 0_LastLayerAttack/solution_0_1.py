''' 
Solution to Exercise:

1. Get some Software that can view and edit .h5 data. For example the official 
   HDFView - https://www.hdfgroup.org/downloads/hdfview/
2. Open the model.h5 file. 
3. If you are using HDFView, don't forget to reload as Read/Write!
4. Explore the file and check the Neural Network Model layout by navigating to 
   the /model_weights/ node and double clicking on layer_names
5. From there, we see that dense_2 is the final layer
6. (Varies, depending on your personal preference) - Edit:
   bias:0 @ /model_weights/dense_2/dense_2/
   and set the bias for value 4 to a high, positive number,
   for example: 100
'''