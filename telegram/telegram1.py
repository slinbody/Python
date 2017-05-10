#!/usr/bin/python
# -*- coding: utf8 -*-
import telegram
import time

def get_chat_id():
    '''
http api url:
https://api.telegram.org/bot_format/getUpdates

bot_format=bot[Your_token]
    '''
#    f = urllib2.urlopen('https://api.telegram.org/bot367618733:AAEgEpFy2uVIohVApNn0ARUuKSNXl4ubZmA/getUpdates')
#    x = json.loads(f.read())
#    chat_id = x['result'][0]['message']['chat']['id']
#    chat_id = bot.getUpdates()[-1].message.chat_id
    chat_id = 356160211
    return chat_id


def send_msg(text):
    token1='367618733:AAEgEpFy2uVIohVApNn0ARUuKSNXl4ubZmA'
    bot = telegram.Bot(token=token1)
    #print bot.getMe()

#    chat_id = bot.getUpdates()[-1].message.chat_id
    chat_id = get_chat_id()
    #bot.sendMessage(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

    #bot.sendMessage(chat_id=chat_id, text=current_time)
    bot.sendMessage(chat_id=chat_id, text=text)

def send_photo_by_url(img_url):
    token1='367618733:AAEgEpFy2uVIohVApNn0ARUuKSNXl4ubZmA'
    bot = telegram.Bot(token=token1)
    chat_id = get_chat_id()
    bot.sendPhoto(chat_id=chat_id, photo=img_url)

if __name__ == "__main__":
    current_time = time.strftime("%Y/%m/%d %H:%M:%S")
    send_msg(current_time+" HIHI")
    send_photo_by_url('https://imgur.com/pQbtxJp')
