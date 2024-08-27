from django.urls import path
from cafe import views


urlpatterns = [
    path("menu_detail/<int:post_id>", views.menu_detail, name = "detail" )
]