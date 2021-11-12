from flask import Flask
from flask import jsonify
from flask import *
from model import FacialExpModel
import json
import os
import base64
import numpy as np

from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app, support_credentials=True)

test_model = FacialExpModel("model.json", "model_weights.h5")

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/rating/', methods = ['POST'])
def upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename)
            result = test_model.predict_emotion(file)
            return json.dumps(result.tolist()[0], cls=NumpyEncoder)


@app.route('/rateVideo',methods = ['POST'])
@cross_origin()
def upload_video_frame():
    if request.method == 'POST':
        imageArray = request.get_json()["images"]
        data = []
        for img in imageArray:
            print(img)
            result = test_model.predict_emotion(img)
            data.append(result.tolist()[0])
            print(data)
        return json.dumps(data, cls=NumpyEncoder)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.debug = True
    app.run(host='0.0.0.0', port=4000)