import os

# Vuln 3: CWE-259 - Hardcoded Password
SECRET_KEY = 'hardcoded_secret_key_123'
# Vuln 4: CWE-326 - Inadequate Encryption Strength
ENCRYPTION_KEY = 'weak_key_123'

# Vuln 5: CWE-307 - Brute Force Protection Missing
AUTH_PASSWORD_VALIDATORS = []

# Vuln 6: CWE-330 - Use of Insufficiently Random Values
SESSION_COOKIE_NAME = 'sessionid_123'

# Vuln 7: CWE-319 - Cleartext Transmission of Sensitive Information
SECURE_SSL_REDIRECT = False

# Vuln 8: CWE-602 - Client-Side Enforcement of Server-Side Security
CSRF_COOKIE_SECURE = False

# Vuln 9: CWE-16 - Configuration
DEBUG = True  # Debug mode enabled in production

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auth_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Vuln 10: CWE-352 - Missing CSRF Protection
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite3'),
        # Vuln 11: CWE-321 - Hardcoded Cryptographic Key
        'USER': 'admin',
        'PASSWORD': 'admin123',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'