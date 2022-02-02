
# imports
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest, GetHistoryRequest

api_id = 14360095
api_hash = '4411841d81d92fa47f4052a5ad9a1dd0'

testing = True
if testing:
    limit = 5
else:
    limit=None

# create client
client = TelegramClient('m', api_id, api_hash)
client.start()

# join a public channels via the invite link
# load join urls
import pickle
path = 'data/tele.pickle'
with open(path, 'rb') as f:
    channel_list = pickle.load(f)   

from telethon.tl.functions.channels import JoinChannelRequest
for channel in channel_list[:5]:
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
    for message in client.iter_messages(chat,limit=limit):
        try: 
            text = message.text.replace(',','')
        except:
            text=''
        date = message.date
        id = message.sender_id
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
    print(chat)
import pandas as pd
msg_df = pd.DataFrame.from_dict(msg_dict,orient='index') 
# print(msg_df)
    # print(message.sender_id, ':', message.text,':',message.date)
msg_df.to_csv('data/raw/messages.csv')


# send me an update message
client.send_message('MikeTelethon', 'Last task done')