from requests import get
from sys import argv

token_bot = "1292759573:AAFQXmTVmXBUplwzzqwhsrw6w6kgDCO8Md8"
channel_id = "@q23rty"
msg = argv[1]

r = get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (token_bot, channel_id, msg))

 