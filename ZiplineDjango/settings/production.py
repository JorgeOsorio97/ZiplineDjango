from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

del STATICFILES_DIRS
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