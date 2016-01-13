import os.path
import djcelery
djcelery.setup_loader()
# Django settings for alpha project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', 'dev.cityfusion.ca',
                 'www.cityfusion.ca', 'cityfusion.ca']

ADMINS = (
    ('alexandr', 'alexandr.chigrinets@silkcode.com'),
    ('tim', 'tim@cityfusion.ca'),
    ('igor', 'info@silkcode.com'),
)

MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = ''

BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not
# all choices may be available on all operating systems.  On Unix
# systems, a value of None will cause Django to use the same timezone
# as the operating system.  If running in a Windows environment this
# must be set to the same as your system time zone.
TIME_ZONE = 'America/Regina'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as
# not to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold
# user-uploaded files.  Example:
# "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use
# a trailing slash.  Examples: "http://media.lawrence.com/media/",
# "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static
# files in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or
    # "C:/www/django/static".  Always use forward slashes, even on
    # Windows.  Don't forget to use absolute paths, not relative
    # paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5=g^q+(_5rk4_r9%n8)2&cg1oqi05)l4w%%fs8%mc+$l&jeseh'

# List of callables that know how to import templates from various
# sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    # required by django-admin-tools
    'django.core.context_processors.request',
    'event.context_processors.user_location',
    'event.context_processors.top5_tags',
    'accounts.context_processors.user_context',
    'accounts.context_processors.taxes_context',
    'django_facebook.context_processors.facebook',
)

ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',    
    'accounts.middleware.VenueAccountMiddleware',
    'accounts.middleware.UserProfileMiddleware',
    'event.middleware.LocationMiddleware',
    'turbolinks.middleware.TurbolinksMiddleware',
    'home.url_management.middleware.UrlManagementMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1', '31.43.27.104')

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".  Always use forward slashes, even on
    # Windows.  Don't forget to use absolute paths, not relative
    # paths.
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.gis',
    'cities',
    'selectable',
    'registration',
    'south',
    'taggit',
    'taggit_autosuggest',
    'event',
    'home',
    'feedback',
    'easy_thumbnails',
    'image_cropping',
    'ajaxuploader',
    'endless_pagination',
    'django_filters',
    'guardian',
    'pdfutils',
    'accounts',
    'userena',
    'django_facebook',
    'djcelery',
    'turbolinks',
    'mamona',
    'advertising',
    'ckeditor',
    'cityfusion_admin',
    'notices',
    'venues',
    'gears',
    'django_gears',
    'django_exportable_admin'
    # 'sprockets'
    #'debug_toolbar',
)

# A sample logging configuration. The only tangible logging performed
# by this configuration is to send an email to the site admins on
# every HTTP 500 error.  See
# http://docs.djangoproject.com/en/dev/topics/logging for more details
# on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'cities': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'event.services.location_service': {
            'handlers': ['mail_admins'],
            'level': 'WARNING'
        }
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 3355


# django.registration settings, one week window to activate
ACCOUNT_ACTIVATION_DAYS = 7

# django auth settings
LOGIN_REDIRECT_URL = '/events/'

# django taggit settings

# alpha.event settings
# EVENT_PICTURE_DIR #defaults to 'pictures'
EVENT_DEFAULT_PICTURE_URL = STATIC_URL + 'img/default.gif'
# EVENT_RESIZE_METHOD #defaults to Image.BICUBIC (cubic spline
#                      interpolation in a 4x4 environment), can be
#                      Image.NEAREST (use nearest neighbour),
#                      Image.ANTIALIAS (a high-quality downsampling
#                      filter), or Image.BILINEAR (linear
#                      interpolation in a 2x2 environment)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cityfusion.smtp@gmail.com'
EMAIL_HOST_PASSWORD = 'forfusion'
EMAIL_PORT = 587

CITIES_FILES = {
    'city': {
       'filename': 'CA.zip',
       'urls':     ['http://download.geonames.org/export/dump/CA.zip']
    }
}

CITIES_POSTAL_CODES = ['CA']
CITIES_LOCALES = ['en', 'und', 'LANGUAGES']
CITIES_PLUGINS = [
    'cities.plugin.postal_code_ca.Plugin',  # Canada postal codes need region codes remapped to match geonames
]

SELECTABLE_MAX_LIMIT = 15

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

