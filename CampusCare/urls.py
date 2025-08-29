
from django.contrib import admin
from django.urls import path, include, URLPattern, URLResolver
from django.http import JsonResponse
from django.urls import get_resolver
from django.conf import settings


def _iter_urlpatterns(patterns, prefix=""):
    for p in patterns:
        if isinstance(p, URLPattern):
            route = str(p.pattern)
            yield (prefix + route) or "/"
        elif isinstance(p, URLResolver):
            route = str(p.pattern)
            new_prefix = prefix + route
            yield from _iter_urlpatterns(p.url_patterns, new_prefix)


def api_index(request):
    if settings.DEBUG:
        resolver = get_resolver()
        endpoints = sorted({("/" + path).replace("//", "/") for path in _iter_urlpatterns(resolver.url_patterns)})
        return JsonResponse({'status': 'server is running', 'endpoints': endpoints})
    return JsonResponse({'status': 'server is running'})

urlpatterns = [
    path('', api_index),
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
]
