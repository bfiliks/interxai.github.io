# shap_explainer.py
"""
SHAP Explainer Module for InterXAI
Generates SHAP explanations for NLP models.
"""

import shap
import numpy as np
import transformers
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import functools

# Load model and tokenizer (replace with your preferred model)
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, return_all_scores=True)
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    tokenizer = None
    model = None
    classifier = None

def _predict_proba(texts):
    """Wrapper for pipeline output suitable for SHAP."""
    if classifier is None:
        raise RuntimeError("Model pipeline is not initialized.")
    results = classifier(texts)
    return np.array([[x["score"] for x in example] for example in results])

@functools.lru_cache(maxsize=128)
def explain_with_shap(text):
    """
    Generate SHAP explanation for input text.

    Args:
        text (str): Input text to explain.

    Returns:
        dict: Dictionary with tokens and SHAP importance values.
    """
    if not tokenizer or not model:
        return {"error": "Model/tokenizer not initialized."}

    try:
        explainer = shap.Explainer(_predict_proba, tokenizer)
        shap_values = explainer([text])
        tokens = shap_values.data[0]
        importance = shap_values.values[0].tolist()
        return {
            "tokens": tokens,
            "importance": importance
        }
    except Exception as e:
        return {"error": str(e)}
