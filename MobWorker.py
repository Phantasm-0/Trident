from Global import Bot
import re
from Mob import Mob
from Global import Guild

mob_list = []




def UserLevelUpdate(Message):
    text_list = Message.text.split('\n')
    for User in Guild.GuildList:
        for line in text_list:
            if(re.search(User.ChatWarsNickName, line)):
                preask = re.search("\d{2,3}\s\[",line)
                preanswer = preask.group(0)
                ask = re.search('\d{2,3}',preanswer)
                level = ask.group(0)
                User.ChangeLevel(level)





def update_helpers(call):
  for mob in mob_list:
      if (mob.link == call.data):
            if(mob.MobUpdateHelpers(call.from_user) is False):
                Bot.answer_callback_query(call.id, "Ты не пройдешь!", show_alert = True)
                return
  Bot.answer_callback_query(call.id)

def find_mobs_message(message):
  mob = Mob(message.from_user,None,message)
  mob.MobsLink()
  markup = mob.MobsMarkups("⚔️В бой", "🤝 Помогаю")
  message_for_update = Bot.send_message(message.chat.id, mob.mobs_text, reply_markup = markup, parse_mode='HTML')
  message_for_update = message_for_update.wait()
  mob.message_for_update = message_for_update
  mob_list.append(mob)
  mob.StartAndUpdating()
  mob_list.remove(mob)




