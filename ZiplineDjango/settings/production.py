from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://46230e7aa5cb47259ccd3ebfb175efc8@sentry.io/1290269",
    integrations=[DjangoIntegration()]
)

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR,'static')

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,    
#     #'formatters': {
#     #    'verbose': {
#     #        'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s'
#     #    }
#     #},
#     'handlers': {
#         'gunicorn': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'formatter': 'verbose',
#             'filename': '/opt/djangoprojects/reports/bin/gunicorn.errors',
#             'maxBytes': 1024 * 1024 * 100,  # 100 mb
#         }
#     },
#     'loggers': {
#         'gunicorn.errors': {
#             'level': 'DEBUG',
#             'handlers': ['gunicorn'],
#             'propagate': True,
#         },
#     }
# }