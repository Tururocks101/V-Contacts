from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=400)
    relationship = models.CharField(max_length=300)
    email = models.EmailField(max_length=250)
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.full_name}'
