# imports
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest, GetHistoryRequest

api_id = 14360095
api_hash = '4411841d81d92fa47f4052a5ad9a1dd0'

testing = True
if testing:
    limit = 1000
else:
    limit=None

# create client
client = TelegramClient('0602b', api_id, api_hash)
client.start()

# join a public channels via the invite link
# load join urls
channels = [
    'https://t.me/BinancePumpTracker',
    'https://t.me/cryptoflashsignals',
    'https://t.me/binacepumpswhales',
    'https://t.me/cointokendrop',
    'https://t.me/kucoin_pumps',
    'https://t.me/cryptoprofitcoach',
    'https://t.me/joinchat/AAAAAE-ufWSDXHjNy2rQJA',
    'https://t.me/joinchat/TlCyEpSWct1YLa7O',
    'https://t.me/WallStreetBetsPumper',
    'https://t.me/binancepumproys',
    'https://t.me/APE_crypto',
    'https://t.me/Whalesguide',
    'https://t.me/BinanceWaves'
]

from telethon.tl.functions.channels import JoinChannelRequest
for channel in channels:
    try:
        client(JoinChannelRequest(channel))
    except Exception as e:
        print(e)
        # continue
## loop is done, we're in all channels

# access all open dialogs
dialogs = client.get_dialogs(limit=limit)
# get chats
chat_list = [
    dialog.name
    for dialog in dialogs
]

from datetime import datetime as dt

# instantiate empty dict to collect all messages
msg_dict = {}

# iterate over all the chats and messages to save them
# this normally is BAD PRACTICE! There are better ways than using loops. 
# It's ok in this instance because this is supposed to run a single time
# and it is a case of asynchronous programming 
for chat in chat_list:
    try:
        for message in client.iter_messages(chat,limit=limit):
            try: 
                text = str(
                    message.text
                    .replace(',','')
                    .replace("'",'')
                    .replace('**','')
                    .replace('\n','.')
                    .replace('##','')
                    .replace('=','')
                    .lower()
                )
                date = message.date
                id = str(message.sender_id)
                message_id = str(message.id)+'_'+chat+'_'+date.strftime('%Y-%m-%d')
                update = {
                    message_id:{
                        'text':text,
                        'date':date,
                        'id':id,
                        'chat':chat
                    }
                }
                msg_dict.update(update)
                msg=message
            except:
                print('MessageIterError')
    except ValueError as e:
        continue
    print(chat)

# leave the channels
from telethon.tl.functions.channels import LeaveChannelRequest
for channel in channels:
    try:
        client(LeaveChannelRequest(channel))
    except Exception as e:
        print(e)

import pandas as pd
msg_df = pd.DataFrame.from_dict(msg_dict,orient='index') 
# print(msg_df)
    # print(message.sender_id, ':', message.text,':',message.date)
msg_df.to_csv('power.csv')