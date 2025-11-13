from fastapi import FastAPI
from src.routes.cep_routes import router as cep_router

app = FastAPI(
    title="API Consulta CEP",
    description="API para consulta e gerenciamento de CEPs",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Rota raiz da API"""
    return {
        "message": "Bem-vindo à API Consulta CEP",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "listar_todos": "GET /cep",
            "buscar": "GET /cep/{cep}",
            "criar": "POST /cep",
            "atualizar": "PUT /cep/{cep}",
            "excluir": "DELETE /cep/{cep}"
        }
    }

app.include_router(cep_router)
