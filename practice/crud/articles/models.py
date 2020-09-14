from django.db import models

# Create your models here.
# model의 기본 Model을 상속받는다.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()