from django.contrib import admin
from db.models import (
    Account,
    Device,
    TelegramAccount
)

# Register your models here.
admin.site.register(Account)
admin.site.register(Device)
admin.site.register(TelegramAccount)
