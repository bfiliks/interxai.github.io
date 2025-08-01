# lime_explainer.py
"""
LIMEExplainer module for InterXAI
Generates LIME explanations for model predictions.
"""

import joblib
from lime.lime_text import LimeTextExplainer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class LIMEExplainer:
    def __init__(self):
        self.model = self._load_model()
        self.explainer = LimeTextExplainer(class_names=["Negative", "Positive"])

    def _load_model(self):
        try:
            return joblib.load("model_pipeline.pkl")
        except FileNotFoundError:
            return self._train_fallback_model()

    def _train_fallback_model(self):
        # Fallback for demonstration or testing
        sample_texts = [
            "Good AI explanation",
            "Poor result",
            "Fair accuracy and transparency",
            "Unclear model output"
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
            explanation = self.explainer.explain_instance(
                text,
                self.model.predict_proba,
                num_features=5
            )
            # Return structured list
            return {
                "tokens": [token for token, _ in explanation.as_list()],
                "weights": [round(weight, 4) for _, weight in explanation.as_list()]
            }
        except Exception as e:
            return {"error": str(e)}


# Local test
if __name__ == "__main__":
    explainer = LIMEExplainer()
    result = explainer.explain("This model is hard to understand.")
    print(result)
