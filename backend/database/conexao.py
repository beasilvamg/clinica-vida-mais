import sqlite3

db_conexao = 'backend/database/dadospacientes.db'

def criar_tabela():
    with sqlite3.connect(db_conexao) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                telefone TEXT NOT NULL UNIQUE
            ); 
        """)
        conn.commit()
criar_tabela()


def db_inserir(Paciente):
    with sqlite3.connect(db_conexao) as conn:
        cursor = conn.cursor() 
        sql = """ INSERT INTO Pacientes (nome, idade, telefone) VALUES (?, ?, ?)"""
        cursor.execute(sql, (Paciente.nome, Paciente.idade, Paciente.telefone))
        conn.commit()
    