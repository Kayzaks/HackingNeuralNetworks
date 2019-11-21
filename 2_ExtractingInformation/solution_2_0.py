''' 
Solution to Exercise:

The idea is to add a small network infront of the target
we want to bypass. We want to train that small network
to generate just one single image that gives us access.

This sounds harder than it is:
1. Load up the target network and make it un-trainable (we don't
   want to change it)
2. Add a small network infront of it, that is supposed to create a fake
   image which the target network thinks grants access
3. Set the output of this entire network to "access granted"
4. Train it and let backpropagation do its magic. It will attempt
   to train our small network in such a way that it gives the correct
   input to the target network, so that "access granted" lights up
'''

import keras
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

from keras.layers import Input, Dense, Reshape
from keras.layers import BatchNormalization, Activation, ZeroPadding2D
from keras.models import Sequential, Model
from keras.optimizers import Adam


# Load the target Model and make it untrainable 
target_model = keras.models.load_model('./model.h5')
target_model.trainable = False

# Create the fake-ID-generator network. It takes as input the same kind of
# vector that the target network would ouput (in our case, 10 different digits)
attack_vector = Input(shape=(10,))
attack_model = Sequential()

# Yes, its perfectly enough to have a single dense layer. We only want to create
# a single image. We don't care about overfitting or generalisation or anything.
attack_model = Dense(28 * 28, activation='relu', input_dim=10)(attack_vector)
attack_img = Reshape((28, 28, 1))(attack_model)
attack_model = Model(attack_vector, attack_img)

# Now, we combine both models. Attack Network -> Target Network
target_output = target_model(attack_img)
combined_model = Model(attack_vector, target_output)
combined_model.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))

# Time to train. 1000 epochs is probably way overkill, but just to make
# sure it works for everyone. It's super fast anyway
batch_size = 128
total_epochs = 1000

# Create the target "access granted" vector. In our case that means that
# Digit 4 is set to 1. We added some minor randomness (0.9 - 1.0) just for
# good measur
final_target = np.zeros((batch_size, 10))
for i in range(batch_size):
    final_target[i][4] = 0.9 + np.random.random() * 0.1

for x in range(total_epochs):
    combined_model.train_on_batch(final_target, final_target)
    if x % (int(total_epochs / 10)) == 0:
        print('Epoch ' + str(x) + ' / ' + str(total_epochs))

# The model is trained, let's generate the fake-ID and save it!
# Don't worry if it doesn't look anything like a digit 4, it will still work
fake_id = attack_model.predict(final_target)
fake_id = np.asarray(fake_id[0])
fake_id = np.reshape(fake_id, (28, 28))
# The scipy.misc.toimage() function was deprecated in Scipy 1.0.0, and was completely removed in version 1.3.0.
io.imsave('./fake_id.png', fake_id)

