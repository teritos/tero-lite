"""Tero lite settings."""

import os

DEBUG = True
FTP_FILES = os.getenv('FTP_FILES', '/tmp')
SQLITE_PATH = os.getenv('SQLITE_PATH', 'tero.sqlite')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
