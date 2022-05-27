from fastapi_mail import FastMail, ConnectionConfig, MessageSchema

from app.config import settings


mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_SENDER,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
)

mail = FastMail(mail_config)


async def send_password_reset(email: str, token: str):
    url = "http://0.0.0.0:8000/password/reset/" + token
    if not settings.MAIL_CONSOLE:
        message = MessageSchema(
            recipients=[email],
            subject='password reset',
            body=f'click link to reset password: {url}',
        )
        await mail.send_message(message)
