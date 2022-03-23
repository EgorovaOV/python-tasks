from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater('5183511361:AAGvLxXNPDkxjM5oevdz-Epc9aUpHpOrXTA')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server is')
updater.start_polling()
updater.idle()