#!/usr/bin/env python3
import telebot, psycopg2, time, htmlentities, re, urllib.parse
from psycopg2 import sql
from mobs import create_mobs_tables, update_helpers, find_mobs_message
from stock import stock


RoyalTrident_bot = telebot.AsyncTeleBot('1125612607:AAG4o5Myw3TB8ZnYfBbnRMZ0AdW_YG1EVMQ')
conn = psycopg2.connect(database='postgres', user="postgres", password='123Anapa2017', host='localhost', port = 5432)
db = conn.cursor()

@RoyalTrident_bot.callback_query_handler(func=lambda call: True)
def decorated_update_helpers(call):
  update_helpers(call)


@RoyalTrident_bot.message_handler(func=lambda message: message.forward_from is not None and message.forward_from.username == "ChatWarsBot",regexp = "Ты заметил враждебных существ. " )
def decorated_find_mobs_message(message):
  find_mobs_message(message)



@RoyalTrident_bot.message_handler(regexp= "[Лл]авки")
def timed_resolve(message):
    answer =''' Вишня — <a href="http://t.me/share/url?url=/ws_chery">/ws_chery</a>''' + '\n'+ '''Пруфе — <a href="http://t.me/share/url?url=/ws_happy">/ws_happy</a>''' + '\n'+'''Мейв — <a href="http://t.me/share/url?url=/ws_FnwIe">/ws_FnwIe</a>'''  + '\n'+ '''Мрак — <a href="http://t.me/share/url?url=/ws_lT0Rm">/ws_lT0Rm</a>''' + '\n'+'''Фарфель — <a href="http://t.me/share/url?url=/ws_XioEX">/ws_XioEX</a>'''
    RoyalTrident_bot.send_message(message.chat.id,answer,parse_mode = 'HTML')


@RoyalTrident_bot.message_handler(func = lambda message: message.forward_from is not None and message.forward_from.username == "ChatWarsBot")
def decorated_stock(message):
    stock(message)


    


@RoyalTrident_bot.message_handler(regexp="^([дД]ай|[Ll]fq)\s")
def give_any(message):
  text = message.text
  g_withdraw ="/g_withdraw"
  answer = g_withdraw
  additional_any = []
  amount = "1"
  if(re.search("\d{1,100}",text)):
     result = re.search("\d{1,100}",text)
     amount = result.group(0)
  if(re.search("\s[Фф][Дд]($|\s)",text)):
            answer += " p04 " + amount +  " p05 " +  amount + " p06 " +  amount
  if(re.search("\s[Фф][Рр]($|\s)",text)):
            answer += " p01 " + amount +  " p02 " +  amount + " p03 " +  amount
  if(re.search("\s[Мм][Оо][Рр][Фф]([Ыы]|$|\s)",text)) :
            answer += " p19 " + amount +  " p20 " +  amount + " p21 " +  amount


  if(answer == g_withdraw):
    if(re.search("\s\w{1,100}",text)):
      result = re.findall("\s\w{1,100}",text)
      while(len(result)>18):
         while (len(additional_any) != 18): 
               additional_any.insert(0, result.pop(0))
         give_additional_any(additional_any,message)
         additional_any.clear()
      for element in result:
            if(element != ("дай" or "Дай" )):
              answer += element 
  if(answer == g_withdraw):
    return          
  answer_url = urllib.parse.quote(answer,)
  answer_html = '<a href="https://t.me/share/url?url=' + answer_url +  '">'+ answer + '</a>'
  RoyalTrident_bot.send_message(message.chat.id,answer_html,parse_mode = 'HTML')



