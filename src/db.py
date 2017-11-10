"""Tero Lite database."""

import settings
import threading

from pony.orm import (
    Json,
    Database,
    Optional,
    Required,
    PrimaryKey,
    db_session,
    set_sql_debug,
)

db = Database()  # pylint: disable=C0103


class Device(db.Entity):
    """A hardware device."""
    label = Required(str)
    active = Required(bool)
    location = Required(str)
    username = PrimaryKey(str)
    password = Required(str)
    telegram = Optional(Json)

    @staticmethod
    @db_session
    def new(username, password, label, location, telegram):
        """Create a new device."""
        return Device(
            username=username,
            password=password,
            label=label,
            active=True,
            location=location,
            telegram=telegram)

    @staticmethod
    @db_session
    def is_valid_using(username, password):
        """Return bool if device is valid."""
        return bool(Device.get(username=username, password=password))

    @db_session
    def print_telegram_users(self):
        """Display a list of telegram users from this device."""
        for user in self.telegram['users']:
            print(f"{user['name']}\t{user['id']}")

    # TODO: Fix this shit, raises DabaseSessionIsOver
    @db_session
    def add_telegram_user(self, telegram_user):
        """Add an observer to given device."""
        with db_session:
            self.telegram['users'].append(telegram_user)

    @db_session
    def send_photo_to_observers(self, fpath):
        """Send a photo to device observers."""
        from bot import get_bot
        bot = get_bot()
        with db_session:
            for user in self.telegram['users']:
                chat_id = user['id']
                t1 = threading.Thread(
                    target=bot.send_message,
                    args=(
                        chat_id,
                        f"Movimiento detectado en {self.location}",
                    ))
                t2 = threading.Thread(
                    target=bot.send_photo, args=(chat_id, open(
                        fpath,
                        'rb',
                    )))
                t1.start()
                t2.start()


db.bind(provider='sqlite', filename=settings.SQLITE_PATH, create_db=True)
set_sql_debug(settings.DEBUG)
db.generate_mapping(create_tables=True)
