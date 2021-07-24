from django.urls import path
from .views import iniciarSesion
urlpatterns = [
    path('', iniciarSesion, name='Login'),
]