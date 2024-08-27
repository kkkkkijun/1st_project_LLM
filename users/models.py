from django.db import models
from django.contrib.auth.models import AbstractUser
from cafe.models import Menu

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField("닉네임", max_length=10)

class Like(models.Model):
    user_id = models.ForeignKey("users.User",
                             verbose_name="작성자",
                             on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu,
                             verbose_name="메뉴",
                             on_delete=models.CASCADE)
    
class Post(models.Model):
    user_id = models.ForeignKey("users.User",
                             verbose_name="작성자",
                             on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=20)
    contents = models.TextField("내용", blank=True)