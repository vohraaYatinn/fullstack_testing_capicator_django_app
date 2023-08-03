from django.urls import path
from .views import check_ip_origin

urlpatterns = [
    path('api/test/', check_ip_origin, name='test-api'),
]