import config
import telebot
from better_profanity import profanity
bot = telebot.TeleBot(config.token)



@bot.message_handler(content_types=["text"])
def check_message(message): # Название функции не играет никакой роли
    userid = message.from_user.id
    user_first_name = message.from_user.first_name
    censored_text = profanity.censor(message.text)
    if censored_text.__contains__('*'):
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "<a href='tg://user?id={userid}'>{name}</a>".format(userid = userid, name=user_first_name) + " написал ненормативную лексику: " + censored_text, parse_mode='HTML')


if __name__ == '__main__':
     bot.infinity_polling()
#Hi       
