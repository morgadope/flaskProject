import mysql.connector
import os

HOSTMANE = os.environ['HOSTNAME']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']


# Connect to the database
def database_conn():
    connection = mysql.connector.connect(
        host=HOSTMANE,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )
    connection.cursor()
    # Verifica se o banco de dados já existe
    if not os.path.exists('meu_banco_de_dados.db'):
        # Cria o banco de dados
        connection = connection.connect('meu_banco_de_dados.db')
    else:
        # Conecta ao banco de dados existente
        connection = connection.connect('meu_banco_de_dados.db')
    connection.commit()
    connection.close()

    return "conexão realiazado com sucesso"
