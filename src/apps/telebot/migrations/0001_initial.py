# Generated by Django 2.0.2 on 2018-02-22 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telegram_accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]