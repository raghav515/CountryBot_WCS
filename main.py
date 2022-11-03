import telebot
import requests
import json
bot = telebot.TeleBot('5653388312:AAEh7bBo_5M6pMU46sUNQinMQfGK-4570rA')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.first_name)
    bot.send_message(message.chat.id, "Hello "+message.chat.first_name+", I am a Fact Bot. I will give you facts about countries which you will ask me. Use /help to know how to use me. \nEnjoy!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "To get a fact about a country, type /fact <country name>")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    s = str(message.text)
    a = s.split(" ")
    print(a[1])

    #bot.reply_to(message, message.text)


bot.infinity_polling()
