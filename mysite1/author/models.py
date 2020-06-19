from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User

# Create your models here.
class  Author (models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()


    def __str__(self):
        return self.full_name

