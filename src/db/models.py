from django.contrib.auth.models import AbstractUser
from django.db import models

import threading


class Account(AbstractUser):
    """An account has multiple devices."""

    @staticmethod
    def send_photo(self, fpath):
        """Send a new photo to all suscriptions."""

        # Notify Telegram Accounts
        for telegram_account in self.telegram_accounts:
            telegram_account.send_photo(fpath)


class TelegramAccount(models.Model):
    """A Telegram account."""
    id = models.IntegerField(primary_key=True)
    account = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE,
        related_name='telegram_accounts')

    @staticmethod
    def send_photo(self, fpath):
        """Send a photo to the given telegram user."""
        from ..telegram_bot import get_bot
        chat_id = self.id
        bot = get_bot()
        t1 = threading.Thread(
            target=bot.send_message,
            args=(
                chat_id,
                f"Movimiento detectado en {self.location}",
            ))
        t2 = threading.Thread(
            target=bot.send_photo, args=(chat_id, open(
                fpath,
                'rb',
            )))
        t1.start()
        t2.start()


    def __str__(self):
        return f"{self.id} - {self.account}"

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

    @staticmethod
    def is_valid_using(username, password):
        """Return bool if device is valid."""

    def __str__(self):
        return f"{self.account} - {self.type} Name: {self.name} @ {self.location}"
