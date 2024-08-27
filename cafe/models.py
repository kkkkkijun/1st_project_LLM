from django.db import models

# Create your models here.
class Menu(models.Model):
    brand = models.CharField("브랜드", max_length=10)
    category = models.CharField("카테고리", max_length=5)
    coffee_name = models.CharField("이름", max_length=50)
    protein = models.FloatField("단백질", blank=True)
    calorie = models.FloatField("칼로리", blank=True)
    fatty = models.FloatField("포화지방", blank=True)
    na = models.FloatField("나트륨", blank=True)
    dang = models.FloatField("당류", blank=True)
    caffeine = models.FloatField("카페인", blank=True)
    img = models.CharField("이미지", max_length=200)

class Comment(models.Model):
    user_id = models.ForeignKey("users.User",
                             verbose_name="작성자",
                             on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu,
                             verbose_name="메뉴",
                             on_delete=models.CASCADE)
    content = models.TextField("내용", blank=True)
    created = models.DateTimeField("작성일시", auto_now_add=True)
