from sqlalchemy import create_engine, text

def get_engine():

    """
    Cria e retorna uma conexão SQLAlchemy com o banco de dados PostgreSQL.
    """

    user = "postgres"
    password = "Password123"
    host = "localhost"
    port = "5432"
    database = "datalake"

    # Windows 11 bugado com o pyscopg2 e pg8000 funciona
    connection_string = f"postgresql+pg8000://{user}:{password}@{host}:{port}/{database}"

    engine = create_engine(
        connection_string,
        pool_pre_ping=True,
        echo=False
    )
    return engine

def create_schema_and_table():

    """
    Cria o schema 'Teddy_360' e a tabela 'todos' caso ainda não existam no banco de dados.
    """

    sql = """
    CREATE SCHEMA IF NOT EXISTS "Teddy_360";

    CREATE TABLE IF NOT EXISTS "Teddy_360".todos (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,   
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
