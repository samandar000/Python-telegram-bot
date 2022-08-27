from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,InlineQueryHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton,InputTextMessageContent,InlineQueryResultArticle,KeyboardButton
import telegram

import os

TOKEN = os.environ['TOKEN']
def start(update,context):
    text = 'Welcome!'
    bot = context.bot 
    button = KeyboardButton(text='Inline')
    keyboard = ReplyKeyboardMarkup(
        [
            [button]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup=keyboard) 

def query(update,context):
    print(1)
    query = update.callback_query
    querybutton = InlineKeyboardButton(
        text='Inline query',
        switch_inline_query_current_chat='inlinequery'
    )
    reply_markup = InlineKeyboardMarkup(
        [
            [querybutton]
        ]
    )
    update.message.reply_text(text='Inline Query',reply_markup=reply_markup)

def inlineQuery(update,context):

    query = update.inline_query.query

    message = InputTextMessageContent(
        message_text=f'Inline search result',
        parse_mode='MarkdownV2',
    )
    result1 = InlineQueryResultArticle(
        title='Inline search',
        input_message_content=message,
        id=1,
        description='inline query'
    )
    results = [result1]
    update.inline_query.answer(results)

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Inline'),query))

updater.dispatcher.add_handler(InlineQueryHandler(inlineQuery,pattern='inlinequery'))

updater.start_polling()
updater.idle()
