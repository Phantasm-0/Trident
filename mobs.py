import time,datetime,psycopg2,urllib.parse,telebot,re
from telebot import types

RoyalTrident_bot = telebot.AsyncTeleBot('1222435814:AAFPEFv8ad_2xBIuYUMc5aIDxqKGhAKRijo')
conn = psycopg2.connect(database='postgres', user='postgres', password='123Anapa2017', host='localhost',port = 5432)
db = conn.cursor()
def update_helpers(call):
  RoyalTrident_bot.answer_callback_query(call.id)
  db.execute('SELECT helpers_number FROM MOBS helpers_number WHERE link = %s',(call.data,))
  number_result = db.fetchone()
  number_result = number_result[0] + 1
  db.execute('SELECT helpers FROM MOBS  WHERE link = %s',(call.data,))
  result = db.fetchone()
  result = str(result[0])  + "<b>" + str(number_result) + "." +"</b>" + call.from_user.first_name + "("+ "@" + call.from_user.username +  ")"
  number_result = number_result + 1
  db.execute('UPDATE MOBS SET helpers = %s  WHERE link = %s',(result,call.data))
  conn.commit()
  db.execute('UPDATE MOBS SET helpers_number = %s  WHERE link = %s',(number_result,call.data))
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
  db.execute(sql.SQL('''INSERT INTO MOBS (link,helpers_number,helpers) VALUES (%s,%s,%s)''') ,(link,0,"\n"))
  conn.commit()
  db.execute('SELECT helpers_number FROM MOBS helpers_number WHERE link = %s',(link,))
  number_result = db.fetchone()
  update_mobs_message(link,timer,message.chat.id,message_for_update.message_id,message.forward_date,mobs_text_parsed)



def create_mobs_table():
  db.execute(' CREATE TABLE IF NOT EXISTS MOBS (link text, mobs_text text, helpers_number  SMALLINT, helpers text)')
  conn.commit()

def delete_table():
    db.execute('DROP TABLE MOBS')
    conn.commit()

def update_mobs_message(link,timer,message_chat_id,message_id,message_date,mobs_text):
  while(time.time() - message_date < timer):
    now  = time.time()
    timers = "⏰: " +  "<b>{}</b>".format("{:02d}:{:02d}".format(int((timer - (now  - message_date))/60) , int((timer - (now - message_date))%60)))
    answer = mobs_text + "\n\n"+ timers + "\n\n"+ "<b>👑 Хокаге по вызову:\n</b>"+ helpers(link)
    RoyalTrident_bot.edit_message_text(answer,message_chat_id,message_id,parse_mode = 'HTML',reply_markup = mobs_markups("⚔️ В бой","🤝 Помогаю",link))
    time.sleep(2)
  answer = mobs_text +"\n\n" + "⏰:РИП\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + helpers(link)
  while(RoyalTrident_bot.edit_message_text(answer,message_chat_id,message_id,parse_mode = 'HTML') == True):
    time.sleep(1)
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

