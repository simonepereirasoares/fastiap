from fastapi import FastAPI
from .database import engine  # Importando o engine do módulo database

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Aqui você pode criar todas as tabelas no banco de dados
    import myapp.models  # Importa modelos para garantir que as tabelas sejam criadas
    myapp.models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
