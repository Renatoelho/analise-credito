
-- # Cria database para o fluxo de análise de crédito

CREATE DATABASE analise_credito_db;

-- # Cria a tabela 'registro_informacoes_cliente'

CREATE TABLE analise_credito_db.dbo.registro_informacoes_cliente (
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

-- SELECT * FROM analise_credito_db.dbo.registro_informacoes_cliente order by datahora_registro DESC ;

-- # Cria a tabela 'registro_solicitacoes_analise_credito'

CREATE TABLE analise_credito_db.dbo.registro_solicitacoes_analise_credito (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_solicitacao VARCHAR(20),
	kafka_consumer_id VARCHAR(50),
	kafka_offset INT,
	kafka_partition INT,
	kafka_timestamp DATETIME,
	kafka_topic VARCHAR(50),
	datahora_registro DATETIME DEFAULT GETDATE()
);

-- SELECT * FROM analise_credito_db.dbo.registro_solicitacoes_analise_credito;

-- # Cria a tabela 'registro_resultados_analise_credito'

CREATE TABLE analise_credito_db.dbo.registro_resultados_analise_credito (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_resultado VARCHAR(20),
    id_solicitacao VARCHAR(20),
    resultado VARCHAR(20),
    porcentagem_aprovada  DECIMAL(18, 2),
    juros  DECIMAL(18, 2),
    prazo INT,
    valor_parcela  DECIMAL(18, 2),
	datahora_registro DATETIME DEFAULT GETDATE()
);


-- SELECT * FROM analise_credito_db.dbo.registro_resultados_analise_credito;


-- # Cria a tabela 'registro_entregas_analise_credito'

CREATE TABLE analise_credito_db.dbo.registro_entregas_analise_credito (
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

-- SELECT * FROM analise_credito_db.dbo.registro_entregas_analise_credito;


-- # Tempo para analisar o crédito

SELECT 	DISTINCT
		t2.id_solicitacao,
		t2.regiao,
		t3.resultado,
		t1.kafka_timestamp, 
		t4.kafka_timestamp,
		DATEDIFF(second, t1.kafka_timestamp , t4.kafka_timestamp) tempo_analise_segundos
FROM analise_credito_db.dbo.registro_solicitacoes_analise_credito t1
INNER JOIN analise_credito_db.dbo.registro_informacoes_cliente t2
ON t1.id_solicitacao = t2.id_solicitacao
INNER JOIN analise_credito_db.dbo.registro_resultados_analise_credito t3
ON t1.id_solicitacao = t3.id_solicitacao
INNER JOIN analise_credito_db.dbo.registro_entregas_analise_credito t4
ON t1.id_solicitacao = t4.id_solicitacao;
-- WHERE t1.id_solicitacao = 'S2023060221042819378';





