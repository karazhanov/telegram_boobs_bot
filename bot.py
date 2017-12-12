import config
import telebot
from telebot import util
from bb_request import BBRequests

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def repeat(message):
    if util.is_command(message.text):
        print("CMD " + message.text)
        command = util.extract_command(message.text)
        if BBRequests.is_photo_cmd(command):
            BBRequests.send_image_by_cmd(command, bot, message.chat.id)
    else:
        print(message.text)
        bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['contact'])
def repeat(message):
    contact = message.contact
    chat = message.chat
    print("contact = " + contact)
    print("chat = " + chat)


if __name__ == '__main__':
    bot.polling(none_stop=True)
