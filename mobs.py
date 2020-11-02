import time,psycopg2,urllib.parse,telebot,re
from telebot import types
from psycopg2 import sql

RoyalTrident_bot = telebot.AsyncTeleBot('1125612607:AAG4o5Myw3TB8ZnYfBbnRMZ0AdW_YG1EVMQ')
conn = psycopg2.connect(database='postgres', user='postgres', password='123Anapa2017', host='localhost',port = 5432)
db = conn.cursor()
def update_helpers(call):
  RoyalTrident_bot.answer_callback_query(call.id)
  db.execute('SELECT helpers_number FROM MOBS helpers_number WHERE link = %s',(call.data,))
  number_result = db.fetchone()
  number_result = number_result[0] + 1
  db.execute('SELECT helpers FROM MOBS  WHERE link = %s',(call.data,))
  result = db.fetchone()
  result = str(result[0])  + "<b>" + str(number_result) + "." +"</b>" + Nonestr(call.from_user.first_name) + "("+ "@" + Nonestr(call.from_user.username )+  ")"+ "\n"
  db.execute('UPDATE MOBS SET helpers = %s  WHERE link = %s',(result,call.data))
  conn.commit()
  db.execute('UPDATE MOBS SET helpers_number = %s  WHERE link = %s',(number_result,call.data))
  conn.commit()
  RoyalTrident_bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup = mobs_markups("⚔️ В бой","🤝 Помогаю",call.data) )

def find_mobs_message(message):
  timer = 180
  if(re.search("It's an ambush!",message.text)):
    timer = 300
  link = re.search("\/fight.{1,100}",message.text)
  link = link.group(0)
  url_link = urllib.parse.quote(link,)
  mobs_text_parsed = mobs_text(message.text)
  markup = mobs_markups("🤝 Помогаю","⚔️ В бой",link)
  answer_html = 'https://t.me/share/url?url=' + url_link 
  message_for_update = RoyalTrident_bot.send_message(message.chat.id,mobs_text(message.text),reply_markup = markup)
  message_for_update = message_for_update.wait()
  db.execute(sql.SQL('''INSERT INTO MOBS (link,helpers_number,helpers) VALUES (%s,%s,%s)''') ,(link,0," "))
  conn.commit()
  db.execute(sql.SQL('''INSERT INTO MOBS_HELPERS (link,helpers_id) VALUES (%s,%s)''') ,(link,message.from_user.id))
  conn.commit()
  try:
    update_mobs_message(link,timer,message.chat.id,message_for_update.message_id,message.forward_date,mobs_text_parsed)
  except:
    RoyalTrident_bot.send_message(450927903,str(message_for_update))

def delete_table():
    db.execute('DROP TABLE MOBS')
    conn.commit()

def update_mobs_message(link,timer,message_chat_id,message_id,message_date,mobs_text):
  while(time.time() - message_date < timer):
	    now  = time.time()	
	    timers = "⏰: " +  "<b>{}</b>".format("{:02d}:{:02d}".format(int((timer - (now  - message_date))/60) , int((timer - (now - message_date))%60)))
	    answer = mobs_text + "\n"+ timers + "\n\n"+ "<b>👑 Хокаге по вызову:\n</b>"+ helpers(link)
	    if(type(RoyalTrident_bot.edit_message_text(answer,message_chat_id,message_id,parse_mode = 'HTML',reply_markup = mobs_markups("⚔️ В бой","🤝 Помогаю",link))) == "bool"):
	     	time.sleep(12)
	    else:
	    	time.sleep(5)
  answer = mobs_text +"\n\n" + "⏰:РИП\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + helpers(link)
  while(type(RoyalTrident_bot.edit_message_text(answer,message_chat_id,message_id,parse_mode = 'HTML')) == "bool"):
    time.sleep(5)
    RoyalTrident_bot.edit_message_text(answer,message_chat_id,message_id,parse_mode = 'HTML')
  #delete_mob(link)
  return


def mobs_markups(btn_url_text,react_btn_text,link):
  markup = types.InlineKeyboardMarkup()
  react_btn = types.InlineKeyboardButton(text = react_btn_text,callback_data = link)
  answer_html = 'https://t.me/share/url?url=' + link 
  btn_url = types.InlineKeyboardButton(text = btn_url_text,url = answer_html)
  markup.add(btn_url)
  markup.add(react_btn)
  return markup

def mobs_text(message_text):
  mobs_str = str()
  mobs_list = re.findall(".{1,50}lvl\.\d{1,5}",message_text)
  for i in mobs_list:
    mobs_str = mobs_str + i + "\n"
  if(re.search("It's an ambush!",message_text)):
    mobs_str + "\n" + "\n"+ "It's an ambush!"
  return ("Ты заметил враждебных существ:\n" + mobs_str )

def helpers(link):
      db.execute('''SELECT helpers FROM MOBS WHERE link = %s''',(link,))
      helpers_result = db.fetchone()
      return helpers_result[0]


def delete_mob(link):
  db.execute('''DELETE FROM MOBS WHERE link = %s''',(link,))
  conn.commit()

def create_mobs_tables():
  db.execute(' CREATE TABLE IF NOT EXISTS MOBS (link text, mobs_text text, helpers_number  SMALLINT, helpers text)')
  conn.commit()
  db.execute(' CREATE TABLE IF NOT EXISTS MOBS_HELPERS (link text,helpers_id text)')
  conn.commit()

def Nonestr(x):
    if x is None:
      return ""
    return x