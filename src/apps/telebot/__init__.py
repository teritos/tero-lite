
from django.dispatch import receiver
from apps.ftpd.signals import motion_detected

@receiver(motion_detected)
def handle_motion_detection(username, filename, **kwargs):
    """Send photo to telegram accounts when motion detected."""

    from apps.telebot.models import Account

    # Send photo to all telegram related accounts
    for account in Account.objects.filter(account__username=username).all():
        account.send_photo(fpath=filename)
        print(f'got signal! {username} {filename}')
