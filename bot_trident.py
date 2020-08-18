import telebot,psycopg2, time, logging,htmlentities,re,urllib.parse
from psycopg2 import sql
RoyalTrident_bot = telebot.AsyncTeleBot('1222435814:AAFPEFv8ad_2xBIuYUMc5aIDxqKGhAKRijo')
conn = psycopg2.connect(database='postgres', user='postgres', password='123Anapa2017', host='localhost',port = 5432)
db = conn.cursor()


  





@RoyalTrident_bot.message_handler(regexp="^[дД]ай\s")
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
   # html_caption  '))'  str ну ахуеть, когда видео и доки и прочее шлют оно лежит хуй пойми где  
   #markov сделать для id
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
def check(message):
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
    kek = str(i)
    stred += kek[2:len(kek)-3] + '\n'    
  RoyalTrident_bot.reply_to(message, stred)


@RoyalTrident_bot.message_handler (commands = ['add_trigger'])
def add_trigger(message):
      chat_id = str(message.chat.id)
      create_table_chat_id(chat_id)
      reply = message.reply_to_message
      ask = message.text[13:]
      if(reply is None or (len(message.text) < 14)):
        return 
      db.execute(sql.SQL('''SELECT ask FROM {} WHERE ask =  %s''').format(sql.Identifier(chat_id)) , (ask,))
      if(db.statusmessage == 'SELECT 1'):
          conn.commit()
          updater(message,reply,chat_id,ask)
          return
        
      elif(db.statusmessage == 'SELECT 0'):
        conn.commit()
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
      check = message.text[13:]
      db.execute(sql.SQL('''DELETE FROM {} WHERE ask = %s''').format(sql.Identifier(chat_id)),(check,))
      conn.commit()
      RoyalTrident_bot.reply_to(message, 'Команда удалена')
    

@RoyalTrident_bot.message_handler()
def any_trigger(message):
     chat_id = str(message.chat.id)
     create_table_chat_id(chat_id)
     db.execute(sql.SQL('''SELECT answer FROM {} WHERE ask =  %s''').format(sql.Identifier(chat_id)) , (message.text,))
     if(db.statusmessage == 'SELECT 0'):
        return
     answer = convert_in_list(db.fetchone())
     db.execute(sql.SQL('''SELECT type FROM {} WHERE ask =  %s''').format(sql.Identifier(chat_id)) , (message.text,))
     _type =convert_in_list(db.fetchone())
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

def convert_in_list(turple):
     anylist = str(turple)
     _anylist = anylist[2:len(anylist)-3]
     return _anylist 

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

def main():
  RoyalTrident_bot.polling(none_stop=True)


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

