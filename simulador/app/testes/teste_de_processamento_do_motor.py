
from typing import Union

import requests


url = "http://localhost:8888/motor-analise-credito"

payload = {
    "id_solicitacao":"S2023051621095197012",
    "informacoes_regional":{
        "id_regional":"REG-SUL-RS",
        "regiao":"Sul",
        "uf":"RS",
        "id_representante":"RS3560728",
        "id_funcionario":"FRS7402598",
        "cidade":"Yndhoawxd"
    },
    "informacoes_cliente":{
        "cpf":"673.743.624-32",
        "nome":"Nome Cxbyypjq Ywkpvzatb Qqtgz Dejxmtecc",
        "sexo":"M",
        "data_nascimento":"1997-11-23",
        "estado_civil":"CASADO (A)",
        "valor_solicitado":125500.0,
        "escolaridade":"Ensino Superior",
        "renda":13700.0,
        "renda_complementar":0.0,
        "profissao":"Prefeito",
        "possui_outro_contrato":"NAO"
    }
}

#payload = {}

resposta = requests.post(url, json=payload)

def teste_envio_payload() -> dict:
    try:
        if resposta.status_code == 200:
            payload_modificado = resposta.json()
            return payload_modificado
        else:
            return {"Erro na solicitação:", resposta.status_code}
    except Exception as erro:
        return {"Erro na solicitação:", erro}
    
if __name__ == "__main__":
    print(teste_envio_payload())