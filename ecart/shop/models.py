from django.db import models

# Create your models here.
class product(models.Model):
    prodName = models.CharField(max_length = 50, default = "")
    prodID = models.AutoField
    prodPrice = models.IntegerField(max_length = 5, default = "")
    prodDesc = models.CharField(max_length = 300, default = "")
    prodImg = models.ImageField(upload_to = "shop/static/shop", default = "")

    def __str__(self):
        return self.prodName


