from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# URLs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = config_secret_deploy['django']['databases']

print('=DEBUG= : ', DEBUG)
print('=ALLOWED_HOSTS= : ', ALLOWED_HOSTS)