from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    preferred_language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

