import asyncio
from asyncio.events import get_running_loop
import socketio
import pytest

username = 'tornike'
chat_id = '11'


@pytest.mark.asyncio
async def test_on_connect():
    sio = socketio.AsyncClient()

    @sio.event
    async def connection():
        print('connection gud')

    @sio.event
    async def send_message(data):
        print('message', data)
        await sio.emit('message', {"message": 'hello'})

    await sio.connect(f'http://0.0.0.0:8000/get/{chat_id}', socketio_path='/ws/socket.io')
    await sio.wait()



