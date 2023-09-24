from core.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ENVIRONMENT = 'local'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


ALLOWED_HOSTS = ["127.0.0.1", "localhost", "nodeme-backend-env.eba-6zp3pfnk.eu-central-1.elasticbeanstalk.com", '*']