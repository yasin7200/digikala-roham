from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/products')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    seller = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    weight = models.FloatField()
    counts = models.PositiveSmallIntegerField()
    rate = models.FloatField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title