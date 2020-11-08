
import time,urllib.parse,telebot,re
from telebot import types


RoyalTrident_bot = telebot.AsyncTeleBot('1222435814:AAFPEFv8ad_2xBIuYUMc5aIDxqKGhAKRijo')

mob_list = []

class Mob:
    def __init__(self,owner,link,ambush,mobs_text,message_for_update,message,timer):
        self.owner = owner
        self.link = link
        self.is_ambush = ambush
        self.mobs_text = mobs_text
        self.message_for_update = message_for_update
        self.message = message
        self.timer = timer
        self.helpers_list = list()
        self.is_champion = False
        self._force_update = False

    def updating(self):
        if(re.search("⚜️Forbidden Champion",self.message.text)):
            self.pin_champ()
        answer = str()
        while (time.time() - self.message.forward_date < self.timer):
            if(self._force_update == False):
                now = time.time()
                timers = "⏰: " + "<b>{}</b>".format("{:02d}:{:02d}".format(int((self.timer - (now - self.message.forward_date)) / 60), int((self.timer - (now - self.message.forward_date)) % 60)))
                answer = self.mobs_text + "\n" + timers + "\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + self.helpers()
                if (type(RoyalTrident_bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id, parse_mode='HTML',reply_markup= self.mobs_markups("⚔️ В бой", "🤝 Помогаю"))) == "bool"):
                    time.sleep(9)
                else:
                    time.sleep(5)
        answer = self.mobs_text + "⏰:РИП\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + self.helpers()
        any = RoyalTrident_bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id, parse_mode='HTML')
        print(any)

    def helpers(self):
        answer = ''
        n = 1
        for helper in self.helpers_list:
            answer += "<b>" + str(n) + "."  "</b>"  + nonestr(helper.first_name) + nonestr(helper.last_name) + "(" + '@'+nonestr(helper.username) + ")" + '\n'
            n+=1
        return answer

    def mobs_markups(self,btn_url_text, react_btn_text):
            markup = types.InlineKeyboardMarkup()
            react_btn = types.InlineKeyboardButton(text=react_btn_text, callback_data = self.link)
            answer_html = 'https://t.me/share/url?url=' + self.link
            btn_url = types.InlineKeyboardButton(text=btn_url_text, url=answer_html)
            markup.add(btn_url)
            markup.add(react_btn)
            return markup

    def mob_update_helpers(self,user):
        for helper in self.helpers_list:
            if((helper.id == user.id) or (user.id == self.owner.id)):
                return False
        self.helpers_list.append(user)
        self.force_update()
        return True

    def force_update(self):
        self._force_update = True
        if(time.time() - self.message.forward_date < self.timer):
            now = time.time()
            timers = "⏰: " + "<b>{}</b>".format("{:02d}:{:02d}".format(int((self.timer - (now - self.message.forward_date)) / 60),int((self.timer - (now - self.message.forward_date)) % 60)))
            answer = self.mobs_text + "\n" + timers + "\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + self.helpers()
            RoyalTrident_bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id,
                                               parse_mode='HTML', reply_markup=self.mobs_markups("⚔️ В бой", "🤝 Помогаю"))
        self._force_update = False

    def pin_champ(self):
        RoyalTrident_bot.pin_chat_message(self.message_for_update.chat.id,self.message_for_update.message_id,disable_notification = True)



def update_helpers(call):
  for mob in mob_list:
      if (mob.link == call.data):
            if(mob.mob_update_helpers(call.from_user) is False):
                RoyalTrident_bot.answer_callback_query(call.id,"Ты не пройдешь!",show_alert = True)
                return
  RoyalTrident_bot.answer_callback_query(call.id)

def find_mobs_message(message):
  ambush = False
  timer = 180
  if(re.search("It's an ambush!",message.text)):
    ambush = True
    timer = 300
  link = re.search("\/fight.{1,100}",message.text)
  link = link.group(0)
  mobs_text_parsed = mobs_text(message.text)
  mob = Mob(message.from_user, link, ambush, mobs_text_parsed,None,message,timer)
  markup = mob.mobs_markups("⚔️ В бой","🤝 Помогаю")
  message_for_update = RoyalTrident_bot.send_message(message.chat.id,mobs_text(message.text),reply_markup = markup,parse_mode='HTML')
  message_for_update = message_for_update.wait()
  mob.message_for_update = message_for_update
  mob_list.append(mob)
  mob.updating()
  mob_list.remove(mob)




def nonestr(x):
    if x is None:
      return ""
    return x



def mobs_text(message_text):
  answer = message_text.split('\n')
  answer.pop(0)
  new_answer = str()
  for element in answer:
    if ((element is not None) and (re.search("\/fight.{1,100}",element) is None) ):
      new_answer = new_answer + "<b>{}</b>".format(element) + "\n"
  return new_answer
