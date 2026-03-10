
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sucesso/<str:protocolo>/", views.sucesso, name="sucesso"),
    path("acompanhar/", views.acompanhar, name="acompanhar"),
]
