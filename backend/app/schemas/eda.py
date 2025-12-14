from pydantic import BaseModel

class EDARequest(BaseModel):
    path: str