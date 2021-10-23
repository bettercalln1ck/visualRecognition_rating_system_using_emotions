from flask import Flask
from flask import jsonify
from model import FacialExpModel


test_model = FacialExpModel("model.json", "model_weights.h5")

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/rating/', methods = ['POST'])
def hello():

    if 'file' not in request.files:







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)