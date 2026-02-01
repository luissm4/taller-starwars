import httpx
from fastapi import APIRouter
from services.swapi_service import StarWarsService
from DTOs.swapi_dtos import CharacterResponseDTO

router = APIRouter(prefix="/api/starwars", tags=["Star Wars"])

@router.get("/characters/{name}", response_model=CharacterResponseDTO)
async def find_character(name: str):
    """
    Busca un personaje de Star Wars y devuelve sus datos básicos.
    """
    async with httpx.AsyncClient() as http_client:
        service = StarWarsService()
        return await service.get_character(name, http_client)