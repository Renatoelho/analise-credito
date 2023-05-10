
from datetime import datetime
from random import sample

ALFABETO = "qwertyuiopasdfghjklçzxcvbnm"
NUMEROS = "0123456789"
REGIOES = [
    {"Centro-Oeste": ["DF", "GO", "MT", "MS"]},
    {"Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]},
    {"Norte": ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]},
    {"Sudeste": ["ES", "MG", "RJ", "SP"]},
    {"Sul": ["PR", "RS", "SC"]} 
]

def _regiao_mais_ufs() -> dict:
    return sample(REGIOES, 1)[0]

regiao_mais_ufs = _regiao_mais_ufs()

def id_identificacao() -> str:
    prefixo = "S"
    datahora = datetime.now().strftime("%Y%m%d%H%M%S")
    semente = "".join(sample(NUMEROS, 5))
    return f"{prefixo}{datahora}{semente}"

def regiao(regiao_mais_ufs: dict) -> str:
    for item in regiao_mais_ufs.keys():
        _ = item
    return _

def uf(regiao_mais_ufs: dict) -> str:
    for item in regiao_mais_ufs.values():
        _ = item
    _ = sample(_, 1)[0]
    return _

def id_regional(regiao: str, uf: str) -> str:
    return f"REG{regiao}{uf}".upper()

#print(id_identificacao())
#print(regiao(regiao_mais_ufs))
#print(uf(regiao_mais_ufs))

_regiao = regiao(regiao_mais_ufs)
_uf = uf(regiao_mais_ufs)
print(_regiao)
print(_uf)
print(id_regional(_regiao, _uf))

