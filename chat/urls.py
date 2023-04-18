from django.urls import path
# from . import views
from .views import Index

urlpatterns = [
    path("chat/", Index.as_view())
]
