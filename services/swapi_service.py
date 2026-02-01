import httpx
from fastapi import HTTPException
from clients.swapi_client import StarWarsClient
from DTOs.swapi_dtos import CharacterResponseDTO

class StarWarsService:
    """Lógica de negocio para procesar datos de Star Wars."""

    def __init__(self):
        self.client = StarWarsClient()

    async def get_character(self, name: str, http_client: httpx.AsyncClient) -> CharacterResponseDTO:
        # 1. Llamar al cliente
        raw_response = await self.client.search_person(name, http_client)

        # 2. Validar lógica de negocio
        # SWAPI devuelve: { "count": 0, "results": [] } si no encuentra nada
        results = raw_response.get("results", [])
        
        if not results:
            raise HTTPException(
                status_code=404, 
                detail=f"No se encontró ningún personaje con el nombre '{name}'."
            )
        
        # Tomamos el primer resultado (la mejor coincidencia)
        character_data = results[0]

        # 3. Mapeo a DTO
        # Aquí transformamos los datos crudos a nuestro formato limpio
        return CharacterResponseDTO(
            name=character_data.get("name"),
            height=character_data.get("height", "unknown"),
            mass=character_data.get("mass", "unknown"),
            gender=character_data.get("gender", "unknown"),
            birth_year=character_data.get("birth_year", "unknown"),
            homeworld_url=character_data.get("homeworld"),
            # Lógica extra: contamos cuántas películas hay en la lista
            film_count=len(character_data.get("films", []))
        )