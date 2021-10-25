from tensorflow.keras.models import model_from_json
import numpy as np
import cv2


class FacialExpModel(object):

    def __init__(self,model_json,model_weights):
        with open('model.json','r') as json_file:
            json_savedModel = json_file.read()

        self.model = model_from_json(json_savedModel)
        self.model.load_weights('model_weights.h5')

    def predict_emotion(self,img):
        img = cv2.imread(img)
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # if img is None:
        #     result = "Image is empty!!"
        # else:
        #     faces = cv2.resize(img,(48,48))
        #     img = np.reshape(faces,[1,48,48,1])
        #     result = self.model.predict(img)
        #     print(result)
 
        # return str(result)
        

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
  
        # Detect faces  
        faces = face_cascade.detectMultiScale(gray, 1.3, 3)

        if len(faces) == 0:
            return "face not detected"
        

        
        for (x, y, w, h) in faces:
            
            faces = gray[y:y + h, x:x + w]
            faces = cv2.resize(faces,(48,48))
#            img = np.reshape(faces,[1,48,48,1])
        return str(self.model.predict(faces[np.newaxis, :, :, np.newaxis]))    




