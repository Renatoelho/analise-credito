#!/home/user01/.virtualenvs/bin/python3

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from utils.gerador_de_mensagens import mensagem
from utils.produtor_de_mensagens import publica_mensagem


app = FastAPI()


@app.get("/healthcheck")
async def check():
    try:
        exemplo_mensagem = mensagem()
        publica_mensagem(exemplo_mensagem)
        return JSONResponse(status_code=200, content="Tudo Ok")
    except Exception as erro:
        erro = f"Ocorreu o seguinte erro no servidor: {erro}"
        return JSONResponse(status_code=500, content=erro)

@app.get("/healthcheck-motor")
async def check():
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

@app.get("/motor-analise-credito")
async def exemplo():
    try:
        resultado_analise = (
            {"status": "Adicione aqui o resultado da análise de crédito"}
        )
        return JSONResponse(status_code=200, content=resultado_analise)
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