GEOIP_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geoip'))
GEOIP_CITY = "GeoIPCityca.dat"

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'django_facebook.auth_backends.FacebookBackend',
)

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
USERENA_REDIRECT_ON_SIGNOUT = "/events/"

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.Account'

FACEBOOK_APP_ID = "583239701740569"
FACEBOOK_APP_SECRET = "aae620ebe9a61c65018f17b2dfada437"
FACEBOOK_DEFAULT_SCOPE = ['email', 'user_about_me', 'user_birthday', 'user_website', 'create_event', 'manage_pages']
# FACEBOOK_REGISTRATION_BACKEND = 'django_facebook.registration_backends.UserenaBackend'
AUTH_PROFILE_MODULE = 'accounts.Account'

TWILIO_ACCOUNT_SID = 'AC1a554e71d3c0921faa3732bd495f5878'
TWILIO_AUTH_TOKEN = '89eec7d9c48d4d3f3809ed8edb17a48d'
TWILIO_NUMBER = "+12026013648"


MAMONA_ACTIVE_BACKENDS = (
    'paypal',
)

MAMONA_BACKENDS_SETTINGS = {
    'paypal': {
        'url': 'https://www.sandbox.paypal.com/cgi-bin/webscr',
        'email': 'sellet@cityfusion.ca',
    }
}

IPADRESSLAB_KEY = "SAK44B55F864BQ627A4Z"

CKEDITOR_UPLOAD_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ckeditor_uploads'))
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
    },
}

CKEDITOR_CONFIGS = {
    "default":
    {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Styles','Format','Font','FontSize', 'Maximize'],
            '/',
            ['Bold','Italic','Underline','StrikeThrough','-','Undo','Redo'],
            ['Table','-','Link','TextColor','BGColor','Source'],
            '/',
            ['NumberedList','BulletedList','-','Outdent','Indent','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
        ],
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
        ],
        'toolbar': 'Basic',
        'height': 200,
        'width': 400,
        'filebrowserWindowWidth': 940,
        'filebrowserWindowHeight': 725,
    }
}

#Celery settings

BROKER_URL = 'amqp://fusion:forfusion@127.0.0.1:5672/cityfusion_vhost'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

from datetime import timedelta
from celery.schedules import crontab

DELETED_EVENTS_REMINDING_INTERVAL = 5

CELERYBEAT_SCHEDULE = {
    'reminding-about-events-every-5-minutes': {
        'task': 'accounts.tasks.remind_accounts_about_events',
        'schedule': timedelta(minutes=5)
    },
    'reminding-about-deleted-events-every-5-minutes': {
        'task': 'accounts.tasks.remind_accounts_about_deleted_events',
        'schedule': timedelta(minutes=DELETED_EVENTS_REMINDING_INTERVAL)
    },
    'reminding-about-event-every-day': {
        'task': 'accounts.tasks.remind_accounts_about_events_on_week_day',
        'schedule': crontab(hour=6, minute=0),
    },
    'inform-accounts-about-new-events-with-tags-every-3-hours': {
        'task': 'accounts.tasks.inform_accounts_about_new_events_with_tags',
        'schedule': timedelta(hours=3)
    },
    'return-unused-money-to-bonus-every-5-minutes': {
        'task': 'advertising.tasks.return_unused_money_to_bonus_for_advertising_campaigns',
        'schedule': timedelta(minutes=5)
    },
    'upgrade-maxmind-on-wednesday': {
        'task': 'accounts.tasks.upgrade_maxmind',
        'schedule': crontab(minute='20', hour='22', day_of_week='wed')
    }
}

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}

ADVERTISING_TYPE_CPC_ON = False

GEARS_ROOT = os.path.join(BASE_PATH, 'static')

GEARS_DIRS = (
    os.path.join(BASE_PATH, 'assets'),
)

GEARS_COMPRESSORS = {
    'text/css': 'gears.compressors.CSSMinCompressor',
    'application/javascript': 'gears_uglifyjs.UglifyJSCompressor'
}

GEARS_POSTPROCESSORS = {
    'text/css': 'gears.processors.HexdigestPathsCityfusionProcessor',
}

GEARS_DEBUG = True

GEARS_PUBLIC_ASSETS = (
    lambda path: True,
    # lambda path: not any(path.endswith(ext) for ext in ('.css', '.js')),
    # r'^.*combine\.css$',
    # r'^.*combine\.js$',
)