import requests
import pandas as pd

class APIClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_todos(self) -> pd.DataFrame:

        print(f"Conectando a URL: {self.base_url}")
        response = requests.get(self.base_url, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Erro ao acessar API. Status: {response.status_code}")

        data = response.json()

        df = pd.DataFrame(data)
        print(f"{len(df)} registros encontrados.")

        return df
