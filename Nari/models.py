from django.db import models
class Contact(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=200)
    def _str_(self):
        return self.email

# Create your models here.
