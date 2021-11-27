import socketio

from urllib.parse import parse_qs

from app.chatlet.models.room import Message, Room
from app.chatlet.util.queries import get_current_user

sio = socketio.AsyncServer(async_mode='asgi')

sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ, data):
    chat_id = parse_qs(environ['QUERY_STRING']).get('chat_id')
    username = get_current_user()

    with sio.session(sid) as session:
        session['username'] = username

    sio.enter_room(sid, chat_id)

    await sio.emit('connect', {'username': username}, room=chat_id)

    message = Message(
        content=data['content'],
        sent_by=username,
        sent_at=data['sent_at']
    )

    insert_in_db = Room(messages=message)
    await insert_in_db.save()

    await sio.emit('message', message.content, to=chat_id)


@sio.event
async def disconnect(sid):
    username = get_current_user()
    with sio.session(sid) as session:
        await sio.emit(f"{session['username']} disconnected")
