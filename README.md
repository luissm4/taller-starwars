# Star Wars API   
**Documentación del Contrato**

---

## Descripción General

### ¿Qué hace la API?
Esta aplicación consume la **Star Wars API (SWAPI)** para buscar y obtener información detallada sobre personajes del universo de Star Wars.  
La aplicación actúa como un **API Gateway**, simplificando la respuesta original, filtrando datos innecesarios y entregando un formato limpio al cliente final.

### ¿Qué información devuelve?
- **Nombre del personaje**
- **Características físicas** (altura, peso, género)
- **Año de nacimiento** (cronología de Star Wars)
- **Planeta de origen** (URL del recurso)
- **Participación en películas** (conteo total)

### ¿Para qué sirve?
- Consultar datos rápidos sin manejar paginación de SWAPI  
- Integración en aplicaciones front-end  
- Ejemplo educativo de consumo de APIs externas con arquitectura en capas  

---

## Endpoints Externos Utilizados

### 1. People Resource (Búsqueda de Personajes)

| Campo | Descripción |
|------|-------------|
| **URL del endpoint** | `https://swapi.dev/api/people/` |
| **Método HTTP** | `GET` |
| **Documentación oficial** | https://swapi.dev/documentation#people |

#### Parámetros Requeridos (Query Params)

| Parámetro | Tipo | Requerido | Descripción |
|----------|------|-----------|-------------|
| `search` | string | Sí | Nombre o parte del nombre del personaje (ej: luke, vader) |

#### Ejemplo de Petición Externa

```http
GET https://swapi.dev/api/people/?search=luke
```

#### Ejemplo de Respuesta Exitosa (JSON Crudo de SWAPI)

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "Luke Skywalker",
      "height": "172",
      "mass": "77",
      "hair_color": "blond",
      "skin_color": "fair",
      "eye_color": "blue",
      "birth_year": "19BBY",
      "gender": "male",
      "homeworld": "https://swapi.dev/api/planets/1/",
      "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/6/"
      ],
      "created": "2014-12-09T13:50:51.644000Z",
      "edited": "2014-12-20T21:17:56.891000Z",
      "url": "https://swapi.dev/api/people/1/"
    }
  ]
}
```

#### Descripción de Campos Importantes (Entrantes)

| Campo | Tipo | Descripción |
|-----|------|-------------|
| `results` | array | Lista de coincidencias |
| `name` | string | Nombre del personaje |
| `height` | string | Altura en cm |
| `mass` | string | Peso en kg |
| `films` | array | URLs de películas |

---

## Endpoint de Nuestra API Local

### Buscar Personaje

| Campo | Descripción |
|----|-------------|
| **URL** | `http://localhost:8000/api/starwars/characters/{name}` |
| **Método HTTP** | `GET` |

#### Ejemplo de Petición

```http
GET http://localhost:8000/api/starwars/characters/luke
```

#### Ejemplo de Respuesta Exitosa (DTO Limpio)

```json
{
  "name": "Luke Skywalker",
  "height": "172",
  "mass": "77",
  "gender": "male",
  "birth_year": "19BBY",
  "homeworld_url": "https://swapi.dev/api/planets/1/",
  "film_count": 4
}
```

#### Campos de Respuesta

| Campo | Tipo | Descripción |
|-----|------|-------------|
| `name` | string | Nombre completo |
| `height` | string | Altura |
| `mass` | string | Peso |
| `gender` | string | Género |
| `birth_year` | string | Año de nacimiento |
| `homeworld_url` | string | Planeta de origen |
| `film_count` | int | Total de películas |

---

## Manejo de Errores

| Código HTTP | Significado | Causa |
|-----------|------------|------|
| 404 | Not Found | Personaje no existe |
| 500 | Internal Server Error | Error inesperado |
| 504 | Gateway Timeout | Timeout con SWAPI |

#### Ejemplo de Error (Personaje No Encontrado)

```http
GET http://localhost:8000/api/starwars/characters/batman
```

```json
{
  "detail": "No se encontró ningún personaje con el nombre 'batman'."
}
```

---

## Configuración Requerida

### Variables de Entorno (.env)

```env
SWAPI_BASE_URL=https://swapi.dev/api
TIMEOUT_SECONDS=15
```

---

## Recursos Adicionales
- SWAPI: https://swapi.dev  
- HTTPX (Python Requests)  
- FastAPI Documentation  

---

## Autor
Desarrollado por: **[Tu Nombre Aquí]**  
Fecha: **Enero 2026**

---

## Licencia
Proyecto de uso **educativo**.
