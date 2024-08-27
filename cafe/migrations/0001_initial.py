# Generated by Django 5.1 on 2024-08-27 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=10, verbose_name="브랜드")),
                ("category", models.CharField(max_length=5, verbose_name="카테고리")),
                ("coffee_name", models.CharField(max_length=50, verbose_name="이름")),
                ("protein", models.FloatField(blank=True, verbose_name="단백질")),
                ("calorie", models.FloatField(blank=True, verbose_name="칼로리")),
                ("fatty", models.FloatField(blank=True, verbose_name="포화지방")),
                ("na", models.FloatField(blank=True, verbose_name="나트륨")),
                ("dang", models.FloatField(blank=True, verbose_name="당류")),
                ("caffeine", models.FloatField(blank=True, verbose_name="카페인")),
                ("img", models.CharField(max_length=200, verbose_name="이미지")),
            ],
        ),
    ]