@RoyalTrident_bot.message_handler(commands = ['info'])
def info(message):
    message_str = str()
    reply = message.reply_to_message
    chat_id = str(message.chat.id)
    if(reply is None):
      return 
    first_name = reply.from_user.first_name
    username = reply.from_user.username
    last_name = reply.from_user.last_name
    message_id = reply.message_id
    user_id = str(reply.from_user.id)
    date_str = '<b>' +'Date: '+ '</b>' + '<code>' + str(time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.localtime(reply.date))) + '</code>'
    if(reply.sticker is not None):
      message_str = '<b>'+'Media type: </b>'+ 'sticker'+'\n'

    elif(reply.audio is not None):
      message_str = '<b>'+'Media type: </b>'+ 'audio'+ '\n'

    elif(reply.location is not None):
      message_str = '<b>'+'Media type: </b>'+ 'location'+ '\n'

    elif(reply.video is not None):
      message_str = '<b>'+'Media type: </b>'+ 'video'+'\n'

    elif(reply.video_note is not None):
      message_str = '<b>'+'Media type: </b>'+ 'video_note'+'\n' 

    elif(reply.audio is not None):
      message_str = '<b>'+'Media type: </b>'+  'audio'+ '\n'

    elif(reply.photo is not None):
      message_str = '<b>'+'Media type: </b>'+ 'photo'+ '\n'

    elif(reply.document is not None):
      message_str = '<b>'+'Media type: </b>'+ 'document'+ '\n'

    elif(reply.text is not None):
      reply_text = htmlentities.encode(reply.text)
      message_str ='<b>'+ 'Message: '+ '</b>'+ reply_text + '\n'

    user_str = '<b>' + 'User: '+ '</b>' + Nonestr(first_name) + Nonestr(last_name) + '(' + Nonestr(username) + ('/' if len(Nonestr(username)) > 0 else "") + '<code>' + user_id  + '</code>'  + ')' + '\n'
    answer = message_str + user_str + date_str
    RoyalTrident_bot.send_message(chat_id, answer,parse_mode = 'HTML')



@RoyalTrident_bot.message_handler(commands = ['chat_id'])
def chat_id(message):
    str = message.chat.id
    RoyalTrident_bot.reply_to(message, str)


@RoyalTrident_bot.message_handler(commands = ['show_triggers'])
def show_triggers(message):
  chat_id = str(message.chat.id)
  create_table_chat_id(chat_id)
  db.execute(sql.SQL('''SELECT ask FROM {} ''').format(sql.Identifier(chat_id)))
  if(db.statusmessage == 'SELECT 0'):
    return
  answer = db.fetchall()
  stred ='Список триггеров : \n'
  for i in answer :
    stred += i[0]+ '\n'    
  RoyalTrident_bot.reply_to(message, stred)


@RoyalTrident_bot.message_handler (commands = ['add_trigger'])
def add_trigger(message):
      chat_id = str(message.chat.id)
      create_table_chat_id(chat_id)
      reply = message.reply_to_message
      ask_result = re.search("\s.*",message.text)
      print(ask_result)
      ask = ask_result.group(0)
      print(ask)
      ask_result = re.search(".*",ask)
      print(ask_result)
      ask = ask_result.group(0)
      print(ask)
      ask = ask[1:]
      if(reply is None or (len(message.text) < 14)):
        return 
      db.execute(sql.SQL('''SELECT ask FROM {}''').format(sql.Identifier(chat_id)))
      result = db.fetchall()
      result = convert(result)
      if(lower_check(result,ask)!= False):
          conn.commit()
          updater(message,reply,chat_id,ask)
          return

      if(reply.audio is not None):
         db.execute(sql.SQL('''INSERT INTO {} (ask,answer,type) VALUES ( %s, %s,%s)''').format(sql.Identifier(chat_id)),(ask ,reply.audio(0).file_id, 'audio'))
         conn.commit()
         RoyalTrident_bot.reply_to(message, 'Аудио добавлено')


      if(reply.video_note is not None):
         db.execute(sql.SQL('''INSERT INTO {} (ask,answer,type) VALUES ( %s, %s,%s)''').format(sql.Identifier(chat_id)),(ask ,reply.video_note.file_id, 'video_note'))
         conn.commit()
         RoyalTrident_bot.reply_to(message, 'Кругляш добавлен')



      elif(reply.document is not None):
          db.execute(sql.SQL('''INSERT INTO {} (ask,answer,type) VALUES ( %s, %s,%s)''').format(sql.Identifier(chat_id)),(ask ,reply.document.file_id, 'document'))
          conn.commit()
          RoyalTrident_bot.reply_to(message, 'Документ добавлен')

      elif(reply.photo is not None):
          image = reply.photo[0]
          db.execute(sql.SQL('''INSERT INTO {} (ask,answer,type) VALUES ( %s, %s,%s)''').format(sql.Identifier(chat_id)), (ask ,image.file_id, 'photo'))
          conn.commit()
          RoyalTrident_bot.reply_to(message, 'Фото добавлено')

      elif(reply.video is not None):
          db.execute(sql.SQL('''INSERT INTO {} (ask,answer,type) VALUES ( %s, %s,%s)''').format(sql.Identifier(chat_id)),(ask ,reply.video.file_id, 'video'))
          conn.commit()
          RoyalTrident_bot.reply_to(message, 'Видео добавлено')

      elif(reply.voice is not None):
          db.execute(sql.SQL('''INSERT INTO {} (ask,answer,type) VALUES ( %s, %s,%s)''').format(sql.Identifier(chat_id)) ,(ask ,reply.voice.file_id, 'voice'))
          conn.commit()
          RoyalTrident_bot.reply_to(message, 'Войс добавлен')

      elif(reply.text is not None):
          db.execute(sql.SQL('''INSERT INTO {} (ask,answer,type) VALUES ( %s, %s,%s)''').format(sql.Identifier(chat_id)) ,(ask ,reply.text, 'text'))
          conn.commit()
          RoyalTrident_bot.reply_to(message, 'Текст добавлен')
              

