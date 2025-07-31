# shap_explainer.py
import shap
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Caching and error handling
class SHAPExplainer:
    def __init__(self):
        self.model = self._load_model()
        self.vectorizer = self.model.named_steps["tfidfvectorizer"]
        self.explainer = shap.Explainer(self.model.predict_proba, self.vectorizer)

    def _load_model(self):
        try:
            return joblib.load("model_pipeline.pkl")
        except Exception:
            sample_texts = [
                "Good AI explanation",
                "Poor result",
                "Fair accuracy and transparency",
                "Unclear model output"
            ]
            labels = [1, 0, 1, 0]
            model = Pipeline([
                ("tfidfvectorizer", TfidfVectorizer()),
                ("classifier", LogisticRegression())
            ])
            model.fit(sample_texts, labels)
            joblib.dump(model, "model_pipeline.pkl")
            return model

    def explain(self, text):
        try:
            shap_values = self.explainer([text])
            return {
                "tokens": shap_values.data[0].tolist(),
                "importance": shap_values.values[0].tolist()
            }
        except Exception as e:
            return {"error": str(e)}

# Usage example
if __name__ == "__main__":
    explainer = SHAPExplainer()
    result = explainer.explain("This model is hard to understand.")
    print(result)
