import datetime,re
from global_consts import RoyalTrident_bot


guild_dict = {
'Bekish': ['bekmurat'],
'Scuns87':['Scuns87'],
'Coca-Cola': ['kappainho'],
'PlotArmor KT': ['PlotArmor'],
'Ну этот как его': ['Soarelia','Renbrane'],
'Старик Семецкий': ['Soarelia','Renbrane'],
'Флегматик': ['Soarelia','Renbrane'],
'EPetuhov': ['Soarelia','Renbrane'],
'undfndnm': ['PlotArmor'],
'Виски': ['Soarelia'],
'BolshoyMolodecKT': ['Ln156'],
'Тёпленькая вода': ['Renbrane'],
'Shinen': ['HatredPerson'],
'phenjan': ['Scuns87'],
'Итианаа': ['tahena'],
'ОплотМнеВРот': ['Soarelia','PlotArmor'],
'Cerethrius': ['Soarelia','PlotArmor','Renbrane'],
'Phantasm': ['ElderSign'],
'Farfelkygelain': ['Farfelkygelain'],
'Maeve': ['notaloneindec'],
'Shiawase': ['ProoFFie'],
'Сахарок': ['Soarelia','PlotArmor'],
'cat Leopold': ['Soarelia','Scuns87'],
'Kronprincen' : ['Soarelia','PlotArmor','Renbrane']
}

guild_keys = guild_dict.keys()
tz = datetime.tzinfo('Europe/Moscow')
tz = datetime.timezone(datetime.timedelta(hours=3))

f_evening = datetime.datetime(1,1,1,16,45,0,0,tz)
f_morning = datetime.datetime(1,1,1,8,45,0,0,tz)
f_night = datetime.datetime(1,1,1,00,45,0,0,tz)




const_times_f =[f_morning,f_evening,f_night]




def righttime(message):
    now = datetime.datetime.fromtimestamp(message.date,tz)
    for  time_f in const_times_f:
        if((time_f.hour - now.hour  == 0) and (now.minute  - time_f.minute > 0) and (time_f.minute - now.minute <= 14)):
                list_for_ping = create_list_for_ping(message.text)
                ping(list_for_ping,message.chat.id)


def create_list_for_ping(text):
    list_for_ping = list()
    for user in guild_keys:
        if((re.search("🛌]\s"+user,text)) or (re.search("⚒]\s"+user,text)) or (re.search("⚗️]\s"+user,text))):
            list_for_ping.extend(guild_dict[user])
    return list(set(list_for_ping))

def ping(list_for_ping ,chat_id):
    answer = str()
    counter = 0
    while (len(list_for_ping) > 0):
                answer += '@'+str(list_for_ping[0]) + ' '
                counter +=1
                if(counter == 5):
                    RoyalTrident_bot.send_message(chat_id,answer)
                    counter = 0
                    answer =''
                list_for_ping.pop(0)




