"""Tero Lite Bot (for sure using Telegram)."""

from telegram.ext import Updater, CommandHandler
from telegram import Bot
from telegram.utils import request

import settings


request.CON_POOL_SIZE = 50


def get_bot():
    """Returns a bot instance."""
    return Bot(settings.TELEGRAM_TOKEN)


def hello(bot, update):
    """Just says hello."""
    _ = bot
    update.message.reply_text(
        f'Hello {update.message.from_user.id}'
    )


if __name__ == '__main__':
    updater = Updater(settings.TELEGRAM_TOKEN)  # pylint: disable=C0103

    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    updater.start_polling()
    updater.idle()
