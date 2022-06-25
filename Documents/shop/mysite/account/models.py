from django.db import models

# Create your models here.
class User(models.Model):

    user_id = models.CharField(primary_key=True, max_index=128, unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.user_id
        
    class Meta:
        ordering = ["-user_id"]
        verbose_name = "ユーザ"
        verbose_name_plural = "ユーザ"

# 必須機能