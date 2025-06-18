from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="AgentVerse API")
app.include_router(router)
