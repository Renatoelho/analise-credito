
from random import choice
from random import sample
from datetime import datetime

from modelos.motor import Motor
from modelos.resultado import OpcoesParcelas
from amostras_de_dados import NUMEROS


def processamento_motor(motor: Motor) -> dict:

    def _resultado() -> str:
        return choice(["APROVADO", "REPROVADO"])

    def _porcentagem_aprovada(resultado_analise: float) -> float:
        if resultado_analise == "APROVADO":
            return round(choice(range(70, 100, 5)), 2)
        else:
            return 0.00

    resultado_analise = _resultado()

    porcentagem_aprovada = _porcentagem_aprovada(resultado_analise)

    def _id_resultado() -> str:
        prefixo = "R"
        datahora = datetime.now().strftime("%Y%m%d%H%M%S")
        semente = "".join(sample(NUMEROS, 5))
        return f"{prefixo}{datahora}{semente}"

    valor_solicitado = motor.informacoes_cliente.valor_solicitado

    valor_aprovado = (
        round(
            valor_solicitado * (porcentagem_aprovada / 100),
            2
        )
    )

    _info_origem = {"id_solicitacao": motor.id_solicitacao}
    _informacoes_resultado_analise = {
        "resultado": resultado_analise,
        "porcentagem_aprovada": porcentagem_aprovada
    }

    if resultado_analise == "APROVADO":
        _opcoes_parcelas = [
            {
                "valor_parcela": round(((valor_aprovado / 120) * 1.0019), 2),
                "prazo": 120,
                "juros": 0.19
            },
            {
                "valor_parcela": round(((valor_aprovado / 150) * 1.0035), 2),
                "prazo": 150,
                "juros": 0.35
            },
            {
                "valor_parcela": round(((valor_aprovado / 200) * 1.0065), 2),
                "prazo": 200,
                "juros": 0.65
            }
        ]
    else:
        _opcoes_parcelas = [
            {
                "valor_parcela": 0.0,
                "prazo": 0,
                "juros": 0.0
            }
        ]
    _estrutura_resultado = {
        "id_resultado": _id_resultado(),
        "info_origem": _info_origem,
        "informacoes_resultado_analise": _informacoes_resultado_analise,
        "opcoes_parcelas": OpcoesParcelas(opcoes_parcelas=_opcoes_parcelas)
    }

    return _estrutura_resultado
