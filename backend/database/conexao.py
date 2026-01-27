import sqlite3

conexao = sqlite3.connect('backend/database/dadospacientes.db')
cursor = conexao.cursor()

creat_table = """
 CREATE TABLE IF NOT EXISTS Pacientes (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 idade INTEGER NOT NULL,
 telefone TEXT NOT NULL UNIQUE
 ); 
 """

cursor.execute(creat_table)
conexao.commit()
conexao.close()