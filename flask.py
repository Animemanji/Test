from flask import Flask, request
import telebot

API_TOKEN = '6139882386:AAFZUzoNQTYoGsszz4TQbZEuB4aH2ZxgeaQ'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/' + API_TOKEN, methods=['POST'])
def get_message():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR_NETLIFY_APP_NAME.netlify.app/' + API_TOKEN)
    return 'Webhook set', 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the music bot!")

if __name__ == "__main__":
    app.run(debug=True)
