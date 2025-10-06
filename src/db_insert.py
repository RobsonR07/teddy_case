import pandas as pd
from .db_engine import get_engine

def insert_dataframe(df: pd.DataFrame):

    """
    Insere o DataFrame filtrado na tabela 'Teddy_360.todos' do PostgreSQL.
    Executa a operação em modo transacional e exibe a quantidade de registros inseridos.
    """

    engine = get_engine()

    try:
        
        with engine.begin() as conn:
            df.to_sql(
                name="todos",
                con=conn,
                schema="Teddy_360",
                if_exists="append",
                index=False,
                method=None,
                chunksize=1000
            )

        print(f"{len(df)} registros inseridos na tabela Teddy_360.todos.")

    except Exception as e:
        print(f"Erro ao inserir DataFrame: {e}")
