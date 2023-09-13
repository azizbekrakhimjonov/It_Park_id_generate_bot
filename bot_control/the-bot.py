from telegram.ext import Updater, MessageHandler, CommandHandler, ConversationHandler, Filters
from telegram import ReplyKeyboardMarkup
import hello

def start(update):
    update.message.reply_text("*Salom. Bu Autofiller bot!*", parse_mode="Markdown", reply_markup=ReplyKeyboardMarkup([["📃 Guvohnoma yasash"]]))


def runner():
    updater = Updater(token="6384532641:AAF0e8iMw_ZNb1HGqkr8Kz3-X5KsRPyCgTQ")

    dispacher = updater.dispatcher

    dispacher.add_handler(CommandHandler('start', start))

    dispacher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("(📃 Guvohnoma yasash)"), hello.start_conversation)],
        states={
            1: [MessageHandler(Filters.text, hello.turarjoy_raqami)],
            2: [MessageHandler(Filters.text, hello.guvohnoma_raqami)],
            3: [MessageHandler(Filters.text, hello.familiya)],
            4: [MessageHandler(Filters.text, hello.ism)],
            5: [MessageHandler(Filters.text, hello.ism_sharifi)],
            6: [MessageHandler(Filters.text, hello.xona_raqami)],
            7: [MessageHandler(Filters.text, hello.sana)],
            8: [MessageHandler(Filters.photo, hello.rasm)],
            9: [MessageHandler(Filters.text, hello.tasdiqlash)]
        },
        fallbacks=[CommandHandler('stop', start)]
    ))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()




