from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

TOKEN = '2098845762:AAHZ1ATPBGVUn5nnUkJ-U0QMtk0y0yjVnAk'
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

# url = get_url()
# file_extension = re.search("([^.]*)$", url).group().lower()
# file_extension = url.split('.')[-1]
# print(url)
# print(file_extension)

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        # file_extension = re.search("([^.]*)$",url).group(1).lower()#$是從後開始取，^是非XX
        file_extension = url.split('.')[-1]
    return url


def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()