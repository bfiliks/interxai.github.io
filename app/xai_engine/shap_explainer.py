# shap_explainer.py

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

        # Background data (raw text)
        background_texts = [
            "AI needs transparency.",
            "Explainability matters in ML.",
            "Some predictions are fair.",
            "This model is good."
        ]

        # Pre-transform background data
        self.background_data = self.vectorizer.transform(background_texts)

        # SHAP kernel explainer with predict_proba
        self.explainer = shap.Explainer(self.model.predict_proba, self.background_data)

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
            transformed = self.vectorizer.transform([text])
            shap_values = self.explainer(transformed)

            # Map back token importance using inverse_transform
            tokens = self.vectorizer.inverse_transform(transformed)[0]
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
