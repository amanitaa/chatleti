import os

from pydantic import BaseSettings

PROJECT_NAME = 'Chatlet'
VERSION = '0.0.0'


class Settings(BaseSettings):
    # Dev settings
    environment: str = os.getenv('ENVIRONMENT')
    testing: bool = os.getenv('TESTING')

    # Mongo settings
    db_url: str = os.getenv('MONGODB_URL')
    db_name: str = os.getenv('MONGODB_DATABASE_NAME')

    # Security settings
    authjwt_secret_key: str = os.getenv('SECRET_KEY')

    # FastMail SMTP settings
    mail_console: bool = os.getenv('MAIL_CONSOLE', default=False)
    mail_server = os.getenv('MAIL_SERVER', default='smtp.server.io')
    mail_port: int = os.getenv('MAIL_PORT', default=587)
    mail_username: str = os.getenv('MAIL_USERNAME', default='')
    mail_password: str = os.getenv('MAIL_PASSWORD', default='')
    mail_sender: str = os.getenv('MAIL_SENDER', default='noreply@chatlet.io')


CONFIG = Settings()
