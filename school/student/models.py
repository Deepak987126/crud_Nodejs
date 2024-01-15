from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name