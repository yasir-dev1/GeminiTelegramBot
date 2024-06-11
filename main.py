import os
import dotenv
import telebot as tb
from PIL import Image
from io import BytesIO
from ai import generate_content  # Import from ai.py

# Load environment variables
dotenv.load_dotenv()

# Get the Telegram bot token
token = os.getenv("TOKEN")
bot = tb.TeleBot(token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, how can I help you?")

@bot.message_handler(content_types=['photo', 'text'])
def handle_message(message):
    if message.photo:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Convert the photo to a PIL Image object
        image = Image.open(BytesIO(downloaded_file))
        image_path = f"/tmp/{message.photo[-1].file_id}.jpg"
        image.save(image_path)

        if message.caption:
            prompt = message.caption
        else:
            prompt = "What do you think about this photo?"

        ai_response = generate_content(prompt, image_path)
        bot.reply_to(message, ai_response)
    elif message.text:
        ai_response = generate_content(message.text)
        bot.reply_to(message, ai_response)

bot.infinity_polling()
