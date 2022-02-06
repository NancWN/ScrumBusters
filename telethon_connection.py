# imports
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest, GetHistoryRequest

api_id = 14360095
api_hash = '4411841d81d92fa47f4052a5ad9a1dd0'

testing = True
if testing:
    limit = 100
else:
    limit=None

# create client
client = TelegramClient('0602b', api_id, api_hash)
client.start()

# join a public channels via the invite link
# load join urls
import pickle
path = 'data/tele.pickle'
with open(path, 'rb') as f:
    channel_list = pickle.load(f)   

from telethon.tl.functions.channels import JoinChannelRequest
for channel in channel_list[:100]:
    try:
        client(JoinChannelRequest(channel))
    except Exception as e:
        print(e)
        continue
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


#using a list comprehension to iterate over all the chats
list_comp=[message for chat in chat_list for message in client.iter_messages(chat,limit=limit)]

#parameter die helfen durch die list_comp zu iterarieren
end=limit
start=0

#die zugehörigen chats zu den messages zuordnen
for chat in chat_list:
    for j in range(start,end):
        try: 
            text = str(
                list_comp[j].text
                .replace(',','')
                .replace("'",'')
                .replace('**','')
                .replace('\n','.')
                .replace('##','')
                .lower()
            )
        except:
            text = ''
            end=end-limit+1 #damit leere strings übersprungen werden
            start=j-limit+1
            break
        date = list_comp[j].date
        id = str(list_comp[j].sender_id)
        message_id = str(list_comp[j].id)+'_'+chat+'_'+date.strftime('%Y-%m-%d')
        update = {
            message_id:{
                'text':text,
                'date':date,
                'id':id,
                'chat':chat
            }
        }
        msg_dict.update(update)
        msg=list_comp[j]
    print (chat)
    end=end+limit
    start=start+limit


import pandas as pd
msg_df = pd.DataFrame.from_dict(msg_dict,orient='index') 
# print(msg_df)
    # print(message.sender_id, ':', message.text,':',message.date)
msg_df.to_csv('data/sample/messages.csv')


# send me an update message
client.send_message('me', 'Last task done')


#_______________________________________________________
#the old code without list comprehension
"""for chat in chat_list:
    for message in client.iter_messages(chat,limit=limit):
        try: 
            text = str(
                message.text
                .replace(',','')
                .replace("'",'')
                .replace('**','')
                .replace('\n','.')
                .replace('##','')
                .lower()
            )
        except:
            text=''
            
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
    print(chat)"""