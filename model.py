from tensorflow.keras.models import model_from_json
import numpy as np
import cv2
from PIL import Image
import base64
from io import BytesIO
from PIL import Image


class FacialExpModel(object):

    def __init__(self,model_json,model_weights):
        with open('model.json','r') as json_file:
            json_savedModel = json_file.read()

        self.model = model_from_json(json_savedModel)
        self.model.load_weights('model_weights.h5')

    def predict_emotion(self,img):
        #img = cv2.imread(img)
        # Convert into grayscale
        #jpg_as_np = np.frombuffer(img, dtype=np.uint8)
        #img = cv2.imdecode(jpg_as_np, flags=1)
        #print(type(img))
        #img = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_UNCHANGED)
        #print(type(img))
        #im_bytes = base64.b64decode(str(img)).decode("utf-8")   # im_bytes is a binary image
        #im_file = BytesIO(im_bytes)  # convert image to file-like object
        #img = Image.open(im_file)
        img = img.split(',')[1]
        pil_image = np.fromstring( base64.b64decode(img), np.uint8)
        pil_image =  cv2.imdecode(pil_image, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(pil_image, cv2.COLOR_RGB2BGR)
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
            return np.array([[0,0,0,0,0,0,0]])
        

        
        for (x, y, w, h) in faces:
            
            faces = gray[y:y + h, x:x + w]
            faces = cv2.resize(faces,(48,48))
#            img = np.reshape(faces,[1,48,48,1])
        return (self.model.predict(faces[np.newaxis, :, :, np.newaxis]))    




