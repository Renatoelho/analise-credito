
from utils.gerador_de_evento import evento
from utils.publica_evento_no_kafka import publica_evento

# export PYTHONPATH=/..../analise-credito/Regionais/utils

exemplo_evento = evento()
print(type(exemplo_evento))
print(exemplo_evento)
teste = publica_evento(exemplo_evento)
