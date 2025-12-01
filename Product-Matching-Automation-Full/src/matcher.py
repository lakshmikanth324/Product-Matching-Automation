
import pandas as pd
from difflib import SequenceMatcher
from utils import clean_text

def match_products(src_file, dest_file):
    src = pd.read_csv(src_file)
    dest = pd.read_csv(dest_file)

    results = []

    for _, s in src.iterrows():
        best = None
        best_score = 0

        for _, d in dest.iterrows():
            score = SequenceMatcher(None, clean_text(s['title']), clean_text(d['title'])).ratio()

            if score > best_score:
                best_score = score
                best = d

        results.append({
            "source_id": s["id"],
            "destination_id": best["id"] if best is not None else None,
            "similarity": best_score
        })

    return results

if __name__ == "__main__":
    matches = match_products("../data/source.csv", "../data/destination.csv")
    print(matches)
