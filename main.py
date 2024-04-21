import dotenv,os,ai
import telebot as tb

dotenv.load_dotenv()

token = os.getenv("TOKEN")

bot = tb.TeleBot(token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, how can I help you?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, ai.send(message.text))



bot.infinity_polling()