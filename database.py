# database.py

import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, descricao TEXT, data_vencimento TEXT)")

    conexao.commit()
    conexao.close()

def adicionar_tarefa(descricao, data_vencimento):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO tarefas (descricao, data_vencimento) VALUES (?, ?)", (descricao, data_vencimento))
    
    conexao.commit()
    conexao.close()

def obter_tarefas_pendentes():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE data_vencimento >= date('now') ORDER BY data_vencimento ASC")
    tarefas = cursor.fetchall()

    conexao.close()
    return tarefas
