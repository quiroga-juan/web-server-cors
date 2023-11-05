import os


class Config:
    password = os.environ.get('ADMIN_PASSWORD')
