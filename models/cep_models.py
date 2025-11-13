from pydantic import BaseModel

class CepCreate(BaseModel):
    cep: str
    rua: str
    bairro: str
    cidade: str
    estado: str

class CepUpdate(BaseModel):
    rua: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    estado: str | None = None
