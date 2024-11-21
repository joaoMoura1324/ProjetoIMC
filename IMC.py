import sqlite3

# Conectar ou criar a base de dados IMC.db
conexao = sqlite3.connect('IMC.db')

# Criar um cursor
cursor = conexao.cursor()

# Criar a tabela User com os campos Nome, Idade, Altura e Peso
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Idade INTEGER NOT NULL,
        Altura REAL NOT NULL,
        Peso REAL NOT NULL
    )
''')


# Função para pedir dados dos utilizadores
def criar_utilizadores():
    usuarios = []

    for i in range(5):
        print(f"\nInserir dados do utilizador {i + 1}:")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura (em metros, ex: 1.75): "))
        peso = float(input("Peso (em kg, ex: 70.5): "))
        usuarios.append((nome, idade, altura, peso))

    return usuarios


# Pedir ao utilizador para inserir 5 utilizadores
usuarios = criar_utilizadores()

# Inserir utilizadores na base de dados
cursor.executemany('''
    INSERT INTO User (Nome, Idade, Altura, Peso)
    VALUES (?, ?, ?, ?)
''', usuarios)

# Confirmar e salvar a transação
conexao.commit()


print("Utilizadores inseridos com sucesso.")

# Fechar a conexão
conexao.close()