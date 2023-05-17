from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="AsteroidAPI",
    version="0.0.1",
    description="Simple api to request data for asteroids in better format",
)
