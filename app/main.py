from fastapi import FastAPI, HTTPException

from app.libraries.scheduling import (
    neocp_confirmation,
    object_ephemeris,
    observing_target_list,
    sun_moon_ephemeris,
    twilight_times,
    weather,
)
from app.models import (
    NeocpConfirmationPayload,
    ObjectEphemerisPayload,
    ObjectTargetListPayload,
    ObserverCoordinates,
)

app = FastAPI(
    title="AsteroidAPI",
    version="0.0.1",
    description="Simple api to request data for asteroids in better format",
)


@app.get("/")
def root() -> str:
    return "home"


@app.get("/api/v1/target_list")
async def target_list(payload: ObjectTargetListPayload):
    response = await observing_target_list(payload)
    return {"data": response}


@app.get("/api/v1/neocp_confirmation")
def neocp_confirm_list(payload: NeocpConfirmationPayload):
    response = neocp_confirmation(payload)
    return {"data": response}


@app.get("/api/v1/twilight")
def get_twilight_times(payload: ObserverCoordinates):
    response = twilight_times(payload)
    return {"data": response}


@app.get("/api/v1/sun_moon")
def get_sun_moon_eph(payload: ObserverCoordinates):
    response = sun_moon_ephemeris(payload)
    return {"data": response}


@app.get("/api/v1/object_ephemeris")
def get_object_ephemeris(payload: ObjectEphemerisPayload):
    response = object_ephemeris(payload)
    return {"data": response}
