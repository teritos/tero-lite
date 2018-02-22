from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run tero ftp server.'

    def handle(self, *args, **options):
        from apps.ftpd import server
        server.run()
