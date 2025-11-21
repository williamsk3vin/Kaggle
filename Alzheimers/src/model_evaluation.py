from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

def evaluate_model(y_test, preds):
    """
    Prints accuracy, confusion matrix, and a full classification report.
    """
    print("Accuracy:", accuracy_score(y_test, preds))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, preds))
    print("\nClassification Report:\n", classification_report(y_test, preds))
