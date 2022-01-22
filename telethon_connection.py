
# imports
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest

api_id = 14360095
api_hash = '4411841d81d92fa47f4052a5ad9a1dd0'

# create client
client = TelegramClient('mike2', api_id, api_hash)
client.start()

# join a public channel via the invite link
from telethon.tl.functions.channels import JoinChannelRequest
channel = 'https://t.me/BinanceWaves'
client(JoinChannelRequest(channel))

dialogs = client.get_dialogs()
print(dialogs[0].message.message)

# send me an update message
client.send_message('MikeTelethon', 'Last task done')

# client = TelegramClient('Mike', api_id, api_hash)
# client.start()

# @client.on(events.NewMessage)
# def my_event_handler(event):
#     if 'hello' in event.raw_text:
#         event.reply('hi!')

# client.idle()