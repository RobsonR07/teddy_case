import pandas as pd

def filter_completed_records(df: pd.DataFrame) -> pd.DataFrame:

    initial_count = len(df)
    df_filtered = df[df["completed"] == True].copy()
    final_count = len(df_filtered)

    removed = initial_count - final_count
    print(f"Foram removidos {removed} registros incmpletos.")
    return df_filtered
