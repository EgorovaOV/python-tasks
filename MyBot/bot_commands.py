from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *


def hello(update: Update, context: CallbackContext) :
    log(update, context)
    update.message.reply_text(f'HI, darling {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext) :
    log(update, context)
    update.message.reply_text(f'/hello\n/time\n/help\n/sum\n')

def time_command(update: Update, context: CallbackContext) :
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now()}')#datetime.datetime.now().time()
def sum_command(update: Update, context: CallbackContext) :
    log(update, context)
    msg = update.message.text
    item = msg.split()# разбить на элементы(сум 1число 2 число)
    x = int(item[1])
    y = int(item[2])
    print(msg)
    update.message.reply_text(f'{x} + {y} = {x + y}')
#def mult_command(update: Update, context: CallbackContext) :
 #   update.message.reply_text(f'')