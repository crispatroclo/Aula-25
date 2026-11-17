import pandas as pd
import mysql.connector
from mysql.connector import Error

try:
    # Estabelece a conexão
    
    conexao = mysql.connector.connect(
        host = 'localhost', # ou o IP do servidor
        user = 'root',
        password = '',
        database = 'escola' 
    ) 

    if conexao.is_connected():
        print('Conectado com sucesso')

    # cria um cursor (objeto que permite executar comandos SQL)
    cursor = conexao.cursor()

    cursor.execute('DESCRIBE disciplinas')

    resultados = cursor.fetchall()

    print(resultados)

except Error as e:
        print(f'Error ao comectar: {e}')

finally:
    # fecha o cursos (se foi criado)
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass # se já estiver fechado ou ocorrer erro, ignore

    # fecha conexão (se foi criada e ainda está conectada)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexao encerrada.')

