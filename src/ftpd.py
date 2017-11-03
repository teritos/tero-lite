#!/usr/bin/env python

# This code was taken from: 
# https://github.com/giampaolo/pyftpdlib/blob/master/demo/basic_ftpd.py
# which has a MIT license and has the following copyright: 
# Copyright (C) 2007 Giampaolo Rodola' <g.rodola@gmail.com>.
# Modified by: Emiliano Dalla Verde Marcozzi <edvm@fedoraproject.org>
# to work for Tero Lite

"""A basic FTP server which uses a DummyAuthorizer for managing 'virtual
users', setting a limit for incoming connections.
"""

import db

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.authorizers import AuthenticationFailed
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class DeviceAuthorizer(DummyAuthorizer):
    """Authorize devices."""

    def validate_authentication(self, username, password, handler):
        """Validate device."""
        if not db.Device.is_valid(label=username, token=password):
            raise AuthenticationFailed()

    def get_home_dir(self, username):
        """TODO"""

    def get_msg_login(self, username):
        """TODO"""


def main():
    """Start FTPd Server."""
    authorizer = DeviceAuthorizer()
    handler = FTPHandler
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