from fastapi import APIRouter

from app.chatlet.routes.auth import router as auth_router
from app.chatlet.routes.password import router as password_router
from app.chatlet.routes.register import router as register_router
from app.chatlet.routes.user import router as user_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(password_router)
router.include_router(register_router)
router.include_router(user_router)
