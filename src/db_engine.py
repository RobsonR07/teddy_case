from sqlalchemy import create_engine, text

def get_engine():
    user = "postgres"
    password = "Password123"
    host = "localhost"
    port = "5432"
    database = "datalake"

    # Utilização do pg8000 para evitar bugs do Windows
    connection_string = f"postgresql+pg8000://{user}:{password}@{host}:{port}/{database}"

    engine = create_engine(
        connection_string,
        pool_pre_ping=True,
        echo=False
    )
    return engine

def create_schema_and_table():

    sql = """
    CREATE SCHEMA IF NOT EXISTS "Teddy_360";

    CREATE TABLE IF NOT EXISTS "Teddy_360".todos (
        userId INTEGER NOT NULL,
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL,
        data_carga TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text(sql))
        conn.commit()
    print("Tabela 'Teddy_360.todos' criada")
