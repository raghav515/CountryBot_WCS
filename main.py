#!/usr/bin/env python3
import telebot
import requests
import json
bot = telebot.TeleBot('YOUR_API_KEY') #API_TOKEN


@bot.message_handler(commands=['start']) #start command
def send_welcome(message):
    print(message.chat.first_name)
    bot.send_message(message.chat.id, "Hello "+message.chat.first_name +
                     ", I am a Fact Bot. I will give you facts about countries which you will ask me. Use /help to know how to use me. \nEnjoy!")


@bot.message_handler(commands=['help']) #help command
def send_help(message):
    bot.send_message(
        message.chat.id, "To get a fact about a country, type /fact <country name>")


@bot.message_handler(commands=['fact']) #fact command
def send_fact(message):
    s = str(message.text) # Input converted to string
    a = s.split(" ")
    # print(a[1])
    cname=''
    for i in range(1,len(a)):
        cname=cname+a[i]
        if i!=len(a)-1:
            cname=cname+" " #Error handling for country names with spaces
    response = requests.get('https://restcountries.com/v3.1/name/'+cname) #API Call
    if (response.status_code == 200):  # Everything went okay, we have the data
        data = response.json() 
        #############################################
        cur = data[0]['currencies'] #Currency data
        k = cur.keys()
        f = 0
        for i in k:
            f = i
            break
        ##############################################
        lang = data[0]['languages'] #Language data 
        lng = ''
        for i in lang:
            lng += lang[i]+', '
        ##############################################
        txt_msg = 'Hello from '+cname+'!\nOfficial Name: '+data[0]['name']['official']+'\nCapital: ' + \
            data[0]['capital'][0]+'\nCurrency: '+cur[f]['name'] + \
            '('+f+')\nSymbol: '+cur[f]['symbol']+'\nLanguages Spoken:'+lng #Final message
        bot.send_message(chat_id=message.chat.id, text=txt_msg) #Sending message
        bot.send_photo(chat_id=message.chat.id, photo=data[0]['flags']['png']) #Sending flag
    else:  # Error Handing in case of wrong country name
        bot.send_message(chat_id=message.chat.id,
                         text="Looks like you have entered a wrong country name. Please try again.") #Error message


bot.infinity_polling() #Bot polling
