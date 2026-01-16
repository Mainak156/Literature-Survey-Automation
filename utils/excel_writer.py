import pandas as pd
import os
import time

def write_excel(rows, output_path="output/literature_review.xlsx"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(rows)

    # Replace NaN with N/A (VERY IMPORTANT)
    df = df.fillna("N/A")

    try:
        df.to_excel(output_path, index=False)
    except PermissionError:
        timestamp = int(time.time())
        new_path = f"output/literature_review_{timestamp}.xlsx"
        df.to_excel(new_path, index=False)
        print(f"⚠️ File open. Saved as {new_path}")
