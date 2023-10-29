from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Iris Flower Species Predictor"

@app.route("/predict", methods=["POST"])
def predict():
    # Your prediction logic here
    return "Prediction:"