#!/usr/bin/env python
# Code was taken from:
# https://github.com/giampaolo/pyftpdlib/blob/master/demo/basic_ftpd.py
# which has a MIT license and has the following copyright:
# Copyright (C) 2007 Giampaolo Rodola' <g.rodola@gmail.com>.
# Modified by (really minor modifications, all credits goes to author): Emiliano Dalla Verde Marcozzi <6564766d@gmail.com>

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.authorizers import AuthenticationFailed
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import settings
import os.path
import os

setup_django()
from db.models import (Account, Device)


class DeviceAuthorizer(DummyAuthorizer):
    """Authorize devices."""

    def validate_authentication(self, username, password, handler):
        """Validate device."""

        try:
            Account.objects.get(username=username, password=password)
        except Exception:  # TODO: Catch DoesNotExist Django Exception, do not be a madafaka catch em all pokemon trainer
            raise AuthenticationFailed()

        if not self.has_user(username):
            perm = 'elawdm'
            homedir = self.get_home_dir(username)
            self.add_user(username, password, homedir, perm)

    def get_home_dir(self, username):
        """Returns path where ftp files are saved for this user."""
        homedir = os.path.join(settings.FTP_FILES, username)
        if not os.path.isdir(homedir):
            os.makedirs(homedir)
        return homedir

    def get_msg_login(self, username):
        """Greet user."""
        return f"Welcome aboard {username}"


class FTPLiteHandler(FTPHandler):
    """Tero Lite FTPd handler."""

    def split_filename(self, file):
        """Returns device id and filename from given argument."""
        try:
            device_id, filename = file.split('::')
        except Exception:
            raise AuthenticationFailed()

        return device_id, filename

    def on_file_received(self, file):
        """Send received file to device observers."""
        account = Account.objects.get(username=self.username)
        for telegram_account in account.telegram_accounts:
            telegram_account.send_photo(file)


def setup_django():
    """Init Django."""
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    import django
    django.setup()


def main():
    """Start FTPd Server."""
    authorizer = DeviceAuthorizer()
    handler = FTPLiteHandler
    handler.authorizer = authorizer
    handler.banner = "Tero Lite FTPd ready."

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('', 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


if __name__ == '__main__':
    main()
