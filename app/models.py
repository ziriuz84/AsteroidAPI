from enum import Enum

from pydantic import BaseModel


class ObjectType(str, Enum):
    asteroid = "mp"
    comet = "cmt"
    nea = "neo"

class NeocpConfirmationPayload(BaseModel):
    latitude:float
    longitude:float
    min_score: int=0
    max_magnitude: int
    height: int=0

class ObjectTargetListPayload(BaseModel):
    utf8: str = "%E2%9C%93"
    authenticity_token: str = "W5eBzzw9Clj4tJVzkz0z%2F2EK18jvSS%2BffHxZpAshylg%3D"
    latitude: float
    longitude: float
    height: float = 0
    year: int
    month: int
    day: int
    hour: int
    minute: int
    duration: int = 1
    max_objects: int = 10
    min_alt: int = 0
    solar_elong: int = 0
    lunar_elong: int = 0
    object_type: ObjectType 
    submit: str = "Submit"
