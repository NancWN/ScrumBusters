# imports
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest

api_id = 14360095
api_hash = '4411841d81d92fa47f4052a5ad9a1dd0'

with TelegramClient('Mike', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('MikeTelethon', 'Hello, myself!'))
    updates = client(ImportChatInviteRequest('BitcoinBillionaires'))