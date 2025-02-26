import socketio

from bff.src.websockets.ws_server import sio

connected_clients = {}

@sio.event
async def connect(sid, environ):
    """New WebSocket connection"""
    print(f"✅ Client connected: {sid}")
    connected_clients[sid] = sid
    await sio.emit("message", {"data": "Connected to WebSocket"}, room=sid)

@sio.event
async def disconnect(sid):
    """Handle WebSocket disconnection"""
    print(f"❌ Client disconnected: {sid}")
    connected_clients.pop(sid, None)

async def broadcast_ws_all_clients(data):
    """Broadcast messages to all WebSocket clients"""
    print(f"📡 Broadcasting: {data}")
    await sio.emit("ml_result", {"data": data})  # Broadcast event
