
import telebot


BOT_TOKEN = '6133542290:AAHm00bN6Fh4J9fjmrvifsmtYF9UNaTle4s'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    with open("temp_file.txt","w") as f:
        f.write(message.text)
    bot.reply_to(message, "done")

bot.infinity_polling()

