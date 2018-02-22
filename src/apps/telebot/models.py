from django.db import models
import threading


class Account(models.Model):
    """A Telegram account."""
    id = models.IntegerField(primary_key=True)
    account = models.ForeignKey(
        'db.Account',
        on_delete=models.CASCADE,
        related_name='telegram_accounts')

    def send_photo(self, fpath):
        """Send a photo to the given telegram user."""
        from apps.telebot.bot import get_bot
        chat_id = self.id
        bot = get_bot()
        t1 = threading.Thread(
            target=bot.send_photo, args=(chat_id, open(
                fpath,
                'rb',
            )))
        t1.start()

    def __str__(self):
        return f"{self.id} - {self.account}"
