from src.api_client import APIClient

def main():
    BASE_URL = "https://jsonplaceholder.typicode.com/todos/"

    client = APIClient(BASE_URL)
    df = client.fetch_todos()

    print("Dados obtidos:")
    print(df.head())

if __name__ == "__main__":
    main()
