from django.utils.translation import gettext as _
from django.http import JsonResponse

def my_view(request):
    response_data = {
        'message': _("Welcome to my site.")
    }
    return JsonResponse(response_data)


'''
Ensure Django Handles the "Accept-Language" Header
With LocaleMiddleware enabled, Django will automatically set the language for the request based on the "Accept-Language" header.

Summary
Django Backend: Ensure LocaleMiddleware is enabled in settings.py, configure LANGUAGES and LOCALE_PATHS, and use translations in views.
React Frontend: Set the "Accept-Language" header in requests based on the user's selected language, and store the language preference in localStorage.
Language Detection: With LocaleMiddleware, Django will automatically detect the "Accept-Language" header and respond in the appropriate language.
'''


'''settings.py============

MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    ...
]

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
    ('bn', 'Bengali'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'en'

'''