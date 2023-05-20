# Análise de crédito em tempo real

![Análise de Crédito em Tempo Real](simulador/app/docs/analise-credito-em-tempo-real.drawio.png)

# Implementação

### Requisitos para implementação

- Ubuntu 20.04 (Host)

- Docker 23.0.3 (Host)

- Docker-Compose 1.25.0 (Host)

- Git 2.25.1 ou superior (Host)

### Clonando o repositório para iniciar a implementação

```bash
git clone https://github.com/Renatoelho/analise-credito.git "analise-credito"
```

```bash
cd analise-credito/
```


### Fazendo o build da imagem que simula as regionais e o motor de análise de crédito

```bash
cd simulador/
```

```bash
docker build -f dockerfile -t imagem-base-simulador:0.0.1 .
```


### Ativando todos os serviços do fluxo

```bash
cd ..
```

```bash
docker-compose -f docker-compose.yaml --compatibility up -d
```

Ajustar permissões, pois o contâiner Apache Nifi registry é non-root

Deixe o docker-compose criar o diretório para os volumes e depois altere as permissões.

```bash
sudo chmod -R 777 volumes/
```

> ***IMPORTANTE:*** No primeiro start dos serviços, pode ocorrer um erro no serviço '***nifi-registry***' se a permissão de acesso ao volume criado for negada. Nesse caso, desative os serviços (***docker-compose -f docker-compose.yaml --compatibility down***) e ***altere as permissões do volume***. Use o comando '***sudo chmod -R 777 volumes/nifi_registry/***' e, em seguida, suba novamente os serviços. Tudo deve funcionar corretamente.


# Criando senhas pelo terminal

```bash
openssl rand -hex 16
```

# Verificando os serviços (contâiners)

```bash
docker ps --format "{{.ID}}\t{{.Names}}\t{{.Status}}" | sort -k2
```

```SQL
SELECT * FROM analise_credito_db.dbo.exemplo;
```

***Em Desenvolvimento...***


Criando tópico: kafka-console-producer.sh --bootstrap-server 127.0.0.1:9094 --topic solicitacoes_regionais

Listando tópicos: kafka-topics.sh --list --bootstrap-server localhost:9094

Listando mensagens do tópico: kafka-console-consumer.sh --bootstrap-server localhost:9094 --topic solicitacoes_regionais --from-beginning


https://rmoff.net/2018/08/02/kafka-listeners-explained/

https://hub.docker.com/r/bitnami/kafka


https://hub.docker.com/_/microsoft-mssql-server?tab=description

https://learn.microsoft.com/pt-br/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver16 