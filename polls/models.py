from django.db import models

# Create your models here.

class Client(models.Model):
    rut   = models.CharField(primary_key=True, max_length=11)
    name  = models.CharField(max_length=30)

    def __str__(self):
        return self.rut
