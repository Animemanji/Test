import telebot

API_TOKEN = '6139882386:AAFZUzoNQTYoGsszz4TQbZEuB4aH2ZxgeaQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the music bot!")

@bot.message_handler(commands=['play'])
def play_music(message):
    # Implement your music playing functionality here
    bot.reply_to(message, "Playing music...")

if __name__ == '__main__':
    bot.polling()
