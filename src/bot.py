"""Tero Lite Bot (for sure using Telegram)."""

from telegram.ext import Updater, CommandHandler
import settings


def start(bot, update):
    """Greet user."""
    _ = bot
    update.message.reply_text('Hello World!')


def hello(bot, update):
    """Just says hello."""
    _ = bot
    update.message.reply_text(
        f'Hello {update.message.from_user.first_name}'
    )


updater = Updater(settings.TELEGRAM_TOKEN)  # pylint: disable=C0103

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
