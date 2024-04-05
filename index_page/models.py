import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver



class Pizzas(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение', upload_to='media/pizzas_images')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    
    class Meta:
        db_table = 'pizzas'
        verbose_name = 'Пицц'
        verbose_name_plural = 'Пиццы'
        
    def __str__(self):
        return f"{self.name}"
