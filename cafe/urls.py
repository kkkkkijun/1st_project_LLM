from django.urls import path
from cafe import views

app_name = "cafe"
urlpatterns = [
    path("menu/<int:menu_id>/", views.menu_detail, name = "detail" ),
    path("main/", views.main, name="main"),
    path("menu/<int:menu_id>/like/", views.menu_like, name='like'), 
    path("comment_add/", views.comment_add, name="comment_add"),
    path("comment_delete/<int:comment_id>", views.comment_delete, name="comment_delete"),
]