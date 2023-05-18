
from typing import List

from pydantic import BaseModel


class InfoOrigem(BaseModel):
    id_solicitacao: str

class InformacoesResultadoAnalise(BaseModel):
    resultado: str
    porcentagem_aprovada: float

class InformacoesParcela(BaseModel):
    valor_parcela: float
    prazo: int
    juros: float

class OpcoesParcelas(BaseModel):
    opcoes_parcelas: List[InformacoesParcela]

class Resultado(BaseModel):
    id_resultado: str
    info_origem: InfoOrigem
    informacoes_resultado_analise: InformacoesResultadoAnalise
    opcoes_parcelas: OpcoesParcelas
