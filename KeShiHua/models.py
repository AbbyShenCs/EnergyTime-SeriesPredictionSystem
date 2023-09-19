from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Users(AbstractUser):
    set_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    age = models.CharField(verbose_name='Age', max_length=16, default='18')
    set = models.CharField(verbose_name='Gender', max_length=12, default='Male', choices=set_choices)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User Table"
        verbose_name_plural = "User Table"

class ShuJu(models.Model):
    date = models.DateTimeField(verbose_name='Date', max_length=124)
    Total_radiation = models.FloatField(verbose_name='Total_radiation', default=0.0, max_length=124)
    Direct_radiation = models.FloatField(verbose_name='Direct_radiation', default=0.0)
    Diffuse_radiation = models.FloatField(verbose_name='Diffuse_radiation', default=0.0)
    Temperature = models.FloatField(verbose_name='Temperature', default=0.0)
    Pressure = models.FloatField(verbose_name='Pressure', default=0.0)
    Humidity = models.FloatField(verbose_name='Humidity', default=0.0)
    Actual_power = models.FloatField(verbose_name='Actual_power', default=0.0)
    Rated_power = models.FloatField(verbose_name='Rated_power', default=0.0)
    type = models.CharField(verbose_name='Region', max_length=16, default='')

    class Meta:
        verbose_name = "Information Table"
        verbose_name_plural = "Information Table"

class Lishi_ShuJu(models.Model):
    date = models.DateTimeField(verbose_name='Date', max_length=124)
    Total_radiation = models.FloatField(verbose_name='Total_radiation', default=0.0, max_length=124)
    Direct_radiation = models.FloatField(verbose_name='Direct_radiation', default=0.0)
    Diffuse_radiation = models.FloatField(verbose_name='Diffuse_radiation', default=0.0)
    Temperature = models.FloatField(verbose_name='Temperature', default=0.0)
    Pressure = models.FloatField(verbose_name='Pressure', default=0.0)
    Humidity = models.FloatField(verbose_name='Humidity', default=0.0)
    Actual_power = models.FloatField(verbose_name='Actual_power', default=0.0)
    Rated_power = models.FloatField(verbose_name='Rated_power', default=0.0)

    class Meta:
        verbose_name = "Historical Information Table"
        verbose_name_plural = "Historical Information Table"

class YuCe_ShuJu(models.Model):
    date = models.DateTimeField(verbose_name='Date', max_length=124)
    Total_radiation = models.FloatField(verbose_name='Total_radiation', default=0.0, max_length=124)
    Direct_radiation = models.FloatField(verbose_name='Direct_radiation', default=0.0)
    Diffuse_radiation = models.FloatField(verbose_name='Diffuse_radiation', default=0.0)
    Temperature = models.FloatField(verbose_name='Temperature', default=0.0)
    Pressure = models.FloatField(verbose_name='Pressure', default=0.0)
    Humidity = models.FloatField(verbose_name='Humidity', default=0.0)
    Actual_power = models.FloatField(verbose_name='Actual_power', default=0.0)
    Rated_power = models.FloatField(verbose_name='Rated_power', default=0.0)
    type = models.CharField(verbose_name='Region', max_length=16, default='')

    class Meta:
        verbose_name = "Forecast Information Table"
        verbose_name_plural = "Forecast Information Table"

class Lishi_YuCe_ShuJu(models.Model):
    date = models.DateTimeField(verbose_name='Date', max_length=124)
    Total_radiation = models.FloatField(verbose_name='Total_radiation', default=0.0, max_length=124)
    Direct_radiation = models.FloatField(verbose_name='Direct_radiation', default=0.0)
    Diffuse_radiation = models.FloatField(verbose_name='Diffuse_radiation', default=0.0)
    Temperature = models.FloatField(verbose_name='Temperature', default=0.0)
    Pressure = models.FloatField(verbose_name='Pressure', default=0.0)
    Humidity = models.FloatField(verbose_name='Humidity', default=0.0)
    Actual_power = models.FloatField(verbose_name='Actual_power', default=0.0)
    Rated_power = models.FloatField(verbose_name='Rated_power', default=0.0)

    class Meta:
        verbose_name = "Historical Forecast Information Table"
        verbose_name_plural = "Historical Forecast Information Table"
