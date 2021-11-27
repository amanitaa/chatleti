import socketio

from urllib.parse import parse_qs

from app.chatlet.util.queries import get_current_user

sio = socketio.AsyncServer(async_mode='asgi')

sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ, data):
    chat_id = parse_qs(environ['QUERY_STRING']).get('chat_id')
    username = get_current_user()

    sio.enter_room(sid, chat_id)

    await sio.emit('connect', {'username': username}, room=chat_id)


@sio.event
async def disconnect(sid):
    pass
