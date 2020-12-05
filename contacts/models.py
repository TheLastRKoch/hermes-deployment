from django.db import models

class Person(models.Model):
    SEX_CHOISES = [('M','Masculine'),('F','Femenine')]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOISES)
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.name