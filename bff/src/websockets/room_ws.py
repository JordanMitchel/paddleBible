from broadcast_ws import sio, connected_clients  # Import shared sio instance

@sio.event
async def join_room(sid, room):
    """Joins a specific WebSocket room"""
    print(f"Client {sid} joined room: {room}")
    connected_clients[sid] = room
    sio.enter_room(sid, room)
    await sio.emit("room_message", {"data": f"{sid} joined {room}"}, room=room)

@sio.event
async def leave_room(sid, room):
    """Leaves a WebSocket room"""
    print(f"Client {sid} left room: {room}")
    sio.leave_room(sid, room)
    connected_clients[sid] = None
    await sio.emit("room_message", {"data": f"{sid} left {room}"}, room=room)

@sio.event
async def send_room_message(sid, data):
    """Sends a message to all clients in the same room"""
    room = connected_clients.get(sid)
    if room:
        print(f"Client {sid} sent to {room}: {data}")
        await sio.emit("room_message", {"data": data}, room=room)
