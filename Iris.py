from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target variable

# Create a k-Nearest Neighbors classifier
k = 3  # You can change this value
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# Function to predict the Iris species
def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width):
    data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = knn.predict(data)
    return iris.target_names[prediction[0]]