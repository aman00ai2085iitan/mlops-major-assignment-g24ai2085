# test.py
import joblib
from sklearn.metrics import accuracy_score

def main():
    model = joblib.load("artifacts/savedmodel.pth")
    X_test, y_test = joblib.load("artifacts/test_split.pth")

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test accuracy: {acc:.4f}")

if __name__ == "__main__":
    main()
