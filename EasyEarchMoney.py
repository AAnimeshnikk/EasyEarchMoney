from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon import TelegramClient, events, sync
import time
import random
import asyncio


api_id = 1113563
api_hash = '1f7121137341cf01592a5e0079d665ac'

client = TelegramClient('EasyEarchMoney', api_id, api_hash)
client.start()


dlgs = client.get_dialogs()
def AlfaprofitViews():
    for dlg in dlgs:
        if dlg.title == 'ALPHAPROFIT | VIEWS':
            AlphaViews = dlg
    msgs = client.get_messages(AlphaViews, limit = 30)
    for msg in msgs:
        time.sleep(random.uniform(0, 2))
        def get_id_data():
            global button_data
            global message_id
            if msg.reply_markup is not None:
                button_data = msg.reply_markup.rows[0].buttons[0].data
                message_id = msg.id
                print(button_data, message_id)
        try:
            get_id_data()
        except:
            print('KeyboardButtonUrl Error')
        resp = client(GetBotCallbackAnswerRequest(
            AlphaViews, # dialog
            message_id,
            data = button_data
            ))
AlfaprofitViews()

@client.on(events.NewMessage(chats=('ALPHAPROFIT | VIEWS')))
async def normal_handler(event):
    AlfaprofitViews()
