from fastapi_mail import FastMail, ConnectionConfig, MessageSchema

from core.config import CONFIG

mail_config = ConnectionConfig(
    MAIL_USERNAME=CONFIG.mail_username,
    MAIL_PASSWORD=CONFIG.mail_password,
    MAIL_FROM=CONFIG.mail_sender,
    MAIL_PORT=CONFIG.mail_port,
    MAIL_SERVER=CONFIG.mail_server,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
)

mail = FastMail(mail_config)


async def send_password_reset(email: str, token: str):
    url = CONFIG.root_url + "/password/reset/" + token
    if not CONFIG.mail_console:
        message = MessageSchema(
            recipients=[email],
            subject='password reset',
            body=f'click link to reset password: {url}',
        )
        await mail.send_message(message)
