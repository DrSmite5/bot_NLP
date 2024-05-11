import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from chatgpt import ChatGPT

chatbot = ChatGPT(config.api_key)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, готовый общаться с вами. Просто напишите мне что-нибудь.')

def echo(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = chatbot.ask_question(user_input)
    update.message.reply_text(response)

def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Извините, я не понимаю эту команду.")

def main() -> None:
    updater = Updater("6609927310:AAHwMT_cEDviUIsnJEal4eVAxZz3--ElWw4")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
