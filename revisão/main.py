import pymysql
from sqlalchemy import create_engine, text

usuario = 'sql812.main-hosting.eu'
senha = 'u274908554_718A'
host = 'INbd718A'
porta = ''
banco_de_dados = 'u274908554_718A'



connection = pymysql.connect(
    host=usuario,
    user=senha,
    password=host,
    database= banco_de_dados
)

uri = f"mysql+pymysql : //{usuario}: {senha}@{host}:{porta}/{banco_de_dados}"

engine = create_engine(uri)

query = text("SELECT * FROM ew_aluno")
with engine.connect() as connection:
    resul = connection.execute(query)
    
    for row in resul:
        print(row)
        
query = text(f"""
             INSERT INTO ew_aluno(
                 nome,
                 data_nascimento,
                 serie)VALUES(Davi,18/06/2002,3 ano);
             )
             """)

with engine.connect() as connection:
    cursor = connection.execute(query)
    connection.commit()


"-----------------------------------"

import psycopg2

connection = psycopg2.connect(
    host = '',
    user = '',
    password = '',
    dbname = ''  
)

with connection.cursor() as cursor:
    query = text(f"""
             INSERT INTO ew_aluno(
                 nome,
                 data_nascimento,
                 serie)VALUES(Davi,18/06/2002,3 ano);
             )
             """)
    
    
    cursor.execute(query)