#!/home/user01/.virtualenvs/bin/python3

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from modelos.motor import Motor
from modelos.resultado import Resultado
from modelos.resultado import OpcoesParcelas
from utils.gerador_de_mensagens import mensagem
from utils.produtor_de_mensagens import publica_mensagem
from utils.estrutura_modelagem_sql import execute_query


app = FastAPI()

@app.get("/healthcheck-regionais")
async def check_regionais():
    try:
        execute_query()
        exemplo_mensagem = mensagem()
        publica_mensagem(exemplo_mensagem)
        return JSONResponse(status_code=200, content="Tudo Ok")
    except Exception as erro:
        erro = f"Ocorreu o seguinte erro no servidor: {erro}"
        return JSONResponse(status_code=500, content=erro)

@app.get("/healthcheck-motor")
async def check_motor():
    try:
        return JSONResponse(status_code=200, content="Tudo Ok")
    except Exception as erro:
        erro = f"Ocorreu o seguinte erro no servidor: {erro}"
        return JSONResponse(status_code=500, content=erro)

@app.get("/exemplo")
async def exemplo():
    try:
        return JSONResponse(status_code=200, content=mensagem())
    except Exception as erro:
        erro = f"Ocorreu o seguinte erro no servidor: {erro}"
        return JSONResponse(status_code=500, content=erro)

@app.post("/motor-analise-credito")
async def motor_analise_credito(motor: Motor):
    try:
        _info_origem = {"id_solicitacao": motor.id_solicitacao}
        _informacoes_resultado_analise = {
            "resultado": "True", #Criar função
            "porcentagem_aprovada": 90.0 #Criar função
        }
        _opcoes_parcelas = [
            {
                "valor_parcela": 1000.0, #Criar função
                "prazo": 120, #Criar função
                "juros": 0.0 #Criar função
            },
            {
                "valor_parcela": 900.0, ##Criar função
                "prazo": 110, #Criar função
                "juros": 0.8 #Criar função
            },
            {
                "valor_parcela": 500.0, #Criar função
                "prazo": 150, #Criar função
                "juros": 0.6 #Criar função
            }
        ]
        _estrutura_resultado = {
            "id_resultado": "R2023051621095197012", #Criar função
            "info_origem": _info_origem,
            "informacoes_resultado_analise": _informacoes_resultado_analise,
            "opcoes_parcelas": OpcoesParcelas(opcoes_parcelas=_opcoes_parcelas)             
        }

        estrutura_resultado = Resultado(**_estrutura_resultado)

        return JSONResponse(status_code=200, content=estrutura_resultado.dict())
    except Exception as erro:
        erro = f"Ocorreu o seguinte erro no servidor: {erro}"
        return JSONResponse(status_code=500, content=erro)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=8888,
        log_level="info",
        reload=True
    )
