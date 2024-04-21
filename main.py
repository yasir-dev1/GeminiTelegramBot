import dotenv,os
import telebot as tb

dotenv.load_dotenv()

token = os.getenv("TOKEN")

bot = tb.TeleBot(token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, how can I help you?")



bot.infinity_polling()