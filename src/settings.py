"""Tero lite settings."""

import os

DEBUG = True
SQLITE_PATH = os.getenv('SQLITE_PATH', 'tero.sqlite')
