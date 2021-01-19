import datetime,re
from global_consts import RoyalTrident_bot



guild_dict = {
'Bekish': 'bekmurat',
'Scuns87':'Scuns87',
'Coca-Cola': 'kappainho',
'PlotArmor KT': 'PlotArmor',
'Ну этот как его': 'Vasde',
'Старик Семецкий': 'larina457',
'Флегматик': 'Ksandrax',
'EPetuhov': 'EPetuhov',
'undfndnm': 'ProydemteMolodoy',
'Виски': 'Soarelia',
'BolshoyMolodecKT': 'Ln156',
'Тёпленькая вода': 'Renbrane',
'Shinen': 'HatredPerson',
'phenjan': 'tahena',
'Итианаа': 'phenjan',
'ОплотМнеВРот': 'm1sha007',
'Cerethrius': 'gaelicwar',
'Phantasm': 'ElderSign',
'Farfelkygelain': 'Farfelkygelain',
'Maeve': 'notaloneindec',
'Shiawase': 'ProoFFie',
'Сахарок': 'VishenkaNyam',
'cat Leopold': 'GoTo87',
}
guild_keys = guild_dict.keys()
tz = datetime.tzinfo('Europe/Moscow')

f_evening = datetime.datetime(1,1,1,16,45,0,0,tz)
f_morning = datetime.datetime(1,1,1,8,45,0,0,tz)
f_night = datetime.datetime(1,1,1,00,45,0,0,tz)

s_evening = datetime.datetime(1,1,1,16,59,0,0,tz)
s_morning = datetime.datetime(1,1,1,8,59,0,0,tz)
s_night = datetime.datetime(1,1,1,0,59,0,0,tz)

const_times_f =[f_morning,f_evening,f_night]
const_times_s = [s_morning,s_evening,s_night]


def righttime(message):
    now = datetime.datetime.fromtimestamp(message.date)
    for  time_f in const_times_f:
        print(time_f.hour - now.hour + '$'+ now.minute  - time_f.minute + '$'+ time_f.minute - now.minute + '$')
        if((time_f.hour - now.hour == 0) and (now.minute  - time_f.minute > 0) and (time_f.minute - now.minute <= 14)):
                ping(message.text,message.chat.id)


def ping(text,chat_id):
    answer = str()
    list_for_ping = []
    for user in guild_keys:
        if((re.search("🛌]\s"+user,text)) or (re.search("⚒]\s"+user,text)) or (re.search("⚗️]\s"+user,text))):
            list_for_ping.append(guild_dict[user])
            if(len(list_for_ping) == 5):
                for user_ping in list_for_ping:
                    answer += '@'+user_ping + ' '
                RoyalTrident_bot.send_message(chat_id,answer)
                list_for_ping.clear()
                answer =''
    if(len(list_for_ping) > 0):
        for user_ping in list_for_ping:
            answer += '@' + user_ping + ' '
        RoyalTrident_bot.send_message(chat_id, answer)
        list_for_ping.clear()



