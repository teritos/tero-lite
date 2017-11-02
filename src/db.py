"""Tero Lite database."""

from pony.orm import (
    Set,
    Database,
    Required,
    db_session,
    set_sql_debug,
)
import settings

db = Database()  # pylint: disable=C0103


class Device(db.Entity):
    """A hardware device."""
    token = Required(str)
    label = Required(str)
    active = Required(bool)
    location = Required(str)
    users = Set('User')

    @classmethod
    @db_session
    def new(cls, token, label, active, location):
        """Create a new device."""
        cls(token=token, label=label, active=active, location=location)


class User(db.Entity):
    """A user."""
    alias = Required(str)
    first_name = str
    last_name = str
    telegram_id = int
    device = Required(Device)


db.bind(
    provider='sqlite',
    filename=settings.SQLITE_PATH,
    create_db=True
)
set_sql_debug(settings.DEBUG)
db.generate_mapping(create_tables=True)
