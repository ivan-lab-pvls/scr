import telebot
BOT_TOKEN = '6889891310:AAGopeBlk_BoVIdC-BwFE45KkLd7wSRZUvc'
OWNER_ID = 7116960225
GREETING_TEXT = (
    "Опишите свой проект, и наш менеджер свяжется с вами в течение 24 часов."
)
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    """Приветствие нового пользователя"""
    bot.send_message(message.chat.id, GREETING_TEXT)
    user_id = message.chat.id
    print(f"Сообщение от пользователя {user_id}")
@bot.message_handler(func=lambda message: True)
def relay_message(message):
    """Пересылка сообщения от пользователя владельцу бота"""
    user_id = message.from_user.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    user_text = message.text
    owner_message = f"new request from telegram: @{username} \n\n \"{user_text}\""
    bot.send_message(OWNER_ID, owner_message)
bot.polling()
