
import os
import json

from dotenv import load_dotenv
from kafka import KafkaProducer


load_dotenv()


def publica_evento(json_evento: dict) -> bool:
    mensagem = json.dumps(f"{json_evento}").encode("utf-8")
    kafka_topico = os.getenv("KAFKA_TOPICO", None)
    kafka_porta = os.getenv("KAFKA_PORTA", None)
    kafka_servidor = os.getenv("KAFKA_SERVIDOR", None)
    try:
        with KafkaProducer(
            bootstrap_servers=[f"{kafka_servidor}:{kafka_porta}"]
        ) as produtor:
            produtor.send(kafka_topico, value=mensagem)
        return True
    except Exception as _:
        return False
