from django.db import models

# Create your models here.

# CAR MODEL
class CarModel(models.Model):
    make = models.CharField(max_length=30, default="")
    model = models.CharField(max_length=30, default="")
    year = models.IntegerField(default=0)
    mpg = models.IntegerField(default= 0)

    # FOR YEAR/MAKE/MODEL TO SHOW IN ADMIN SITE
    def __str__(self):
        return f'{self.year} {self.make} {self.model} '