@RoyalTrident_bot.message_handler(commands = ['del_trigger'])
def del_trigger(message):
    chat_id = str(message.chat.id)
    create_table_chat_id(chat_id)
    if (len(message.text) >= 14):
      ask_result = re.search("\s.*",message.text)
      ask = ask_result.group(0)
      ask_result = re.search(".*",ask)
      ask = ask_result.group(0)
      ask = ask[1:]
      db.execute(sql.SQL('''DELETE FROM {} WHERE ask = %s''').format(sql.Identifier(chat_id)),(ask,))
      conn.commit()
      RoyalTrident_bot.reply_to(message, 'Команда удалена')



    

@RoyalTrident_bot.message_handler()
def any_trigger(message):
     chat_id = str(message.chat.id)
     create_table_chat_id(chat_id)
     db.execute(sql.SQL('''SELECT ask FROM {}''').format(sql.Identifier(chat_id)))
     result = db.fetchall()
     result = convert(result)
     if(lower_check(result,message.text)!= False):  
       ask = lower_check(result,message.text)
     else:
         return
     db.execute(sql.SQL('''SELECT type FROM {} WHERE ask =  %s''').format(sql.Identifier(chat_id)) , (ask,))
     type_ = db.fetchone()
     _type = type_[0]
     db.execute(sql.SQL('''SELECT answer FROM {} WHERE ask =  %s''').format(sql.Identifier(chat_id)) , (ask,))
     _answer = db.fetchone()
     answer = _answer[0]
     if(_type is not None):
           if(_type=='audio'):
              RoyalTrident_bot.send_audio(chat_id,answer)
           elif(_type =='document'):
              RoyalTrident_bot.send_document(chat_id,answer)

           elif(_type =='photo'):
              RoyalTrident_bot.send_photo(chat_id,answer)

           elif(_type =='video'):
              RoyalTrident_bot.send_video(chat_id,answer)

           elif(_type =='video_note'):
              RoyalTrident_bot.send_video_note(chat_id,answer)

           elif(_type =='voice'):
              RoyalTrident_bot.send_voice(chat_id,answer)

           elif(_type =='text'):
              if answer is not None and len(answer) > 0:
                  RoyalTrident_bot.reply_to(message, answer)

