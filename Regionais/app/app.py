#!/home/regionais/.virtualenvs/bin/python3

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from utils.gerador_de_mensagens import mensagem
from utils.produtor_de_mensagens import publica_mensagem


app = FastAPI()


@app.get("/healthcheck")
async def check():
    try:
        exemplo_mensagem = mensagem()
        print(exemplo_mensagem)
        if not publica_mensagem(exemplo_mensagem):
             raise ValueError("Erro")
        return JSONResponse(status_code=200, content="Tudo Ok")
    except Exception as _:
        erro = f"Ocorreu o seguinte erro no servidor: {erro}"
        return JSONResponse(status_code=500, content=erro)

@app.get("/exemplo")
async def exemplo():
    try:
        exemplo = mensagem()
        return JSONResponse(status_code=200, content=exemplo)
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
