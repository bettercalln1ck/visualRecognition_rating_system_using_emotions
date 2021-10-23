from tensorflow.keras.models import model_from_json
import numpy as np


class FacialExpModel(object):

    def __init__(self,model_json,model_weights):
        with open('model.json','r') as json_file:
            json_savedModel = json_file.read()

        self.model = model_from_json(json_savedModel)
        self.model.load_weights('model_weights.h5')

    def predict_emotion(self,img):
        return self.model.predict(img)    




