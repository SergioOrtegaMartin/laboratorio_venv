from fastapi import FastAPI

app = FastAPI()

# Endpoint raíz
@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo desde FastAPI!"}

# Endpoint de ejemplo con parámetro
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola, {nombre}!"}