from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lista de URLs que no requieren autenticación
        exempt_urls = [
            reverse('login'),
            reverse('logout'),
            reverse('index'),
            reverse('sign_up'),
        ]

        if not request.user.is_authenticated and request.path_info not in exempt_urls:
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)