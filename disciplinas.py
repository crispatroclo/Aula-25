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

    # descreve as colunas para ajudar na inserção dos dados
    #cursor.execute('DESCRIBE disciplinas')

    # buscar e traz todas as linhas de resultado que o banco de dados gerou após um cursor.execute()
    #resultados = cursor.fetchall()
    #print(resultados)

    # dados da tabela disciplinas:
    # 'id_disciplina', 'int(11)', 'NO', 'PRI', None, 'auto_increment'
    # 'id_curso', 'int(11)', 'NO', 'MUL', None, ''
    # 'nome_disciplina', 'varchar(100)', 'YES', '', None, ''
    # 'carga_horaria', 'int(11)', 'YES', '', None, ''

    # Define a query de INSERT usando placeholders (%s)
    #sql = 'INSERT INTO disciplinas (id_disciplina, id_curso, nome_disciplina, carga_horaria) VALUES (%s, %s, %s, %s)'
    
    # Valores qye serão substituidos nos placeholders, na mesm aordem
    #valores = [
        #(101, 1, 'introdução_1', 16), 
        #(102, 1, 'pratica_1', 32), 
        #(201, 2, 'introdução_2', 16), 
        #(202, 2, 'pratica_2', 32), 
        #(301, 3, 'introdução_3', 16),
        #(302, 3, 'pratica_3', 32)
    #]

    # Executa insert no banco, substituindo os %s pelos valores em 'valores'
    # o conector trata automaticamente aspas, datas e acentos
    #cursor.executemany(sql, valores)

    # confirma (grava) as alterações da transação no banco
    # sem commit(), o INSERT ficaria só na memoria e seria descartado
    #conexao.commit()

    # Mostra o ID (AUTO_INCREMENR) gerado na ultima inserção
    # print(f'Linha inserida. ID gerado: {cursor.lastrowid}')

    # executa uma consulta
    cursor.execute('SELECT * FROM disciplinas', conexao)

    # busca os resultados
    resultados = cursor.fetchall()
    print(resultados)

    #df = pd.DataFrame(resultados) # traz o banco sem o nome das colunas
    df = pd.read_sql('SELECT * FROM disciplinas', conexao)
    #df.to_csv("sql.csv", index=False)

    print(df)


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

