import environ

from .common import *


environ.Env.read_env(BASE_DIR/'.env')
env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'django-insecure-r9$j3gb=3l+u!y$j$j3y3%b3e4%uh_z49((9s@ru41uzo*7d!g')
)

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

if DEBUG:
    from .development import *
else:
    from .production import *