import socketio

from urllib.parse import parse_qs

from app.chatlet.models.room import Message, Room

sio = socketio.AsyncServer(async_mode='asgi')

sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ, data):
    chat_id = parse_qs(environ['QUERY_STRING']).get('chat_id')
    username = environ['HTTP_X_USERNAME']

    with sio.session(sid) as session:
        session['username'] = username

    sio.enter_room(sid, chat_id)

    await sio.emit('connect', username, room=chat_id)

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
    with sio.session(sid) as session:
        await sio.emit(f"{session['username']} disconnected")
