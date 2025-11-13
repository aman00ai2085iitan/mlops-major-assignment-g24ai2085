# train.py
import joblib
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import os

def main():
    data = fetch_olivetti_faces()
    X = data.data  # flattened images (400, 4096)
    y = data.target
    # split 70% train, 30% test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # save model and test set for testing later
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, "artifacts/savedmodel.pth", compress=3)  # compress level 3
    # save test split for test.py
    joblib.dump((X_test, y_test), "artifacts/test_split.pth", compress=3)

    # print train accuracy for quick info
    preds = model.predict(X_train)
    print("Train accuracy:", accuracy_score(y_train, preds))

if __name__ == "__main__":
    main()
