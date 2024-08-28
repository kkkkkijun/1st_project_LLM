from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path("feedback/", views.feedback, name = "feedback"),
    path("feedback_delete/<int:feedback_id>/", views.feedback_delete, name="feedback_delete"),
    path("feedback_edit/<int:feedback_id>/", views.feedback_edit, name="feedback_edit"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup, name="signup"),
]