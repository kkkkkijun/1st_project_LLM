from django.urls import path
from cafe import views

app_name = "cafe"
urlpatterns = [
    path("main/", views.main, name="main"),
]