
-- Cria database para o fluxo de análise de crédito

CREATE DATABASE analise_credito_db;

-- Cria a tabela 'informacoes_clientes'

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

-- SELECT * FROM analise_credito_db.dbo.informacoes_clientes order by datahora_registro DESC ;

-- Cria a tabela 'registro_solicitacoes_kafka'

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

-- SELECT * FROM analise_credito_db.dbo.registro_solicitacoes_kafka;

-- Cria a tabela 'resultados_analise_credito'

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


-- SELECT * FROM analise_credito_db.dbo.resultados_analise_credito;


-- Cria a tabela 'registro_entrega_analise_credito'

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

-- SELECT * FROM analise_credito_db.dbo.registro_entrega_analise_credito;
