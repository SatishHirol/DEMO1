from flask import Flask, render_template, request
from Iris import predict_iris_species  # Import the function from Iris.py

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get user input from the form
    sepal_length = float(request.form.get("sepal_length"))
    sepal_width = float(request.form.get("sepal_width"))
    petal_length = float(request.form.get("petal_length"))
    petal_width = float(request.form.get("petal_width"))

    # Call the function from Iris.py to make predictions
    prediction = predict_iris_species(sepal_length, sepal_width, petal_length, petal_width)

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)