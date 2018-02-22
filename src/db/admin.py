from django.contrib import admin
from db.models import (
    Account,
    Device,
    TelegramAccount
)


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = ('account', 'type', 'name', 'location', 'active',)
    search_fields = ('account',)

# Register your models here.
admin.site.register(Account)
admin.site.register(Device, DeviceAdmin)
admin.site.register(TelegramAccount)
