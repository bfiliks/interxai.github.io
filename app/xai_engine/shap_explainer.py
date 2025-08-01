# shap_explainer.py
"""
SHAPExplainer module for InterXAI
Generates SHAP explanations for model predictions.
"""

import shap
import joblib
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class SHAPExplainer:
    def __init__(self):
        self.model = self._load_model()
        self.vectorizer = self.model.named_steps["tfidf"]
        
        # Provide a small background dataset for SHAP explainer initialization
        background_texts = [
            "AI is powerful but needs explanation.",
            "Machine learning predictions need clarity."
        ]
        background_data = self.vectorizer.transform(background_texts)

        # SHAP expects transformed input, not transform function
        self.explainer = shap.Explainer(self.model.predict_proba, background_data)

    def _load_model(self):
        try:
            return joblib.load("model_pipeline.pkl")
        except FileNotFoundError:
            return self._train_fallback_model()

    def _train_fallback_model(self):
        sample_texts = [
            "Good AI explanation", "Poor result",
            "Fair accuracy and transparency", "Unclear model output"
        ]
        labels = [1, 0, 1, 0]
        model = Pipeline([
            ("tfidf", TfidfVectorizer()),
            ("classifier", LogisticRegression())
        ])
        model.fit(sample_texts, labels)
        joblib.dump(model, "model_pipeline.pkl")
        return model

    def explain(self, text: str):
        try:
            X_transformed = self.vectorizer.transform([text])
            shap_values = self.explainer(X_transformed)

            # Retrieve tokens and importance scores
            tokens = self.vectorizer.inverse_transform(X_transformed)[0]
            scores = shap_values.values[0][:len(tokens)]

            return {
                "tokens": list(tokens),
                "importance": list(scores)
            }
        except Exception as e:
            return {"error": str(e)}

# Local test
if __name__ == "__main__":
    explainer = SHAPExplainer()
    result = explainer.explain("This model is hard to understand.")
    print(result)
