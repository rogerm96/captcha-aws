import cv2
import keras
import string
import numpy as np
#from breaker import predict
from keras.models import load_model

model = load_model('predict.h5')

symbols = string.ascii_lowercase + "0123456789" # All symbols captcha can contain

# Define function to predict captcha
def predict(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = img / 255.0
    else:
        print("Not detected");
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))
        #probs.append(np.max(a))

    capt = ''
    for l in l_ind:
        capt += symbols[l]
    return capt#, sum(probs) / 5

# Lets Predict By Model
text = predict('./captcha1.png')
print("Predicted Captcha =",text)

with open('text.json', 'w') as f:
    json.dump(text, f)