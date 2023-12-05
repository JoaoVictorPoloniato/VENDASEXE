import mysql.connector

def conectar_banco():
    host = "localhost"
    usuario = "root"
    senha = "123456"
    banco_de_dados = "sistema_loja_autopecas"

    conexao = mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=banco_de_dados
    )

    return conexao