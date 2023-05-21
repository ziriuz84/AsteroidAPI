from pydantic import BaseModel

class ObjectTargetListPayload(BaseModel):
    utf8: str
    authenticity_token: str
    latitude: str
    longitude: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    duration: int = 1
    max_objects: int = 10
    min_alt : int = 0
    solar_elong: int = 0
    lunar_elong: int = 0
    object_type: int
    submit: str = "Submit"

