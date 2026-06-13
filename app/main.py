from fastapi import FastAPI
from app.incidents.incidents_router import IncidentsRouter

app = FastAPI(
    title="Inference Service",
    version="1.0.0"
)
incidents_router = IncidentsRouter()

app.include_router(incidents_router.router)