# Análise de crédito em tempo real

![Análise de crédito em tempo real](docs/analise-credito-em-tempo-real.drawio.png)

Este projeto, desenvolvido por nós, [Renato Coelho](https://www.linkedin.com/in/renatoelho/) e [Gyan Lucas](https://www.linkedin.com/in/gyan-almeida-2102a8177), tem como objetivo ***conceitual*** e ***educativo*** demonstrar como seria uma solução de análise de crédito utilizando ferramentas open source e proprietárias em conjunto para resolver uma determinada hipótese.

Nesse contexto, estamos propondo uma solução para processar análise de crédito "quase" em ***tempo real*** a partir de eventos gerados pelas regionais de uma hipotética grande empresa de concessão de crédito. A financeira XYZ S.A. tem abrangência em todo o território nacional e concentra todas as operações de análise de crédito em sua matriz, da qual recebe as solicitações de suas regionais, onde existem dezenas de representantes que comercializam seus produtos de crédito. Por alguma regra de negócio, cada uma das cinco regionais centraliza todas as solicitações de ***análise e concessão de crédito*** referente a sua regional. A solução proposta aqui captura os eventos de solicitação de crédito que são enviados para uma ferramenta de mensageria mantida pela matriz, e cada regional é responsável por enviar o evento para um tópico que, além de armazenar todos os metadados do processamento, inclui o processamento, a devolutiva dos resultados e o registro da confirmação da devolutiva.

O evento de origem passa por um "motor" de ***concessão de crédito*** que define se a solicitação será aceita ou não, e se aceita, qual será o percentual aprovado e três opções de parcelamento. O motor apresentado aqui aprovará ou reprovará a solicitação de forma aleatória, uma vez que a proposta é apresentar e implementar o fluxo. Todas as informações referentes aos dados e metadados serão armazenadas em um banco de dados relacional para futuras análises, com um backup na nuvem para resguardar essas informações. Tudo isso será orquestrado por uma ferramenta que flexibiliza as implementações e dá velocidade ao desenvolvimento e a visualização e monitoramento será feita via um notebook interativo.

Ao final, o evento de resultado da análise será devolvido via ferramenta de mensageria para sua regional de origem, ficando a partir daí a regional responsável por dar continuidade a todo o processo.

As ferramentas que vamos utilizar aqui são o Apache Kafka para gerenciar as mensagens/eventos postados, tanto para as solicitações quanto para os resultados das análises de crédito. O Apache Nifi será responsável por estruturar todo o fluxo de análise de crédito e orquestrar o recebimento, processamento e devolutiva. Além disso, temos o Apache Nifi Registry, que faz backup dos flows desenvolvidos no Apache Nifi. Para armazenar os metadados e dados dos processamentos, temos uma instância de SQL Server para análises mais avançadas. Para o armazenamento de dados em nuvem, optamos por utilizar o MinIO em vez do S3 para desenvolvimento local, pois ele nos oferece a flexibilidade e o controle necessários para testar diferentes cenários e configurações localmente.

Além disso, utilizaremos o Jupyter Notebook como uma das principais ferramentas de desenvolvimento e documentação. O Jupyter Notebook nos permite escrever e executar código de forma interativa, facilitando o processo de ***análise e monitoramento*** da nossa solução de análise de crédito.

# Responsáveis pelo projeto

***Renato coelho***

Sou Analista de Big Data em uma grande multinacional de seguros. Tenho experiência na automatização de processos e estruturação de pipelines de dados. Também atuo como professor de tecnologia, compartilhando meu conhecimento em Linux, Data Lake, Python, Docker, Apache Nifi, Shell Script, SQL e expressões regulares. 

[Linkedin do Renato](https://www.linkedin.com/in/renatoelho/)

***Gyan Lucas*** 

Sou Analista de Processos com foco em dados em uma empresa de consórcios. Com especialização em Data Science, atuo na gestão e extração dos dados bem como na geração de insights de valor a empresa. Extensa experiência com SQL, Power BI, Power automate, Power Apps e VBA.

[Linkedin do Gyan](https://www.linkedin.com/in/gyan-almeida-2102a8177)


# Tópicos

+ [Tecnologias](#tecnologias)
+ [Requisitos](#requisitos) 
+ [Apresentação em vídeo](#apresentacao-video)
+ [Implementação](#implementacao)
+ [Referências](#referencias)


# Tecnologias<a name="tecnologias"></a>

### Apache Nifi

***Apache Nifi*** é uma plataforma open source que permite o gerenciamento e processamento de dados em ***tempo real*** de forma simples e escalável. Ele foi desenvolvido para lidar com fluxos de dados em ambientes distribuídos, oferecendo uma interface gráfica amigável para o desenvolvimento de pipelines de dados. O Apache Nifi suporta diversos tipos de fontes de dados, incluindo sistemas de arquivos, bancos de dados, serviços web, fluxos de dados, e muitos outros. Além disso, ele oferece integração com outras ferramentas de Big Data, como Apache Hadoop, Spark, e Hive.


### Apache Nifi Registry

O ***Apache Nifi Registry*** é um subprojeto do Apache Nifi que fornece um repositório central para gerenciamento de ***versionamento***, controle de acesso e colaboração para flows do Apache Nifi. Isso permite que as organizações gerenciem seus flows de forma mais eficiente e compartilhem seu trabalho com outras pessoas de maneira controlada e segura.


### Apache Kafka/Zookeeper

***Apache Kafka*** e o ***Apache ZooKeeper*** são componentes fundamentais para o processamento e gerenciamento de fluxos de dados em tempo real. Enquanto o Kafka lida com a ***ingestão***, armazenamento e ***entrega confiável*** das mensagens, o ZooKeeper garante a coordenação e a estabilidade do cluster Kafka. Juntos, eles oferecem uma solução robusta e escalável para aplicações de streaming de dados.


### MinIO/S3 

***MinIO*** é uma solução de ***armazenamento em nuvem*** de código aberto e escalável, compatível com a API ***S3***. Ele oferece flexibilidade e controle, permitindo a organização dos dados em buckets e objetos, além de suportar criptografia. Por sua vez, o Amazon S3 é um serviço líder de armazenamento em nuvem, altamente escalável e durável, com recursos avançados como controle de acesso granular, replicação entre regiões e integração nativa com outros serviços da AWS. Ambas as ferramentas têm seus pontos fortes e podem ser selecionadas com base nas necessidades específicas de armazenamento e integração de um projeto.


### SQL Server

O ***SQL Server*** é um sistema de gerenciamento de banco de dados relacional desenvolvido pela Microsoft, oferecendo uma plataforma completa para armazenar, consultar e gerenciar dados. Ele suporta a linguagem SQL e fornece recursos avançados, como transações ACID, controle de acesso e integridade referencial. O SQL Server também inclui ferramentas de ***administração*** e ***monitoramento*** para facilitar a gestão e o desempenho do banco de dados. Sua confiabilidade, segurança e escalabilidade o tornam uma escolha popular em empresas de diversos tamanhos.


### Jupyter notebook

O ***Jupyter Notebook*** é uma aplicação web que permite a criação de ***documentos interativos*** contendo código, texto e visualizações. É usado por cientistas de dados, pesquisadores e desenvolvedores para explorar e analisar dados, prototipar algoritmos e comunicar resultados. Com suporte a várias linguagens de programação, como Python e R, o Jupyter Notebook permite a execução de código em células individuais, tornando o processo de desenvolvimento iterativo e facilitando a experimentação. Além disso, oferece recursos de visualização de dados e integração com bibliotecas populares de ciência de dados. Sua interface intuitiva e flexível o torna uma ferramenta versátil e amplamente utilizada na comunidade de análise de dados.


### Docker

***Docker*** é uma plataforma de virtualização de aplicativos que permite que os aplicativos sejam executados em ***ambientes isolados*** e portáteis chamados contêineres. Cada contêiner inclui todos os componentes necessários para executar um aplicativo, como código, bibliotecas, dependências e configurações. Isso permite que os desenvolvedores criem, gerenciem e implantem aplicativos de forma mais rápida e consistente em diferentes ambientes.


### Docker Compose

O ***Docker Compose*** é uma ferramenta que permite que os usuários definam e executem aplicativos Docker compostos por ***vários contêineres***. Ele usa um arquivo YAML para definir as configurações de cada contêiner e suas dependências. Isso facilita o gerenciamento de aplicativos complexos que requerem vários contêineres, permitindo que eles sejam gerenciados como uma unidade.


# Requisitos<a name="requisitos"></a>

+ Ubuntu 20.04 (Host)

+ Docker 23.0.3 (Host)

+ Docker-Compose 1.25.0 (Host)

+ Git 2.25.1 ou superior (Host)


# Apresentação em vídeo<a name="apresentacao-video"></a>

Em desenvolvimento...


# Implementação<a name="implementacao"></a>

### Credenciais de acesso às ferramentas

+ Apache Kafka

|Parâmetro         |Valor         |
|------------------|--------------| 
|Broker interno/porta|kafka:9002    |
|Broker externo/porta|localhost:9004|

+ Apache Nifi

|Parâmetro         |Valor         |
|------------------|--------------|
|Usuário           |nifi          |
|Senha             |mkYUQBJ9BBhc38RWa1p3E76xUR1rhYGR|
|URL externa       |https://localhost:8443/nifi/|

+ Apache Nifi Registry

|Parâmetro         |Valor         |
|------------------|--------------|
|URL interna       |http://nifi-registry:18080/|
|URL externa       |http://localhost:18080/nifi-registry/|

+ SQL Server

|Parâmetro         |Valor         |
|------------------|--------------|
|Usuário           |SA|
|Senha             |b90bee3b63bf33fa9901f92e|
|Host interno      |sqlserver|
|Host externo      |localhost|
|Porta             |1433|

+ MinIO

|Parâmetro         |Valor         |
|------------------|--------------|
|Usuário           |admin|
|Senha             |eO3RNPcKgWInlzPJuI08|
|URL externa       |http://localhost:9001|
|Access Key        |Definir manualmente\*\*|
|Secret Key        |Definir manualmente\*\*|

> ***Observação:*** A diferença entre Broker/Host/URL interno ou externo é que os internos são utilizados dentro da rede onde as aplicações estão sendo executadas, permitindo a comunicação entre elas. Já os externos são destinados aos usuários para que possam acessar as ferramentas a partir de seus computadores, onde as aplicações estão sendo executadas.

### Clonando o repositório do projeto

```bash
git clone https://github.com/Renatoelho/analise-credito.git ‘analise-credito’
```

> ***Observação:*** Será criado um diretório chamado "análise-crédito" em seu computador, onde estarão todos os arquivos necessários para a implementação do projeto.

### Construindo a imagem base das regionais

Essa imagem é responsável por simular cada uma das regionais existentes no projeto. Quando ativadas, as postagens dos eventos que alimentarão o fluxo de análise de crédito serão iniciadas imediatamente.

```bash
cd analise-credito/simulador/
```

```bash
docker build -f dockerfile -t imagem-base-simulador:0.0.1 .
```

```bash
cd ..
```

> ***Observação***: Serão ativados 5 containers, cada um deles com um healthcheck ativo que monitorará a saúde de cada um. Para visualizar, utilize o comando ```docker ps -a``` e verifique a coluna status. 


### Ativando todos os serviços do projeto

Aqui estamos utilizando o docker-compose e a partir do arquivo ```docker-compose.yaml``` teremos um cluster com todas as tecnologias mencionadas acima, prontas para iniciar a análise de crédito em tempo real. No entanto, antes disso, faremos algumas configurações. 

Execute o seguinte comando para iniciar as aplicações:

```bash
docker-compose -f docker-compose.yaml --compatibility up -d
```


### Ajustando as permissões do volumes docker

Para manter os dados das aplicações que estamos utilizando, será criado o diretório ```volumes```. Nele, serão armazenados todos os dados do Apache NiFi, Apache NiFi Registry e SQL Server. As demais aplicações têm seus volumes gerenciados diretamente pelo Docker. Portanto, se após a ativação dos serviços você notar algum problema nas aplicações mencionadas aqui, cujos dados estão armazenados no diretório ```volumes```, faça o down de todos os serviços ativos, altere as permissões do diretório ```volumes``` e, em seguida, inicie novamente todos os serviços. 

Execute a seguinte sequência de comandos:

+ Baixado os serviços

```bash
docker-compose -f docker-compose.yaml --compatibility down
```

+ Alterando as permissões do diretório volumes

```bash
chmod -R 777 volumes/
```

+ Ativando todos os serviços novamente

```bash
docker-compose -f docker-compose.yaml --compatibility up -d
```

Se tudo der certo, você verá todos os serviços em execução por meio do comando:

```bash
docker ps -a
```

# Referências<a name="referencias"></a>

Apache/Nifi, ***Docker Hub***. Disponível em: <https://hub.docker.com/r/apache/nifi>. Acesso em: 19 abr. 2023.

Volumes, ***Docker Docs***. Disponível em: <https://docs.docker.com/storage/volumes/>. Acesso em: 24 abr. 2023.

NiFi System Administrator’s Guide, ***Apache NiFi***. Disponível em: <https://nifi.apache.org/docs/nifi-docs/html/administration-guide.html>. Acesso em: 22 abr. 2023.

apache/nifi-registry, ***Docker Hub***. Disponível em: <https://hub.docker.com/r/apache/nifi-registry>. Acesso em: 22 abr. 2023.

Getting Started with Apache NiFi Registry, ***Apache NiFi Registry***. Disponível em: <https://nifi.apache.org/docs/nifi-registry-docs/index.html>. Acesso em: 22 abr. 2023.

How to build a data lake from scratch - Part 1: The setup, ***Victor Seifert***. Disponível em: <https://towardsdatascience.com/how-to-build-a-data-lake-from-scratch-part-1-the-setup-34ea1665a06e>. acesso em: 19 abr. 2023.

How to build a data lake from scratch - Part 2: Connecting the components, ***Victor Seifert***. Disponível em: <https://medium.com/towards-data-science/how-to-build-a-data-lake-from-scratch-part-2-connecting-the-components-1bc659cb3f4f>. acesso em: 23 abr. 2023.

How to Successfully Implement A Healthcheck In Docker Compose, ***Linuxhint***. Disponível em: <https://linuxhint.com/how-to-successfully-implement-healthcheck-in-docker-compose/>. Acesso em: 24 abr. 2023.

Expression Language Guide, ***Apache NiFi Expression Language Guide***. Disponível em: <https://nifi.apache.org/docs/nifi-docs/>. Acesso em: 26 abr. 2023.

Install Docker Desktop on Ubuntu, ***docs.docker.com***. Disponível em: <https://docs.docker.com/desktop/install/ubuntu/>. Acesso em: 15 de abr. 2023.

The Compose file, ***docs.docker.com***. Disponível em: <https://docs.docker.com/compose/compose-file/03-compose-file/>. Acesso em: 15 de abr. 2023.

Início Rápido: Executar imagens de contêiner do SQL Server Linux com o Docker, ***learn.microsoft.com***. Disponível em: <https://learn.microsoft.com/pt-br/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&tabs=ubuntu&pivots=cs1-bash>. Acesso em: 15 de abr. 2023.

bitnami/minio, ***Docker Hub***. Disponível em: <https://hub.docker.com/r/bitnami/minio>. Acesso em: 18 mai. 2023.

High Performance Object Storage for AI, ***MinIO***. Disponível em: <https://min.io/>. Acesso em: 18 mai. 2023.

bitnami/kafka, ***Docker Hub***. Disponível em: <https://hub.docker.com/r/bitnami/kafka>. Acesso em: 18 mai. 2023.

INTRODUCTION, ***Apache Kafka***. Disponível em: <https://min.io/>. Acesso em: 18 mai. 2023.

bitnami/zookeeper, ***Docker Hub***. Disponível em: <https://hub.docker.com/r/bitnami/zookeeper>. Acesso em: 19 mai. 2023.

Welcome to Apache ZooKeeper, ***Apache Zookeeper***. Disponível em: <https://min.io/>. Acesso em: 21 mai. 2023.

Project Jupyter Documentation, ***Jupyter***. Disponível em: <https://docs.jupyter.org/en/latest/>. Acesso em: 05 jun. 2023.

Service unit configuration, ***systemd.service***. Disponível em: <https://www.freedesktop.org/software/systemd/man/systemd.service.html>. Acesso em: 05 jun. 2023.
