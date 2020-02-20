from telethon import TelegramClient, sync
import urllib.parse
import re
import socks
proxy = (socks.SOCKS5, '127.0.0.1', 9050)
app_id = '' #my.telegram.org
app_hash = '' #my.telegram.org
client = TelegramClient('me', app_id, app_hash, proxy=(socks.SOCKS5, '127.0.0.1', 9050)) #client data
antispam_message = 'Просим пройти вас антиспам проверку напишите этот код в сообщении: '
antispam_fail = 'К сожелению код не верен повторите попытку'
antispam_good = 'Вы прошли антиспам проверку теперь можете общатся'
dbpass = urllib.parse.quote_plus("")
dblog = urllib.parse.quote_plus("")
