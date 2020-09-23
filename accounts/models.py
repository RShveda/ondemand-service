from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    address = models.TextField()
    is_service_provider = models.BooleanField(default=False)
