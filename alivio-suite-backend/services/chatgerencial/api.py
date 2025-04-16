from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir solicitudes desde cualquier origen (útil para Vercel frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    else:
        return { "respuesta": "Esta es una respuesta simulada de la API." }

