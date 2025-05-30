from django.urls import path
from . import views

app_name = "chat"
urlpatterns = [
    path("", views.index, name="index"),
    path("conversation/", views.conversation, name="conversation"),
    path("history/", views.history, name="history"),
]
