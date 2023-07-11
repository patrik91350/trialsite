from django.db import models

# Create your models here.

class City(models.Model):
    country = models.CharField('Country', max_length=50)
    city = models.CharField('City', max_length=50)
    population = models.IntegerField()
    short_description = models.CharField('Country', max_length=250)
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "City"
        verbose_name_plural = 'Cities'

