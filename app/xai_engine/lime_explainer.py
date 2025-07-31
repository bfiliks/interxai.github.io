# lime_explainer.py
import lime.lime_text
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

class LIMEExplainer:
    def __init__(self):
        self.model = self._load_model()
        self.explainer = lime.lime_text.LimeTextExplainer(class_names=["Negative", "Positive"])

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
            exp = self.explainer.explain_instance(text, self.model.predict_proba, num_features=5)
            return dict(exp.as_list())
        except Exception as e:
            return {"error": str(e)}

# Usage example
if __name__ == "__main__":
    explainer = LIMEExplainer()
    result = explainer.explain("This model is hard to understand.")
    print(result)
