from requests import get
from sys import argv
from keys import token_bot, channel_id

msg = argv[1]

r = get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (token_bot, channel_id, msg))

 