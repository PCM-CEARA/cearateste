# create_db.py
import sqlite3

# Conecta ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('veiculos.db')
cursor = conn.cursor()

# Cria a tabela de veículos
cursor.execute('''
CREATE TABLE IF NOT EXISTS veiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    preco TEXT NOT NULL,
    imagem TEXT
)
''')

# Salva e fecha a conexão
conn.commit()
conn.close()
print("Banco de dados criado com sucesso!")
