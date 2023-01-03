from django.db import models
# Create your models here.
class Sigma(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='media/', default="")
    def __str__(self):
        return self.name



