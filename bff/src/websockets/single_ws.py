from broadcast_ws import sio, connected_clients  # Import the shared sio instance

@sio.event
async def connect(sid, environ):
    """New WebSocket connection"""
    print(f"Client connected: {sid}")
    connected_clients[sid] = sid
    await sio.emit("message", {"data": "Connected to WebSocket"}, room=sid)

@sio.event
async def disconnect(sid):
    """Handle WebSocket disconnection"""
    print(f"Client disconnected: {sid}")
    connected_clients.pop(sid, None)

@sio.event
async def my_message(sid, data):
    """Receive message from WebSocket client"""
    print(f"Received from {sid}: {data}")
    await sio.emit("response", {"data": f"Processed: {data}"}, room=sid)
