from src.api_client import APIClient
from src.data_cleaner import filter_completed_records

def main():
    BASE_URL = "https://jsonplaceholder.typicode.com/todos/"

    client = APIClient(BASE_URL)
    df = client.fetch_todos()

    if not df.empty:
        df_filtered = filter_completed_records(df)
        print("Exemplo de registros completos:")
        print(df_filtered.head())
        print(f"Total de registros: {len(df_filtered)}")

if __name__ == "__main__":
    main()
