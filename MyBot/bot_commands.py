from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime


def hello(update: Update, context: CallbackContext) :
    update.message.reply_text(f'HI, darling {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext) :
    update.message.reply_text(f'/hello\n/time\n/help\n')
def time_command(update: Update, context: CallbackContext) :
    update.message.reply_text(f'{datetime.datetime.now().time()}')
#def sum_command(update: Update, context: CallbackContext) :
 #   update.message.reply_text(f'')
#def mult_command(update: Update, context: CallbackContext) :
 #   update.message.reply_text(f'')