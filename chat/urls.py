from django.urls import path
from chat.views import index
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
