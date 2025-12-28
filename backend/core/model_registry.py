MODEL_REGISTRY = {
    "classification": [
        {
            "name": "Logistic Regression",
            "import": "from sklearn.linear_model import LogisticRegression",
            "constructor": "LogisticRegression(max_iter=1000)"
        },
        {
            "name": "Random Forest Classifier",
            "import": "from sklearn.ensemble import RandomForestClassifier",
            "constructor": "RandomForestClassifier(n_estimators=200, random_state=42)"
        },
        {
            "name": "Support Vector Machine",
            "import": "from sklearn.svm import SVC",
            "constructor": "SVC(kernel='rbf', probability=True)"
        }
    ]
}


