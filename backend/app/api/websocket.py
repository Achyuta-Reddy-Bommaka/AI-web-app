from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("Connected to FastAPI WebSocket!")
    while True:
        msg = await ws.receive_text()
        await ws.send_text(f"Echo: {msg}")