"""Tero Lite database."""

from pony.orm import (
    Set,
    Database,
    Optional,
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
    observers = Set('Observer')

    @staticmethod
    @db_session
    def new(token, label, active, location):
        """Create a new device."""
        Device(token=token, label=label, active=active, location=location)

    @staticmethod
    @db_session
    def is_valid(label, token):
        """Return bool if device is valid."""
        return bool(Device.get(token=token, label=label))


class Observer(db.Entity):
    """A device observer."""
    label = Required(str)
    telegram_id = Optional(int)
    device = Required(Device)


db.bind(
    provider='sqlite',
    filename=settings.SQLITE_PATH,
    create_db=True
)
set_sql_debug(settings.DEBUG)
db.generate_mapping(create_tables=True)
