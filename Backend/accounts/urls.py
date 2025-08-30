from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeViewSet


router = DefaultRouter()
router.register('me', MeViewSet, basename='me')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
