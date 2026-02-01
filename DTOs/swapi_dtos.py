from pydantic import BaseModel
from typing import Optional

class CharacterResponseDTO(BaseModel):
    """Modelo limpio para devolver al cliente."""
    name: str
    height: str       # Lo dejamos como str porque a veces viene "unknown"
    mass: str         # Peso
    gender: str
    birth_year: str   # Ej: "19BBY"
    homeworld_url: str # URL del planeta de origen
    film_count: int   # Calcularemos esto contando la lista de películas