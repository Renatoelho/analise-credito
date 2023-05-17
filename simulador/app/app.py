#!/home/user01/.virtualenvs/bin/python3

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from modelos.modelo_mensagem import Payload
from utils.gerador_de_mensagens import mensagem
from utils.produtor_de_mensagens import publica_mensagem


app = FastAPI()


@app.get("/healthcheck-regionais")
async def check_regionais():
    try:
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
async def motor(payload: Payload):
    try:
        payload.informacoes_cliente.cpf = "999.999.999-99"
        payload.informacoes_cliente.nome = "teste teste teste teste..."
        return JSONResponse(status_code=200, content=payload.dict())
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
