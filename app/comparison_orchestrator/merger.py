"""
merger.py
Combines model explanations and human annotations for comparison.
"""

def merge_explanations(machine_explanation, human_annotation):
    try:
        merged = {
            "tokens": machine_explanation.get("tokens", []),
            "machine_scores": machine_explanation.get("importance", []),
            "human_feedback": human_annotation.get("comments", []),
            "divergence": compute_divergence(machine_explanation, human_annotation)
        }
        return merged
    except Exception as e:
        return {"error": str(e)}

def compute_divergence(machine, human):
    # Dummy logic: counts mismatches between explanation and annotation
    try:
        machine_tokens = set(machine.get("tokens", []))
        human_tokens = set(human.get("comments", []))
        return list(human_tokens - machine_tokens)
    except Exception as e:
        return ["Error computing divergence:", str(e)]
