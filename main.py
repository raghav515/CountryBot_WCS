import telebot
import requests
import json
bot = telebot.TeleBot('5653388312:AAEh7bBo_5M6pMU46sUNQinMQfGK-4570rA')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.first_name)
    bot.send_message(message.chat.id, "Hello "+message.chat.first_name +
                     ", I am a Fact Bot. I will give you facts about countries which you will ask me. Use /help to know how to use me. \nEnjoy!")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id, "To get a fact about a country, type /fact <country name>")


@bot.message_handler(commands=['fact'])
def send_fact(message):
    s = str(message.text)
    a = s.split(" ")
    # print(a[1])
    response = requests.get('https://restcountries.com/v3.1/name/'+a[1])
    if (response.status_code == 200):  # Everything went okay, we have the data
        data = response.json()
        # print(data)
        #############################################
        cur = data[0]['currencies']
        k = cur.keys()
        f = 0
        for i in k:
            f = i
            break
        ##############################################
        lang = data[0]['languages']
        lng = ''
        for i in lang:
            lng += lang[i]+', '
        ##############################################
        txt_msg = 'Hello from '+a[1]+'!\nOfficial Name: '+data[0]['name']['official']+'\nCapital: ' + \
            data[0]['capital'][0]+'\nCurrency: '+cur[f]['name'] + \
            '('+f+')\nSymbol: '+cur[f]['symbol']+'\nLanguages Spoken:'+lng
        bot.send_message(chat_id=message.chat.id, text=txt_msg)
        bot.send_photo(chat_id=message.chat.id, photo=data[0]['flags']['png'])
    else:  # something went wrong
        bot.send_message(chat_id=message.chat.id,
                         text="Error, something went wrong.")


bot.infinity_polling()
