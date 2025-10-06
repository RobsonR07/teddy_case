import pandas as pd

def filter_completed_records(df: pd.DataFrame) -> pd.DataFrame:

    """
    Filtra apenas os registros com 'completed=True' no DataFrame.
    Renomeia a coluna 'userId' para 'user_id' e exibe a quantidade de registros removidos.
    """

    initial_count = len(df)
    df_filtered = df[df["completed"] == True].copy()
    final_count = len(df_filtered)
    df_filtered = df_filtered.rename(columns={"userId": "user_id"})


    removed = initial_count - final_count
    print(f"Foram removidos {removed} registros incompletos.")
    return df_filtered
