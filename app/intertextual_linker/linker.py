"""
linker.py
Handles intertextual linking between model outputs and reference corpora.
"""

import difflib

def find_intertextual_links(output_text, reference_texts):
    try:
        links = []
        for ref in reference_texts:
            matcher = difflib.SequenceMatcher(None, output_text, ref)
            if matcher.ratio() > 0.6:  # Threshold for a meaningful match
                links.append({
                    "reference": ref,
                    "similarity": matcher.ratio()
                })
        return links
    except Exception as e:
        return {"error": str(e)}
