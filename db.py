from pymongo import MongoClient
import urllib.parse
import re
import random
import config
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (config.dbpass, config.dblog))
db = client['antispam']
ass = db['users']

def add_base(event):
    itog = ass.find_one({"id": event.message.from_id})
    if itog == None:
        code = random.randint(1000,9999)
        post = {"id": event.message.from_id,
                "code": code,
                "activate": False}
        post_id = ass.insert_one(post).inserted_id
        return 1,code #Запрос аунтификации
    else:
        if itog["activate"] == False:
            if str(itog["code"]) == event.message.message:
                db.users.update({'id': event.message.from_id},
                                {'$set': {'activate': True}})
                return 2 #Код пройденой успешной аунтификации
            else:
                return 3#Неправельно введен код
