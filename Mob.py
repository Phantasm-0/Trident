from Utility import EmptyStringCheck
import time,re
from telebot import types
from Global import Bot,Guild





class Mob:
    def __init__(self,owner,message_for_update,message):
        self.owner = owner
        self.message = message
        self.is_ambush = bool()
        self.mobs_text = self.MobsText()
        self.message_for_update = message_for_update
        self.timer = 180
        self.link = str()
        self.helpers_list = list()
        self.is_champion = False
        self._force_update = False
        self._MobsLevel = int()
        self.RANGE_FOR_BATTLE_TAKE = 10
        self.IsAmbush()
        self.MobsLink()
        self.MobsLevel()

    def StartAndUpdating(self):
        if(self.IsChampion() is False):
            self.Ping()
        self.Updating()
        try:
                answer = self.mobs_text + "⏰:РИП\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + self.Helpers()
                Bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id, parse_mode='HTML')
        except:
                time.sleep(5)

    def Updating(self):
        while (self.IsActualMob()):
            if (self._force_update == False):
                try:
                    self.DoUpdate()
                    time.sleep(2)
                except Exception:
                    time.sleep(5)
    def Helpers(self):
        answer = ''
        n = 1
        for helper in self.helpers_list:
            answer += "<b>" + str(n) + "."  "</b>" + EmptyStringCheck(helper.first_name) + ' ' + EmptyStringCheck(helper.last_name) + ' ' + "(" + '@' + EmptyStringCheck(helper.username) + ")" + '\n'
            n+=1
        return answer

    def MobsMarkups(self,btn_url_text, react_btn_text):
            markup = types.InlineKeyboardMarkup()
            react_btn = types.InlineKeyboardButton(text=react_btn_text, callback_data = self.link)
            answer_html = 'https://t.me/share/url?url=' + self.link
            btn_url = types.InlineKeyboardButton(text=btn_url_text, url=answer_html)
            markup.add(btn_url)
            markup.add(react_btn)
            return markup

    def MobUpdateHelpers(self, user):
        for helper in self.helpers_list:
            if((helper.id == user.id) or (user.id == self.owner.id)):
                return False
        self.helpers_list.append(user)
        self.ForceUpdate()
        return True

    def ForceUpdate(self):
        self._force_update = True
        if (self.IsActualMob()):
            self.DoUpdate()
        self._force_update = False

    def MobsText(self):
          answer = self.message.text.split('\n')
          answer.pop(0)
          new_answer = str()
          for element in answer:
            if ((element is not None) and (re.search("\/fight.{1,100}",element) is None) ):
              new_answer = new_answer + "<b>{}</b>".format(element) + "\n"
          return new_answer

    def Ping(self):
        PingList = list()
        for User in Guild.GuildList:
            if(((abs(User.ChatWarsLvl - self._MobsLevel)) <= self.RANGE_FOR_BATTLE_TAKE) and (User.isMain == True) ):
                PingList.append(User.Username)
        Bot.PingByFive(self.message.chat.id,PingList)

    def MobsLevel(self):
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

    def IsChampion(self):
        if(re.search("⚜️Forbidden Champion",self.message.text)):
            self.is_champion = True
            self.PinChamp()
            Bot.GivePots(self.message.chat.id)
            return True
        return False

    def DoUpdate(self):
            now = time.time()
            timers = "⏰: " + "<b>{}</b>".format("{:02d}:{:02d}".format(int((self.timer - (now - self.message.forward_date)) / 60),int((self.timer - (now - self.message.forward_date)) % 60)))
            answer = self.mobs_text + "\n" + timers + "\n\n" + "<b>👑 Хокаге по вызову:\n</b>" + self.Helpers()
            response = Bot.edit_message_text(answer, self.message.chat.id, self.message_for_update.message_id,
                                  parse_mode='HTML', reply_markup=self.MobsMarkups("⚔️ В бой", "🤝 Помогаю"))

    def TooManyReqestCheck(self,Response):
        try:
            return Response.result[1].result.status_code == 429
        except:
            return False

    def IsActualMob(self):

        return (time.time() - self.message.forward_date) < self.timer

    def PinChamp(self):
        Bot.pin_chat_message(self.message_for_update.chat.id, self.message_for_update.message_id, disable_notification = True)

    def IsAmbush(self):
        if (re.search("It's an ambush!", self.message.text)):
            self.is_ambush = True
            self.timer = 360
        self.is_ambush = False

    def MobsLink(self):
        link = re.search("\/fight.{1,100}", self.message.text)
        self.link = link.group(0)