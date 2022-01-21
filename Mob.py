from Utility import EmptyStringCheck
import time,re
from telebot import types
from Global import Bot,Guild





class Mob:
    def __init__(self,owner,message_for_update,message):
        self.owner = owner
        self.message = message
        self.is_ambush = bool()
        self.mobs_text = self.mobs_text()
        self.message_for_update = message_for_update
        self.timer = 180
        self.link = str()
        self.helpers_list = list()
        self.is_champion = False
        self._force_update = False
        self._MobsLevel = int()
        self.RANGE_FOR_BATTLE_TAKE = 10
        self.is_ambush_check()
        self.mobs_link()
        self.mobs_level()
        self.delete_list = list()

    def start_and_updating(self):
        if(self.is_champion_check() is False):
            self.ping()
        self.updating()
        try:
                answer = self.mobs_text + "⏰:РИП\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + self.helpers()
                Bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id, parse_mode='HTML')
        except Exception as e:
                time.sleep(5)
                print(f"Module start_and_updating /n  Exception :{e}")
        self.clear()

    def clear(self):
        for message in self.delete_list:
            try:
                responce = Bot.delete_message(message.chat.id, message.message_id)

            except  Exception as e:
                print(e)

    def updating(self):
        while (self.is_actual_mob()):
            if (self._force_update == False):
                try:
                    self.do_update()
                    time.sleep(3)
                except Exception:
                    time.sleep(5)

    def helpers(self):
        answer = ''
        n = 1
        for helper in self.helpers_list:
            answer += "<b>" + str(n) + "."  "</b>" + EmptyStringCheck(helper.first_name) + ' ' + EmptyStringCheck(helper.last_name) + ' ' + "(" + '@' + EmptyStringCheck(helper.username) + ")" + '\n'
            n+=1
        return answer

    def mobs_markups(self, btn_url_text, react_btn_text):
            markup = types.InlineKeyboardMarkup()
            react_btn = types.InlineKeyboardButton(text=react_btn_text, callback_data = self.link)
            answer_html = 'https://t.me/share/url?url=' + self.link
            btn_url = types.InlineKeyboardButton(text=btn_url_text, url=answer_html)
            markup.add(btn_url)
            markup.add(react_btn)
            return markup

    def mob_update_helpers(self, user):
        for helper in self.helpers_list:
            if((helper.id == user.id) or (user.id == self.owner.id)):
                return False
        self.helpers_list.append(user)
        self.force_update()
        return True

    def force_update(self):
        self._force_update = True
        if (self.is_actual_mob()):
            self.do_update()
        self._force_update = False

    def mobs_text(self):
          answer = self.message.text.split('\n')
          answer.pop(0)
          new_answer = str()
          for element in answer:
            if ((element is not None) and (re.search("\/fight.{1,100}",element) is None) ):
              new_answer = new_answer + "<b>{}</b>".format(element) + "\n"
          return new_answer

    def ping(self):
        PingList = list()
        for User in Guild.GuildList:
            if(Guild.BlackList.__contains__(User) is not True):
                if(((abs(User.ChatWarsLvl - self._MobsLevel)) <= self.RANGE_FOR_BATTLE_TAKE) and (User.isMain == True) ):
                    PingList.append(User.Username)
        self.delete_list = self.delete_list + Bot.PingByFive(self.message.chat.id,PingList)

    def mobs_level(self):
        AllNumber = 0
        Number = int()
        StringList = self.message.text.split("\n")
        for String in StringList:
            NumberAsk = re.search('\d\sx\s',String)
            if (NumberAsk is not None):
                Number = NumberAsk.group(0)
                Number = re.search('\d{1,3}',Number)
                Number = Number.group(0)
            if(NumberAsk is None):
                Number = 1
            LvlAsk = re.search('lvl\.\d{1,3}',String)
            if(LvlAsk is not None):
                Lvl = LvlAsk.group(0)
                Lvl = re.search('\d{1,3}',Lvl)
                Lvl = Lvl.group(0)
                AllNumber += int(Number)
                self._MobsLevel += int(Number) * int(Lvl)
        self._MobsLevel = self._MobsLevel / AllNumber

    def is_champion_check(self):
        if(re.search("⚜️Forbidden Champion",self.message.text)):
            self.is_champion = True
            self.PinChamp()
            Bot.GivePots(self.message.chat.id)
            return True
        return False

    def do_update(self):
            now = time.time()
            timers = "⏰: " + "<b>{}</b>".format("{:02d}:{:02d}".format(int((self.timer - (now - self.message.forward_date)) / 60),int((self.timer - (now - self.message.forward_date)) % 60)))
            answer = self.mobs_text + "\n" + timers + "\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + self.helpers()
            response = Bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id,
                                             parse_mode='HTML', reply_markup=self.mobs_markups("⚔️ В бой", "🤝 Помогаю"))

    def TooManyReqestCheck(self,Response):
        try:
            return Response.result[1].result.status_code == 429
        except:
            return False

    def is_actual_mob(self):

        return (time.time() - self.message.forward_date) < self.timer

    def PinChamp(self):
        Bot.pin_chat_message(self.message_for_update.chat.id, self.message_for_update.message_id, disable_notification = True)

    def is_ambush_check(self):
        if (re.search("It's an ambush!", self.message.text)):
            self.is_ambush = True
            self.timer = 360
        self.is_ambush = False

    def mobs_link(self):
        link = re.search("\/fight.{1,100}", self.message.text)
        self.link = link.group(0)