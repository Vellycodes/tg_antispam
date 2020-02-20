from telethon import TelegramClient, events
import config
import db
client = config.client.start()
id = client.get_me().id

@client.on(events.NewMessage())
async def normal_handler(event):
    if event.message.to_id.user_id != None:
        if event.message.to_id.user_id == id:
            entity = await client.get_entity(event.message.to_id.user_id)
            if entity.bot == False:
                datebase = db.add_base(event=event)
                print(datebase)
                try:
                    if datebase[0] == 1:
                            await client.delete_messages(event.message.from_id, event.message.id)
                            await client.send_message(event.message.from_id, str(config.antispam_message) + str(datebase[1]))
                except:
                    pass
                if datebase == 2:
                        await client.send_message(event.message.from_id, str(config.antispam_good))
                if datebase == 3:
                        await client.delete_messages(event.message.from_id, event.message.id)
                        await client.send_message(event.message.from_id, str(config.antispam_fail))

client.run_until_disconnected()
