
"""
annotator_interface.py
Simulates a human annotation engine for critique and intertextual interpretation.
"""

import logging

# In-memory annotation store (for demo purposes)
annotations_db = {}

def submit_annotation(sample_id, annotator, interpretation, tags=None, notes=None):
    """
    Stores a human annotation for a given sample.

    Args:
        sample_id (str): ID of the sample or model output.
        annotator (str): Name or ID of the annotator.
        interpretation (str): Annotator's interpretation or critique.
        tags (list of str, optional): List of tags (e.g., metaphor, ethics).
        notes (str, optional): Additional commentary.

    Returns:
        dict: Saved annotation.
    """
    try:
        record = {
            "annotator": annotator,
            "interpretation": interpretation,
            "tags": tags or [],
            "notes": notes or ""
        }
        annotations_db.setdefault(sample_id, []).append(record)
        return record
    except Exception as e:
        logging.error(f"[Annotation] Submission failed: {e}")
        return {}


def get_annotations(sample_id):
    """
    Retrieve all annotations for a given sample.

    Args:
        sample_id (str): ID of the sample or model output.

    Returns:
        list: List of annotation dicts.
    """
    try:
        return annotations_db.get(sample_id, [])
    except Exception as e:
        logging.error(f"[Annotation] Retrieval failed: {e}")
        return []
