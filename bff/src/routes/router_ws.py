from typing import Dict

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

# Create a new router for WebSocket routes
ws_router = APIRouter()
connected_clients: Dict[str, WebSocket] = {}

# WebSocket endpoint
@ws_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id:str):
    # Accept the WebSocket connection
    await websocket.accept()

    connected_clients[client_id] = websocket
    print(f"✅ Client {client_id} connected")

    try:
        while True:
            # Receive messages from the client
            message = await websocket.receive_text()
            print(f"Message received: {message}")

            # Send a response back to the client
            await websocket.send_text(f"Message received: {message}")
    except WebSocketDisconnect:
        # Handle client disconnect
        print("Client disconnected")


@ws_router.websocket("/wsa")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the WebSocket connection
    await websocket.accept()


    try:
        while True:
            # Receive messages from the client
            message = await websocket.receive_text()
            print(f"Message received: {message}")

            # Send a response back to the client
            await websocket.send_text(f"Message received: {message}")
    except WebSocketDisconnect:
        # Handle client disconnect
        print("Client disconnected")