def updater(message,reply,chat_id,ask):

      if(reply.audio is not None):
         db.execute(sql.SQL('''UPDATE  {} SET  answer = %s WHERE ask = %s''').format(sql.Identifier(chat_id)),(reply.audio(0).field_id,ask , ))
         conn.commit()
         db.execute(sql.SQL('''UPDATE  {} SET  type = %s WHERE ask = %s''').format(sql.Identifier(chat_id)),('audio', ask ,))
         conn.commit() 
         RoyalTrident_bot.reply_to(message, 'Аудио перезаписано')

      elif(reply.document is not None):
        db.execute(sql.SQL('''UPDATE  {} SET  answer = %s WHERE ask = %s''').format(sql.Identifier(chat_id)),(reply.document.file_id, ask ,))
        conn.commit()
        db.execute(sql.SQL('''UPDATE  {} SET  type = %s WHERE ask = %s''').format(sql.Identifier(chat_id)),('document', ask ,))
        conn.commit()
        RoyalTrident_bot.reply_to(message, 'Документ перезаписан')

      elif(reply.photo is not None):
        image = reply.photo[0]
        db.execute(sql.SQL('''UPDATE  {} SET  answer = %s WHERE ask = %s''').format(sql.Identifier(chat_id)), (image.file_id,ask,))
        conn.commit()
        db.execute(sql.SQL('''UPDATE  {} SET  type = %s WHERE ask = %s''').format(sql.Identifier(chat_id)) ,( 'photo',ask))
        conn.commit()

        RoyalTrident_bot.reply_to(message, 'Фото перезаписано')

      elif(reply.video is not None):
        db.execute(sql.SQL('''UPDATE  {} SET  answer = %s WHERE ask = %s''').format(sql.Identifier(chat_id)),(reply.video.file_id,ask,))
        conn.commit()
        db.execute(sql.SQL('''UPDATE  {} SET  type = %s WHERE ask = %s''').format(sql.Identifier(chat_id)) ,( 'video',ask))
        conn.commit()
        RoyalTrident_bot.reply_to(message, 'Видео перезаписано')


      elif(reply.video_note is not None):
        db.execute(sql.SQL('''UPDATE  {} SET  answer = %s WHERE ask = %s''').format(sql.Identifier(chat_id)),(reply.video_note.file_id,ask,))
        conn.commit()
        db.execute(sql.SQL('''UPDATE  {} SET  type = %s WHERE ask = %s''').format(sql.Identifier(chat_id)) ,( 'video_note',ask))
        conn.commit()
        RoyalTrident_bot.reply_to(message, 'Кругляш перезаписан')


      elif(reply.voice is not None):
        db.execute(sql.SQL('''UPDATE  {} SET  answer = %s WHERE ask = %s''').format(sql.Identifier(chat_id)) ,(reply.voice.file_id,ask))
        conn.commit()
        db.execute(sql.SQL('''UPDATE  {} SET  type = %s WHERE ask = %s''').format(sql.Identifier(chat_id)) ,( 'voice',ask))
        conn.commit()
        RoyalTrident_bot.reply_to(message, 'Войс перезаписан')

      elif(reply.text is not None):
        db.execute(sql.SQL('''UPDATE  {} SET  answer = %s WHERE ask = %s''').format(sql.Identifier(chat_id)) ,(reply.text,ask))
        conn.commit()
        db.execute(sql.SQL('''UPDATE  {} SET  type = %s WHERE ask = %s''').format(sql.Identifier(chat_id)) ,( 'text',ask))
        conn.commit()
        RoyalTrident_bot.reply_to(message, 'Текст перезаписан')



def create_table_chat_id(chat_id):
 db.execute(sql.SQL(' CREATE TABLE IF NOT EXISTS {} (id serial NOT NULL, ask text, answer text, type text)').format(sql.Identifier(chat_id)))
 conn.commit()

def Nonestr(x):
    if x is None:
        return ""
    return x



def give_additional_any(result,message):
    g_withdraw ="/g_withdraw"
    answer = g_withdraw
    for i in result:
            if(i != ("дай" or "Дай" )):
              answer += i 
    answer_url = urllib.parse.quote(answer,)
    answer_html = '<a href="https://t.me/share/url?url=' + answer_url +  '">'+ answer + '</a>'
    RoyalTrident_bot.send_message(message.chat.id,answer_html,parse_mode = 'HTML')


def convert(tuple):
    new_list = list()
    for i in tuple:
        b = i[0]
        new_list.append(b)
    return new_list





def lower_check(table_list,ask):
  for i in table_list:
    if(i.lower() == ask.lower()):
      return i
  return False




def main():
  create_mobs_tables()
  while(True):
    try :
        RoyalTrident_bot.polling(none_stop=True)
    except:
        time.sleep(5)


if __name__=='__main__':
  main()

#def
#if (items_code[i] in anylist):

#kt_list = ['Farfelkygelain','ungewissheit','kappainho','Scuns87','notaloneindec','bekmurat','larina457','EPetuhov','Vasde','Ksandrax','GoTo87','VishenkaNyam','phenjan','PlotArmor','tahena','Renbrane','coronashizus','Soarelia','ProoFFie','gaelicwar','HatredPerson','ProydemteMolodoy','Ln156','ElderSign','','',]


#def kt_check(message):
	#if(message.from_user.username in kt_list):
		#return True
	#else:
		#return False

