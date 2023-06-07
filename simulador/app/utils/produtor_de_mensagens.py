
import os
import json

from dotenv import load_dotenv
from kafka import KafkaProducer


load_dotenv()


def publica_mensagem(json_mensagem: dict) -> bool:
    try:
        mensagem = (
            json.dumps(json_mensagem, ensure_ascii=False)
            .encode("utf-8")
        )
        kafka_topico = os.getenv("KAFKA_TOPICO", None)
        kafka_porta = os.getenv("KAFKA_PORTA", None)
        kafka_servidor = os.getenv("KAFKA_SERVIDOR", None)
        produtor = KafkaProducer(
            bootstrap_servers=f"{kafka_servidor}:{kafka_porta}"
        )
        produtor.send(kafka_topico, value=mensagem)
        return True
    except Exception as _:
        _ = _
        return False
