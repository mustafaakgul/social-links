from core.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ENVIRONMENT = 'development'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


ALLOWED_HOSTS = ["nodeme-backend-env.eba-6zp3pfnk.eu-central-1.elasticbeanstalk.com"]