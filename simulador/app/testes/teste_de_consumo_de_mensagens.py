#!/home/user01/.virtualenvs/bin/python3

import os
import json

from dotenv import load_dotenv
from kafka import KafkaConsumer


load_dotenv()

kafka_topico = os.getenv("KAFKA_TOPICO", None)
kafka_grupo_id = os.getenv("KAFKA_GRUPO_ID", None)
kafka_porta = os.getenv("KAFKA_PORTA", None)
kafka_servidor = os.getenv("KAFKA_SERVIDOR", None)

consumidor = KafkaConsumer(
    kafka_topico,
    group_id=kafka_grupo_id,
    bootstrap_servers=[f"{kafka_servidor}:{kafka_porta}"],
    auto_offset_reset="latest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for mensagem in consumidor:
    evento_recuperado = mensagem.value
    print(evento_recuperado)
    print("*"*50)
