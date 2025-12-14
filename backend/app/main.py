from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, upload, eda, rag, websocket

app = FastAPI(title="FastAPI Minimal Full Stack App")

# CORS so Streamlit can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(eda.router, prefix="/eda", tags=["EDA"])
app.include_router(rag.router, prefix="/rag", tags=["RAG"])
app.include_router(websocket.router, tags=["WebSocket"])