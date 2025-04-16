# BACKEND - FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción cambia esto al dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "").lower()

    if "producto top" in question:
        return { "respuesta": "Ortodoncia Premium es el producto top en ventas." }
    elif "cancelaciones" in question:
        return { "respuesta": "La tasa de cancelación actual es del 12%." }
    elif "ventas" in question:
        return { "respuesta": "Las ventas han aumentado un 25% respecto al mes anterior." }
    else:
        return { "respuesta": "Esta es una respuesta simulada desde el backend API." }
