import socketio


sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*",  # Allow connections from any origin
)

@sio.event
async def connect(sid, environ):
    """New WebSocket connection"""
    print(f"✅ Client connected: {sid}")
    # Debugging: Print the environ (to inspect headers and origins)
    print(f"Connection info: {environ}")
    await sio.emit("message", {"data": "Connected to WebSocket"}, room=sid)

@sio.event
async def disconnect(sid):
    """Handle WebSocket disconnection"""
    print(f"❌ Client disconnected: {sid}")
    # connected_clients.pop(sid, None)

async def broadcast_ws_all_clients(data):
    """Broadcast messages to all WebSocket clients"""
    print(f"📡 Broadcasting: {data}")
    await sio.emit("ml_result", {"data": data})  # Broadcast event


