# Django settings for meu_projeto project.
import os, platform
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOCAL = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Marinho Brandao', 'marinho@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'pycon2009'             # Or path to database file if using sqlite3.
DATABASE_USER = 'postgres'             # Not used with sqlite3.
DATABASE_PASSWORD = '123456'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

# Usada pela template tag 'moneyformat', do django-plus. Depende da locale equivalente
THOUSANDS_SEPARATOR = ''
MONETARY_LOCALE = {
        'darwin': ('pt_BR.utf-8'),      # Mac OS X
        'linux': 'pt_BR.UTF8',          # Linux
        'windows': 'ptb',               # Windows
        }.get(platform.uname()[0].lower(), 'pt_BR.UTF8')

# Formatação de datas
DATE_FORMAT = 'd/m/Y'           # usada na listagem do Admin
DATETIME_FORMAT = 'd/m/Y H:i'   # usada na listagem do Admin

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l^ilbi!(ofj&oqv475*hf-kpns0kf*+2dnq%+q58kf1%rk-bcl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'pagination.middleware.PaginationMiddleware',   # usada pelo widget AjaxFKWidget, do django-plus
    #'utils.profiling.ProfileMiddleware', # implementa profiling no Projeto (usa a setting PROFILE_DIR)
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'djangoplus',
    'pagination',
    'django_extensions',

    'sistema',
    'caixa',
)

#PROFILE_DIR = os.path.join(PROJECT_ROOT_PATH, 'profiling')

