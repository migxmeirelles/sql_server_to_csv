import pyodbc
import pandas as pd

conexao = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=*************;"
    "DATABASE=DW;"
    "UID=**********;"
    "PWD=**********;"
)

conn = pyodbc.connect(conexao)
query = "SELECT * FROM CLIENTES;" 

df = pd.read_sql(query, conn)

conn.close() 


df.rename(columns={'CD_AGENCIA': 'AGENCIA', 'NM_CLIENTE': 'NOME', 'NR_CPF': 'CPF', 'NR_CONTA': 'CONTA', 'ST_ATIVO': 'ATIVO'}, inplace=True)


df = df.drop_duplicates() 
df['ATIVO'] = df['ATIVO'].replace({'S': 'Sim', 'N': 'Não'}) 
df['NOME'] = df['NOME'].str.upper() 
df['NOME'] = df['NOME'].str.strip() 

print(df)
df.to_csv('CLIENTES.csv', encoding='utf-8', index=False)