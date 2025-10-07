# 🧠 Teddy Case

Projeto desenvolvido como parte de um teste técnico.  
O objetivo é consumir dados de uma API pública, filtrar registros concluídos e persistir os resultados em um banco de dados PostgreSQL.

---

## 🚀 Estrutura do Projeto

```
teddy_case/
│
├── src/
│   ├── __init__.py
│   ├── api_client.py          # Consome a API e retorna os dados em DataFrame
│   ├── data_cleaner.py        # Filtra registros com completed=True
│   ├── db_engine.py           # Cria conexão e estrutura do banco de dados
│   ├── db_insert.py           # Insere o DataFrame no PostgreSQL
│   └── main.py                # Ponto de entrada do projeto
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.11 ou superior  
- PostgreSQL (local ou remoto)  
- Bibliotecas listadas em `requirements.txt`

---

## 🧰 Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/<seu-usuario>/teddy_case.git
cd teddy_case
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o script principal
```bash
python -m src.main
```

---

## 🧩 Fluxo de Execução

1. Cria o schema `Teddy_360` e a tabela `todos` no banco.  
2. Consome a API pública `https://jsonplaceholder.typicode.com/todos/`.  
3. Filtra apenas as tarefas concluídas (`completed=True`).  
4. Insere os registros no PostgreSQL.  
5. Exibe no console um exemplo de registros e o total inserido.

---

## 🗄️ Estrutura da Tabela

| Campo       | Tipo       | Descrição                             |
|--------------|------------|--------------------------------------|
| id           | SERIAL     | Identificador único do registro      |
| user_id      | INTEGER    | ID do usuário da tarefa              |
| title        | TEXT       | Título ou descrição da tarefa        |
| completed    | BOOLEAN    | Status da tarefa (True = completa)   |
| data_carga   | TIMESTAMP  | Data/hora da inserção no banco       |

---

## 🧪 Exemplo de saída no console

```
Tabela 'Teddy_360.todos' criada
Conectando a URL: https://jsonplaceholder.typicode.com/todos/
200 registros encontrados.
Foram removidos 110 registros incompletos.
Exemplo de registros completos:
    user_id  id                     title  completed
3        1   4          et porro tempora       True
7        1   8  quo adipisci enim quam ut ab       True
Total de registros: 90
✅ 90 registros inseridos na tabela Teddy_360.todos.
```

---

## 💡 Observações

- Este projeto utiliza o driver **pg8000** por compatibilidade com Windows 11.  
- As credenciais de conexão estão configuradas no arquivo `db_engine.py`.  
  Ajuste conforme o seu ambiente (usuário, senha, host e base de dados).

---

## 🧾 Licença

Este projeto é de uso livre para fins educacionais e demonstrativos.
