
import string
from os import getenv
from random import choice
from random import sample
from datetime import date
from datetime import datetime
from datetime import timedelta

from modelos.mensagem import Mensagem
from amostras_de_dados import REGIOES
from amostras_de_dados import NUMEROS
from amostras_de_dados import ESTADO_CIVIL
from amostras_de_dados import NIVEL_ENSINO
from amostras_de_dados import VALOR_RENDA
from amostras_de_dados import PROFISSOES
from amostras_de_dados import VALOR_SOLICITADO
from amostras_de_dados import VALOR_RENDA_COMPLEMENTAR


def _regiao_mais_ufs(regiao: str) -> dict:
    for item in REGIOES:
        if regiao.strip() == list(item.keys())[0].strip():
            return item


def id_identificacao() -> str:
    prefixo = "S"
    datahora = datetime.now().strftime("%Y%m%d%H%M%S")
    semente = "".join(sample(NUMEROS, 5))
    return f"{prefixo}{datahora}{semente}"


regiao_extra = list(choice(REGIOES).keys())[0]
regiao_mais_ufs = _regiao_mais_ufs(getenv("REGIAO", regiao_extra))


def regiao(regiao_mais_ufs: dict) -> str:
    return list(regiao_mais_ufs.keys())[0]


def uf(regiao_mais_ufs: dict) -> str:
    return sample(list(regiao_mais_ufs.values())[0], 1)[0]


def id_regional(regiao: str, uf: str) -> str:
    return f"REG-{regiao}-{uf}".upper()


def id_Representante(uf: str) -> str:
    semente = "".join(sample(NUMEROS, 7))
    return f"{uf}{semente}"


def id_funcionario(uf: str) -> str:
    semente = "".join(sample(NUMEROS, 7))
    return f"F{uf}{semente}"


def cidade() -> str:
    number_of_strings = 1
    for _ in range(number_of_strings):
        len_string = choice(range(7, 10))
        _Cidade = (
            "".join(choice(string.ascii_letters) for _ in range(len_string))
        )
    return _Cidade.title()


def nome() -> str:
    listNomes = ["Nome"]
    number_of_strings = choice(range(2, 5))
    for _ in range(number_of_strings):
        lstr = choice(range(3, 10))
        (
            listNomes
            .append("".join(choice(string.ascii_letters) for _ in range(lstr)))
        )
    _Nome = ""
    for item in listNomes:
        _Nome = f"{_Nome} {item}"
    return _Nome.title().strip()


def gera_cpf() -> str:
    CPF = "".join(choice(string.digits) for _ in range(11))
    return CPF


def mascara_cpf(cpf: str) -> str:
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def sexo() -> str:
    return choice(["F", "M", "O"])


def data_nascimento() -> str:
    idade = choice(range(18, 60))
    dias = choice(range(1, 365))
    hoje = date.today()
    td = timedelta(((idade * 365)*-1)+dias)
    data_nasc = hoje + td
    return data_nasc.strftime("%Y-%m-%d")


def estado_civil() -> str:
    return choice(ESTADO_CIVIL)


def valor_solicitado() -> float:
    return float(f"{choice(VALOR_SOLICITADO)}.00")


def nivel_ensino() -> str:
    return choice(NIVEL_ENSINO)


def valor_renda() -> float:
    return float(f"{choice(VALOR_RENDA)}.00")


def valor_renda_complementar() -> float:
    return float(f"{choice(VALOR_RENDA_COMPLEMENTAR)}.00")


def profissao() -> str:
    return choice(PROFISSOES)


def possui_outro_contrato() -> str:
    return choice(["SIM", "NAO"])


def mensagem() -> dict:
    _regiao = regiao(regiao_mais_ufs)
    _uf = uf(regiao_mais_ufs)

    _informacoes_regional = (
        {
            "id_regional": id_regional(_regiao, _uf),
            "regiao": _regiao,
            "uf": _uf,
            "id_representante": id_Representante(_uf),
            "id_funcionario": id_funcionario(_uf),
            "cidade": cidade()
        }
    )

    _informacoes_cliente = (
        {
            "cpf": mascara_cpf(gera_cpf()),
            "nome": nome(),
            "sexo": sexo(),
            "data_nascimento": data_nascimento(),
            "estado_civil": estado_civil(),
            "valor_solicitado": valor_solicitado(),
            "escolaridade": nivel_ensino(),
            "renda": valor_renda(),
            "renda_complementar": valor_renda_complementar(),
            "profissao": profissao(),
            "possui_outro_contrato": possui_outro_contrato()
        }
    )

    _conteudo_mensagem = (
        {
            "id_solicitacao": id_identificacao(),
            "informacoes_regional": _informacoes_regional,
            "informacoes_cliente": _informacoes_cliente,
        }
    )

    return Mensagem(**_conteudo_mensagem).dict()


if __name__ == "__main__":
    _regiao = regiao(regiao_mais_ufs)
    _uf = uf(regiao_mais_ufs)

    print("Informações da solicitação")
    print(f"ID_Solicitacao: {id_identificacao()}")

    print("Informações da regional")
    print(f"ID_Regional: {id_regional(_regiao, _uf)}")
    print(f"Regiao: {_regiao}")
    print(f"UF: {_uf}")
    print(f"id_Representante: {id_Representante(_uf)}")
    print(f"id_Funcionario: {id_funcionario(_uf)}")
    print(f"Cidade: {cidade()}")

    print("Informações do cliente")
    print(f"CPF: {mascara_cpf(gera_cpf())}")
    print(f"Nome: {nome()}")
    print(f"Sexo: {sexo()}")
    print(f"Data de nascimento: {data_nascimento()}")
    print(f"Estado civíl: {estado_civil()}")
    print(f"Valor solicitado: {valor_solicitado()}")
    print(f"Nivel de ensino: {nivel_ensino()}")
    print(f"Valor da renda: {valor_renda()}")
    print(f"Valor da renda complementar: {valor_renda_complementar()}")
    print(f"Profissao: {profissao()}")
    print(f"Possui outro contrato: {possui_outro_contrato()}")
