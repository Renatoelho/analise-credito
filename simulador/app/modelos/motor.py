
from pydantic import BaseModel

from mensagem import InformacoesRegional
from mensagem import InformacoesCliente


class Motor(BaseModel):
    id_solicitacao: str
    informacoes_regional: InformacoesRegional
    informacoes_cliente: InformacoesCliente
