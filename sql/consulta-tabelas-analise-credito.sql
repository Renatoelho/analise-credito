
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






