# 🏠 API Consulta CEP

API simples pra gerenciar CEPs. CRUD completo com FastAPI + Supabase.

---

## 🚀 Instalação

```bash
# Clone
git clone https://github.com/luan-diniz11/api-consulta-cep.git
cd api-consulta-cep

# Ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Dependências
pip install -r requirements.txt
```

Crie um `.env`:
```properties
SUPABASE_URL=sua-url
SUPABASE_KEY=sua-chave
```

---

## ▶️ Rodar

```bash
python -m uvicorn main:app --reload
```

Acessa em: **http://localhost:8000/docs**

---

## 📡 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/cep` | Lista todos |
| GET | `/cep/{cep}` | Busca um |
| POST | `/cep` | Cria novo |
| PUT | `/cep/{cep}` | Atualiza |
| DELETE | `/cep/{cep}` | Deleta |

---

## 🌐 Deploy

**Link da API em produção:**
🔗 https://api-consulta-cep.onrender.com

**Documentação interativa:**
📚 https://api-consulta-cep.onrender.com/docs

---

## 📝 Exemplo

**Criar:**
```bash
curl -X POST http://localhost:8000/cep \
  -H "Content-Type: application/json" \
  -d '{
    "cep":"01310100",
    "rua":"Av Paulista",
    "bairro":"Bela Vista",
    "cidade":"São Paulo",
    "estado":"SP"
  }'
```

**Resposta:**
```json
{
  "status": "success",
  "message": "CEP criado com sucesso",
  "data": {
    "cep": "01310100",
    "rua": "Av Paulista",
    "bairro": "Bela Vista",
    "cidade": "São Paulo",
    "estado": "SP"
  }
}
```

---

## 🛠️ Tech

- FastAPI
- Uvicorn
- Supabase
- Pydantic
- Python 3.10+

---

## 📧 Contato

**GitHub:** [@luan-diniz11](https://github.com/luan-diniz11)

---

## 📄 Licença

MIT License
