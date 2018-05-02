from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler, Filters
import re
import urllib.request
import requests
import config

def get_audio(link):
    x = requests.get(link).text
    ret = {}
    ret['title'] = x[x.find('<title>') + 7 : x.find('</title>')-9]
    ret['url'] = x.split('twitter:player:stream" content="')[1].split('">')[0].replace('amp;', '')
    return ret
    #urllib.request.urlretrieve(x.split('twitter:player:stream" content="')[1].split('">')[0].replace('amp;', ''), x[x.find('<title>') + 7 : x.find('</title>')-9]+".m4a")

def hello(bot, update):
    update.message.reply_text(
        'Hello {}, Please send a message containing a Smule URL'.format(update.message.chat.first_name))

def link(bot, update):    
    update.message.reply_text("Searching for Audio...")
    match = re.search("http://www.smule.com/p/\d*_\d*",update.message.text)
    if match:
        link = match.group(0)
        audio = get_audio(link)
        update.message.reply_document(audio['url'],filename=audio['title']+".mp3",caption=audio['title'])
    else:
        update.message.reply_text('Failed to get the File. Sorry')


updater = Updater(config.token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(RegexHandler('.*http://www.smule.com/p/\d*_\d*', link))
updater.dispatcher.add_handler(MessageHandler(Filters.all, hello))

updater.start_polling()
updater.idle()