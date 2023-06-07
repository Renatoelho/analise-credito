
from pydantic import BaseModel


class InformacoesRegional(BaseModel):
    id_regional: str
    regiao: str
    uf: str
    id_representante: str
    id_funcionario: str
    cidade: str


class InformacoesCliente(BaseModel):
    cpf: str
    nome: str
    sexo: str
    data_nascimento: str
    estado_civil: str
    valor_solicitado: float
    escolaridade: str
    renda: float
    renda_complementar: float
    profissao: str
    possui_outro_contrato: str


class Mensagem(BaseModel):
    id_solicitacao: str
    informacoes_regional: InformacoesRegional
    informacoes_cliente: InformacoesCliente
