from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os


def train_model(X, y):

    print("\nTraining Machine Learning Model...\n")

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Random Forest model
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    # train model
    model.fit(X_train, y_train)

    # predictions
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Model Accuracy:", accuracy)
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))

    # create models folder if not exists
    os.makedirs("models", exist_ok=True)

    # save model
    joblib.dump(model, "models/fatigue_model.pkl")

    print("\nModel saved to models/fatigue_model.pkl")

    return model