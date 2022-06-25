from django.db import models

# Create your models here.
# 必須機能
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-category_id"]
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ"

# class Purchase(models.Model):
# 任意機能
class Item(models.Model):
    item_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    recommended = models.BooleanField(default=False)
    category = models.ForeignKey("Category",on_delete=models.CASCADE,)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-item_id"]
        verbose_name = "商品"
        verbose_name_plural = "商品"

class ItemsInCart(models.Model):
    user = models.ForeignKey("account.User",on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    amount = models.IntegerField()
    booked_date = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user_id + "のカート" + self.item.name
    
    class Meta:
        ordering = ["-booked_data"]
        verbose_name = "ショッピングカート"
        verbose_name_plural = "ショッピングカート"

# class PurchaseDetail(models.Model):
# 任意機能