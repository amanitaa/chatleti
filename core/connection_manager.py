# from typing import List
# from fastapi import WebSocket
#
# from app.chatlet.models.personal_room import PersonalMessage
#
#
# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: List[WebSocket] = []
#
#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         self.active_connections.append(websocket)
#
#     def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)
#
#     @staticmethod
#     async def send_personal_message(message: PersonalMessage, websocket: WebSocket):
#         await websocket.send_text(message)
#
#     async def broadcast(self, message: PersonalMessage):
#         for connection in self.active_connections:
#             await connection.send_text(message)
