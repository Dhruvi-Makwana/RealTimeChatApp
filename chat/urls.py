from django.urls import path
from chat.views import index
from . import views

urlpatterns = [
    path("chat/", views.index, name="index"),
]
