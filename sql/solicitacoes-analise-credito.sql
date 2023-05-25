
-- Cria database para o fluxo de análise de crédito, se ele não existir.

CREATE DATABASE analise_credito_db;

-- Cria a tabela 'informacoes_clientes', se ela não existir.

CREATE TABLE analise_credito_db.dbo.informacoes_clientes (
    id INT IDENTITY(1,1),
    id_solicitacao VARCHAR(20) PRIMARY KEY,
    id_regional VARCHAR(20),
    id_representante VARCHAR(20),
    id_funcionario VARCHAR(20),
    cpf VARCHAR(14),
    nome VARCHAR(200),
    sexo VARCHAR(1),
    data_nascimento DATE,
    estado_civil VARCHAR(50),
    escolaridade VARCHAR(50),
    profissao VARCHAR(50),
    renda DECIMAL(18, 2),
    renda_complementar DECIMAL(18, 2),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    regiao VARCHAR(50),
    possui_outro_contrato VARCHAR(3),
    datahora_registro DATETIME DEFAULT GETDATE()
);

-- Cria a tabela 'registro_solicitacoes_kafka', se ela não existir.

CREATE TABLE analise_credito_db.dbo.registro_solicitacoes_kafka (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_solicitacao VARCHAR(20),
	kafka_consumer_id VARCHAR(50),
	kafka_offset INT,
	kafka_partition INT,
	kafka_timestamp BIGINT,
	kafka_topic VARCHAR(50),
	datahora_registro DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_solicitacao) REFERENCES informacoes_clientes(id_solicitacao)
);

-- Insere dados de cliente em 'informacoes_clientes'.

INSERT INTO analise_credito_db.dbo.informacoes_clientes
(
	id_solicitacao,
	id_regional,
	id_representante,
	id_funcionario,
	cpf,
	nome,
	sexo,
	data_nascimento,
	estado_civil,
	escolaridade,
	profissao,
	renda,
	renda_complementar,
	cidade,
	uf,
	regiao,
	possui_outro_contrato
)
VALUES (
	'${id_solicitacao}',
	'${id_regional}',
	'${id_representante}',
	'${id_funcionario}',
	'${cpf}',
	'${nome}',
	'${sexo}',
	'${data_nascimento}',
	'${estado_civil}',
	'${escolaridade}',
	'${profissao}',
	${renda},
	${renda_complementar},
	'${cidade}',
	'${uf}',
	'${regiao}',
	'${possui_outro_contrato}'
);

-- 
SELECT * FROM analise_credito_db.dbo.informacoes_clientes;

-- Insere informaçoes de registro do kafka em 'registro_solicitacoes_kafka'.

INSERT INTO analise_credito_db.dbo.registro_solicitacoes_kafka
(
	id_solicitacao,
	kafka_consumer_id,
	kafka_offset,
	kafka_partition,
	kafka_timestamp,
	kafka_topic
)
VALUES (
	'${id_solicitacao}',
	'${kafka.consumer.id}',
	${kafka.offset},
	${kafka.partition},
	${kafka.timestamp},
	'${kafka.topic}'
);


SELECT * FROM analise_credito_db.dbo.registro_solicitacoes_kafka;

--drop table analise_credito_db.dbo.registro_solicitacoes_kafka;
--drop table analise_credito_db.dbo.informacoes_clientes;



