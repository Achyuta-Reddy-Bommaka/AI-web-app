from fastapi import APIRouter, HTTPException
from app.schemas.auth import LoginRequest
from app.core.security import verify_credentials

router = APIRouter()

@router.post("/login")
def login(req: LoginRequest):
    if verify_credentials(req.username, req.password):
        return {"message": "Login successful"}
    raise HTTPException(401, "Invalid username or password")