from django.contrib.auth.models import AbstractUser
from django.db import models

import threading


class Account(AbstractUser):
    """An account has multiple devices."""


class Device(models.Model):
    """A device."""
    choices = (
        ('ip-camera', 'Camara IP'),
        ('iot', 'Sensor IOT')
    )
    type = models.CharField(max_length=50, choices=choices)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='devices')
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.account} - {self.type} Name: {self.name} @ {self.location}"
