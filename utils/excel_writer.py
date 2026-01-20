import pandas as pd
import os
import time

def write_excel(rows, output_path="output/literature_review.xlsx"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(rows)

    try:
        df.to_excel(output_path, index=False)
    except PermissionError:
        ts = int(time.time())
        new_path = f"output/literature_review_{ts}.xlsx"
        df.to_excel(new_path, index=False)
