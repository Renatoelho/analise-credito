
from os import getenv
from time import sleep
from typing import Union

from pymssql import connect


query_verifica_database_existe = """
SELECT COUNT(1)
FROM sys.databases
WHERE name = 'analise_credito_db';
"""

query_cria_database = """
CREATE DATABASE analise_credito_db;
"""

query_cria_tabela1 = """
CREATE TABLE analise_credito_db.dbo.informacoes_clientes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_solicitacao VARCHAR(20),
    id_regional VARCHAR(20),
    id_representante VARCHAR(20),
    id_funcionario VARCHAR(20),
    cpf VARCHAR(14),
    nome VARCHAR(200),
    sexo VARCHAR(1),
    data_nascimento DATE,
    estado_civil VARCHAR(50),
    escolaridade VARCHAR(50),
    profissao VARCHAR(100),
    renda DECIMAL(18, 2),
    renda_complementar DECIMAL(18, 2),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    regiao VARCHAR(50),
    possui_outro_contrato VARCHAR(3),
    datahora_registro DATETIME DEFAULT GETDATE()
);
"""

query_cria_tabela2 = """
CREATE TABLE analise_credito_db.dbo.registro_solicitacoes_kafka (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_solicitacao VARCHAR(20),
	kafka_consumer_id VARCHAR(50),
	kafka_offset INT,
	kafka_partition INT,
	kafka_timestamp DATETIME,
	kafka_topic VARCHAR(50),
	datahora_registro DATETIME DEFAULT GETDATE()
);
"""

query_cria_tabela3 = """
CREATE TABLE analise_credito_db.dbo.resultados_analise_credito (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_resultado VARCHAR(20),
    id_solicitacao VARCHAR(20),
    resultado VARCHAR(10),
    porcentagem_aprovada  DECIMAL(18, 2),
    juros  DECIMAL(18, 2),
    prazo INT,
    valor_parcela  DECIMAL(18, 2),
	datahora_registro DATETIME DEFAULT GETDATE()
);
"""

query_cria_tabela4 = """
CREATE TABLE analise_credito_db.dbo.registro_entrega_analise_credito (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_resultado VARCHAR(20),
    id_solicitacao VARCHAR(20),
    tamanho_mensagem INT,
    status_retorno_motor INT,
    mensagem_retorno_motor VARCHAR(20),
    kafka_consumer_id VARCHAR(100),
    kafka_committed VARCHAR(20),
    kafka_offset INT,
    kafka_partition INT,
    kafka_timestamp DATETIME,
    kafka_topic_origin VARCHAR(100),
	datahora_registro DATETIME DEFAULT GETDATE()
);
"""

def _execute_query(query: str, ddl: bool = False) -> Union[list, bool]:
    try:
        with connect(
            server=getenv('SQLSERVER_SERVER'),
            user=getenv('SQLSERVER_USUARIO'),
            password=getenv('SQLSERVER_SENHA'),
            database=getenv('SQLSERVER_DB'),
            autocommit=ddl
        ) as conexao:
            cursor = conexao.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
    except Exception as _:
        if ddl:
            return True
        else:
            return False

def execute_query() -> bool:
    try:
        teste_database = _execute_query(query_verifica_database_existe)[0][0]
        if teste_database == 0:
            _execute_query(query_cria_database, True)
            sleep(3)
            _execute_query(query_cria_tabela1, True)
            sleep(3)
            _execute_query(query_cria_tabela2, True)
            sleep(3)
            _execute_query(query_cria_tabela3, True)
            sleep(3)
            _execute_query(query_cria_tabela4, True)
        return True
    except Exception as _:
        return False        
