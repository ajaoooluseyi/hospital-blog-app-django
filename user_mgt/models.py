from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    address_line1 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)


