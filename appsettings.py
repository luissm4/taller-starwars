import os
from dotenv import load_dotenv

load_dotenv()

class AppSettings:
    """Configuración centralizada."""
    
    # URL Base de SWAPI
    SWAPI_URL = os.getenv("SWAPI_BASE_URL")
    
    # SWAPI a veces es un poco lenta, damos buen margen de espera
    TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", 15))