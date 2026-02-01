from fastapi import FastAPI
from controllers.swapi_controller import router as swapi_router

app = FastAPI(
    title="Star Wars API Adapter",
    description="API educativa que consume SWAPI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "May the Force be with you", 
        "docs": "/docs",
        "example": "/api/starwars/characters/luke"
    }

# Registramos el router
app.include_router(swapi_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)