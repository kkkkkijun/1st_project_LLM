from django.urls import path
from cafe import views

app_name = "cafe"
urlpatterns = [
    path("menu_detail/<int:post_id>", views.menu_detail, name = "detail" ),
    path("main/", views.main, name="main"),
]