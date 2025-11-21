import xgboost as xgb
from sklearn.metrics import accuracy_score

def train_xgb(X_train, y_train, X_test, y_test, scale_pos_weight=None):
    """
    Trains a tuned XGBoost classifier.
    """

    model = xgb.XGBClassifier(
        n_estimators=695,
        learning_rate=0.02,
        max_depth=5,
        min_child_weight=6,
        gamma=0.14,
        subsample=0.91,
        colsample_bytree=0.96,
        reg_alpha=0.37,
        reg_lambda=1.82,
        scale_pos_weight=scale_pos_weight,
        random_state=42,
        eval_metric="logloss",
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)

    print(f"Model accuracy: {accuracy:.4f}")
    return model, preds
