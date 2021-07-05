#! /usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	12/05/2021 17:47:27
#+ Editado:	05/07/2021 18:16:26
# -------------------------------------------------------------------------------------------------------------
import utils as u

import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# -------------------------------------------------------------------------------------------------------------
def ola(update: Update, _: CallbackContext) -> None:
    if update.message.text.lower() == 'ola':
        update.message.reply_text('Ola')

def command_ola(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('ola')
# -------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
            )
    logger = logging.getLogger(__name__)

    token_bot, nome_canle1 = u.cargarConfig('.config', -1)

    updater = Updater(token_bot)
    dispatcher = updater.dispatcher

    #dispatcher.add_handler(CommandHandler('ola', ola))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ola))
    dispatcher.add_handler(CommandHandler('ola', command_ola))

    # comeza o loop de polling do boot
    updater.start_polling()
    # apaga o bot cando lle das ctrl+c
    updater.idle()
# -------------------------------------------------------------------------------------------------------------
