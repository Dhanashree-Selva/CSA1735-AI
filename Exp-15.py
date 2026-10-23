from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
 
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2,
    random_state=42, stratify=data.target
)
 
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
 
print("Predictions:", predictions)
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
