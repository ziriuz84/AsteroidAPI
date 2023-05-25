from fastapi import FastAPI, HTTPException
from app.libraries.scheduling import weather, observing_target_list, neocp_confirmation
from app.models import ObjectTargetListPayload, NeocpConfirmationPayload

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
