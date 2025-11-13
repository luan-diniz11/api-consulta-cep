from fastapi import APIRouter, HTTPException, status
from models.cep_models import CepCreate, CepUpdate
from database.supabase_client import supabase

router = APIRouter(
    prefix="/cep",
    tags=["CEP"]
)

# GET /cep → listar todos
@router.get("/", response_description="Lista todos os CEPs")
async def listar_ceps():
    """
    Retorna uma lista com todos os CEPs cadastrados no banco de dados.
    """
    try:
        response = supabase.table("cep").select("*").execute()
        return {
            "status": "success",
            "data": response.data,
            "total": len(response.data)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao listar CEPs: {str(e)}"
        )

# GET /cep/{cep} → buscar
@router.get("/{cep}", response_description="Detalhes de um CEP específico")
async def buscar_cep(cep: str):
    """
    Retorna os detalhes de um CEP específico.
    """
    try:
        response = supabase.table("cep").select("*").eq("cep", cep).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"CEP {cep} não encontrado"
            )
        
        return {
            "status": "success",
            "data": response.data[0]
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar CEP: {str(e)}"
        )

# POST /cep → criar
@router.post("/", response_description="CEP criado com sucesso", status_code=status.HTTP_201_CREATED)
async def criar_cep(cep_data: CepCreate):
    """
    Cria um novo registro de CEP no banco de dados.
    """
    try:
        # Verificar se CEP já existe
        response = supabase.table("cep").select("*").eq("cep", cep_data.cep).execute()
        
        if response.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"CEP {cep_data.cep} já existe"
            )
        
        # Inserir novo CEP
        novo_cep = {
            "cep": cep_data.cep,
            "rua": cep_data.rua,
            "bairro": cep_data.bairro,
            "cidade": cep_data.cidade,
            "estado": cep_data.estado
        }
        
        response = supabase.table("cep").insert(novo_cep).execute()
        
        return {
            "status": "success",
            "message": "CEP criado com sucesso",
            "data": response.data[0]
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar CEP: {str(e)}"
        )

# PUT /cep/{cep} → atualizar
@router.put("/{cep}", response_description="CEP atualizado com sucesso")
async def atualizar_cep(cep: str, cep_update: CepUpdate):
    """
    Atualiza os dados de um CEP existente.
    """
    try:
        # Verificar se CEP existe
        response = supabase.table("cep").select("*").eq("cep", cep).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"CEP {cep} não encontrado"
            )
        
        # Preparar dados para atualização (apenas campos não None)
        dados_atualizacao = {}
        if cep_update.rua is not None:
            dados_atualizacao["rua"] = cep_update.rua
        if cep_update.bairro is not None:
            dados_atualizacao["bairro"] = cep_update.bairro
        if cep_update.cidade is not None:
            dados_atualizacao["cidade"] = cep_update.cidade
        if cep_update.estado is not None:
            dados_atualizacao["estado"] = cep_update.estado
        
        if not dados_atualizacao:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Nenhum campo para atualizar"
            )
        
        # Atualizar CEP
        response = supabase.table("cep").update(dados_atualizacao).eq("cep", cep).execute()
        
        return {
            "status": "success",
            "message": "CEP atualizado com sucesso",
            "data": response.data[0]
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar CEP: {str(e)}"
        )

# DELETE /cep/{cep} → excluir
@router.delete("/{cep}", status_code=status.HTTP_204_NO_CONTENT, response_description="CEP excluído com sucesso")
async def excluir_cep(cep: str):
    """
    Exclui um CEP do banco de dados.
    """
    try:
        # Verificar se CEP existe
        response = supabase.table("cep").select("*").eq("cep", cep).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"CEP {cep} não encontrado"
            )
        
        # Excluir CEP
        supabase.table("cep").delete().eq("cep", cep).execute()
        
        return None
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao excluir CEP: {str(e)}"
        )
