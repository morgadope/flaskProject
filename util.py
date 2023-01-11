import os
import sqlite3 as sql


def database_conn():
    connect = sql.connect('meu banco de dados')
    connect.cursor()
    # Verifica se o banco de dados já existe
    if not os.path.exists('meu_banco_de_dados.db'):
        # Cria o banco de dados
        connect = sql.connect('meu_banco_de_dados.db')
    else:
        # Conecta ao banco de dados existente
        connect = sql.connect('meu_banco_de_dados.db')
    connect.commit()
    connect.close()

    return "conexão realiazado com sucesso"
