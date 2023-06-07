
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
	id_consumer_kafka VARCHAR(50),
	posicao_mensagem_kafka INT,
	particao_mensagem_kafka INT,
	datahora_solicitacao DATETIME2,
	topico_kafka VARCHAR(50),
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


-- SELECT * FROM analise_credito_db.dbo.registro_resultados_analise_credito ORDER BY 9 DESC, 2; 

-- SELECT * FROM analise_credito_db.dbo.registro_resultados_analise_credito WHERE id_resultado in('R2023060705545739581', '');


-- # Cria a tabela 'registro_entregas_analise_credito'

CREATE TABLE analise_credito_db.dbo.registro_entregas_analise_credito (
	id INT IDENTITY(1,1) PRIMARY KEY,
	id_resultado VARCHAR(20),
	id_solicitacao VARCHAR(20),
	tamanho_mensagem INT,
	status_retorno_motor INT,
	mensagem_retorno_motor VARCHAR(20),
	confirmacao_entrega VARCHAR(10),
	datahora_entrega DATETIME2,
	datahora_registro DATETIME DEFAULT GETDATE()
);

-- SELECT * FROM analise_credito_db.dbo.registro_entregas_analise_credito;


-- # Tempo para analisar o crédito

SELECT 	DISTINCT
	t2.id_solicitacao,
	REVERSE(SUBSTRING(REVERSE(t2.id_regional), 1, 2))  uf,
	t2.regiao,
	t3.resultado,
	t1.datahora_solicitacao , 
	t4.datahora_entrega ,
	DATEDIFF(second, t1.datahora_solicitacao , t4.datahora_entrega) tempo_analise_segundos,
	DATEDIFF(millisecond, t1.datahora_solicitacao , t4.datahora_entrega) tempo_analise_milissegundos
FROM analise_credito_db.dbo.registro_solicitacoes_analise_credito t1
INNER JOIN analise_credito_db.dbo.registro_informacoes_cliente t2
ON t1.id_solicitacao = t2.id_solicitacao
INNER JOIN analise_credito_db.dbo.registro_resultados_analise_credito t3
ON t1.id_solicitacao = t3.id_solicitacao
INNER JOIN analise_credito_db.dbo.registro_entregas_analise_credito t4
ON t1.id_solicitacao = t4.id_solicitacao;

-- # Quantidade de clientes

SELECT count(1) qtd FROM analise_credito_db.dbo.registro_informacoes_cliente;


-- # Quantidade de solicitações de análise

SELECT count(1) qtd FROM analise_credito_db.dbo.registro_solicitacoes_analise_credito;

-- # Quantidade de solicitações analisadas (por: resultado)

SELECT
	resultado,
	count(DISTINCT(id_solicitacao)) qtd
FROM analise_credito_db.dbo.registro_resultados_analise_credito
GROUP BY resultado;

-- # Quantidade de confirmação das entregas das análises (por: confirmação do motor e entrega)

SELECT
	mensagem_retorno_motor,
	confirmacao_entrega,
	count(DISTINCT(id_solicitacao)) qtd
FROM analise_credito_db.dbo.registro_entregas_analise_credito
GROUP BY mensagem_retorno_motor, confirmacao_entrega;






