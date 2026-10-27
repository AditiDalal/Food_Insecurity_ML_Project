def run_model(print_results=False):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import accuracy_score, classification_report

    # Load & clean
    df = pd.read_csv("train.csv")
    features = ["Pop2010", "PovertyRate", "MedianFamilyIncome", "Urban", "HUNVFlag"]
    label = "LILATracts_1And20"
    df = df.dropna()
    X = df[features]
    y = df[label]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    # ── Logistic Regression ──
    log_model = LogisticRegression(max_iter=1000, class_weight="balanced")
    log_model.fit(X_train, y_train)
    log_preds = log_model.predict(X_test)
    df["prediction"] = log_model.predict(X)

    # ── MLP Classifier (not returned) ──
    mlp_model = MLPClassifier(
        hidden_layer_sizes=(16, 8),
        solver="adam",
        alpha=1e-4,
        max_iter=500,
        random_state=42
    )
    mlp_model.fit(X_train, y_train)
    mlp_preds = mlp_model.predict(X_test)

    if print_results:
        print("Logistic Regression")
        print("Accuracy:", accuracy_score(y_test, log_preds))
        print(classification_report(y_test, log_preds, digits=3))

        print("MLP Classifier")
        print("Accuracy:", accuracy_score(y_test, mlp_preds))
        print(classification_report(y_test, mlp_preds, digits=3))

    return df, log_model


if __name__ == "__main__":
    run_model(print_results=True)
