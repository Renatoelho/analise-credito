
from os import getenv

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


query = """
SELECT 	DISTINCT
    t2.id_solicitacao,
    REVERSE(SUBSTRING(REVERSE(t2.id_regional), 1, 2))  uf,
    t2.regiao,
    t3.resultado,
    t1.datahora_solicitacao,
    t4.datahora_entrega,
    DATEDIFF(
        second,
        t1.datahora_solicitacao,
        t4.datahora_entrega
    ) tempo_analise_segundos,
    DATEDIFF(
        millisecond,
        t1.datahora_solicitacao,
        t4.datahora_entrega
    ) tempo_analise_milissegundos
FROM analise_credito_db.dbo.registro_solicitacoes_analise_credito t1
INNER JOIN analise_credito_db.dbo.registro_informacoes_cliente t2
ON t1.id_solicitacao = t2.id_solicitacao
INNER JOIN analise_credito_db.dbo.registro_resultados_analise_credito t3
ON t1.id_solicitacao = t3.id_solicitacao
INNER JOIN analise_credito_db.dbo.registro_entregas_analise_credito t4
ON t1.id_solicitacao = t4.id_solicitacao
"""


def dados() -> pd.DataFrame:
    url_conexao = (
        "mssql+pymssql://"
        f"{getenv('SQLSERVER_USUARIO')}:"
        f"{getenv('SQLSERVER_SENHA')}@"
        f"{getenv('SQLSERVER_SERVER')}:"
        f"{getenv('SQLSERVER_PORTA')}/"
        f"{getenv('SQLSERVER_DB')}"
    )
    engine = create_engine(url_conexao)
    return pd.read_sql(query, engine)
