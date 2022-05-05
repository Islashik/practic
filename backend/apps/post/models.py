from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='images/')