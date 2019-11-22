# THIS IS THE "SERVER"
# DO NOT MODIFY. But you can look..
# --------------------

import keras
import numpy as np

def serverCheckInput(img):
    if serverCheckInput.model is None:
        serverCheckInput.model = keras.models.load_model('./model.h5')

    prediction = serverCheckInput.model.predict(np.reshape(img, (1, 2, 2, 1)))
    if np.argmax(prediction[0]) == 0:
        return (1, "Access Granted!")
    else:
        return (0, "Access Denied.")

serverCheckInput.model = None