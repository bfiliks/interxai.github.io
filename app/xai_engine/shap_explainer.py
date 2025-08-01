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

        # Background data for SHAP (raw text)
        background_texts = [
            "AI needs transparency.",
            "Explainability matters in ML.",
            "Good and bad predictions exist."
        ]

        # SHAP expects a pipeline: we use the whole pipeline
        self.explainer = shap.Explainer(self.model, self.vectorizer.transform(background_texts))

    def _load_model(self):
        try:
            return joblib.load("model_pipeline.pkl")
        except FileNotFoundError:
            return self._train_fallback_model()

    def _train_fallback_model(self):
        # Fallback model for testing/demo purposes
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
            # Input for SHAP should be raw text if pipeline includes vectorizer
            shap_values = self.explainer([text])
            tokens = shap_values.data[0]
            scores = shap_values.values[0].tolist()
            return {
                "tokens": tokens,
                "importance": scores
            }
        except Exception as e:
            return {"error": str(e)}

# Test locally
if __name__ == "__main__":
    explainer = SHAPExplainer()
    result = explainer.explain("This model is hard to understand.")
    print(result)
