import httpx
from fastapi import HTTPException
from appsettings import AppSettings

class StarWarsClient:
    """Cliente HTTP para interactuar con swapi.dev"""

    async def search_person(self, name: str, http_client: httpx.AsyncClient) -> dict:
        """
        Busca personajes por nombre en SWAPI.
        Retorna el JSON completo de la respuesta (que incluye 'count' y 'results').
        """
        url = f"{AppSettings.SWAPI_URL}/people/"
        
        # SWAPI usa query param para buscar: /people/?search=luke
        params = {"search": name}

        try:
            response = await http_client.get(
                url,
                params=params,
                timeout=AppSettings.TIMEOUT_SECONDS
            )
        except httpx.ReadTimeout:
            raise HTTPException(status_code=504, detail="La API de Star Wars tardó demasiado en responder.")

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, 
                detail="Error al comunicar con SWAPI."
            )

        return response.json()