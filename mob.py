    
import time,re,urllib
from telebot import types
from global_consts import RoyalTrident_bot


top_list = []

class Mob:
    def __init__(self,owner,link,ambush,message_for_update,message,timer):
        self.owner = owner
        self.message = message
        self.link = link
        self.is_ambush = ambush
        self.mobs_text = self.mobs_text()
        self.message_for_update = message_for_update
        self.timer = timer
        self.helpers_list = list()
        self.is_champion = False
        self._force_update = False

    def updating(self):
        if(re.search("⚜️Forbidden Champion",self.message.text)):
            self.pin_champ()
            self.ping_tops()
            self.give_pots()
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
        RoyalTrident_bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id, parse_mode='HTML')

    def helpers(self):
        answer = ''
        n = 1
        for helper in self.helpers_list:
            answer += "<b>" + str(n) + "."  "</b>"  + nonestr(helper.first_name) +' ' +nonestr(helper.last_name) +' ' + "(" + '@'+nonestr(helper.username) + ")" + '\n'
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

    def mobs_text(self):
          answer = self.message.text.split('\n')
          answer.pop(0)
          new_answer = str()
          for element in answer:
            if ((element is not None) and (re.search("\/fight.{1,100}",element) is None) ):
              new_answer = new_answer + "<b>{}</b>".format(element) + "\n"
          return new_answer


    def ping_tops(self):
        RoyalTrident_bot.send_message(self.message.chat.id,'''@kappainho @bekmurat @Farfelkygelain @PlotArmor @ProoFFie''')
        RoyalTrident_bot.send_message(self.message.chat.id,'@Scuns87 @Soarelia')

    def give_pots(self):

        answer = "/g_withdraw"+" p04 " + str(1) + " p05 " + str(1) + " p06 " + str(1)
        answer_url = urllib.parse.quote(answer, )
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Писы" + '</a>'
        RoyalTrident_bot.send_message(self.message.chat.id,answer_html,parse_mode='HTML')
        answer = "/g_withdraw"+" p01 " + str(1) + " p02 " + str(1) + " p03 " + str(1)
        answer_url = urllib.parse.quote(answer,)
        answer_html = '<a href="https://t.me/share/url?url=' + answer_url + '">' + "Раги" + '</a>'
        RoyalTrident_bot.send_message(self.message.chat.id,answer_html,parse_mode='HTML')

def nonestr(x):
    if x is None:
      return ""
    return x




