from django.urls import path
from .views import zaglushka

urlpatterns = [
    path('', zaglushka)
]