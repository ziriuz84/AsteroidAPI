from fastapi import FastAPI, HTTPException
from app.lib.scheduling import weather
import models

app = FastAPI(
    title="AsteroidAPI",
    version="0.0.1",
    description="Simple api to request data for asteroids in better format",
)


@app.get("/")
def root() -> str:
    return "home"


@app.get("/api/v1/scheduling")
def scheduling():
    return {"section": "scheduling", "test": "test"}

